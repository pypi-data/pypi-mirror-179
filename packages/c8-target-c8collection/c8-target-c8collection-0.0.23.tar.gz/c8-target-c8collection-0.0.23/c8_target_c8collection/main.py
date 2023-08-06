#!/usr/bin/env python3

import argparse
import io
import json
import sys

import jsonschema
from adjust_precision_for_schema import adjust_decimal_precision_for_schema
from c8 import C8Client, DocumentInsertError
from c8.collection import StandardCollection
from jsonschema import Draft4Validator
from singer import get_logger

logger = get_logger('c8_target_c8collection')


def emit_state(state):
    if state is not None:
        line = json.dumps(state)
        logger.debug('Emitting state {}'.format(line))
        sys.stdout.write("{}\n".format(line))
        sys.stdout.flush()


def try_upsert(collection: StandardCollection, record: dict):
    try:
        collection.insert(record)
    except DocumentInsertError as e:
        try:
            logger.warn(f'Failed to insert record: {record}. {e}. Hence, trying to update instead.')
            collection.update(record)
        except Exception as e:
            logger.warn(f'Failed to insert/update record: {record}. {e}')


def try_delete(collection: StandardCollection, _key: str):
    try:
        collection.delete(_key)
    except Exception as e:
        logger.warn(f'Failed to delete record with _key: {_key}. {e}')


def persist_messages(messages, target):
    state = None
    schemas = {}
    key_properties = {}
    validators = {}
    collections = []

    if target != None and target:
        if not client.has_collection(target):
            client.create_collection(name=target)
    else:
        for c in client.get_collections():
            if not c['system']:
                collections.append(c['name'])

    for message in messages:
        try:
            o = json.loads(message)
        except json.decoder.JSONDecodeError:
            logger.error("Unable to parse:\n{}".format(message))
            raise

        message_type = o['type']
        if message_type == 'RECORD':
            stream = o['stream']
            if stream not in schemas:
                raise Exception(
                    "A record for stream {}"
                    "was encountered before a corresponding schema".format(stream)
                )

            try:
                validators[stream].validate((o['record']))
            except jsonschema.ValidationError as e:
                logger.error(f"Failed parsing the json schema for stream: {stream}.")
                raise e

            if target == None or not target:
                if stream not in collections:
                    client.create_collection(name=stream)
                    collections.append(stream)
                    # Get Collecion Handle and Insert
                    coll = client.get_collection(stream)
            else:
                coll = client.get_collection(target)

            try:
                rec = o['record']
                try:
                    logger.info(f'key_properties are {key_properties}')
                    kps = key_properties[stream]
                    if len(kps) > 1:
                        logger.warn(f'Multiple key_properties found ({",".join(kps)}).'
                                    f' Only `{kps[0]}` will be considered.')
                    _key = rec[kps[0]].strip()
                    logger.info(f'_key is {_key}')
                    rec['_key'] = _key
                except:
                    _key = None
                if '_sdc_deleted_at' in rec:
                    if rec['_sdc_deleted_at']:
                        if _key:
                            try_delete(coll, _key)
                    else:
                        rec.pop('_sdc_deleted_at', None)
                        logger.info(f'record is {rec}')
                        try_upsert(coll, rec)
                else:
                    try_upsert(coll, rec)
            except TypeError as e:
                # TODO: This is temporary until json serializing issue for Decimals are fixed in pyC8
                logger.debug("pyC8 error occurred")

            state = None
        elif message_type == 'STATE':
            logger.debug('Setting state to {}'.format(o['value']))
            state = o['value']
        elif message_type == 'SCHEMA':
            stream = o['stream']
            schemas[stream] = o['schema']
            adjust_decimal_precision_for_schema(schemas[stream])
            validators[stream] = Draft4Validator((o['schema']))
            key_properties[stream] = o['key_properties']
        else:
            logger.warning("Unknown message type {} in message {}".format(o['type'], o))

    return state


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', help='Config file')
    args = parser.parse_args()

    if args.config:
        with open(args.config) as input_json:
            config = json.load(input_json)
    else:
        raise Exception(
            "Required '--config' parameter was not provided"
        )
    region = config['region']
    fabric = config['fabric']
    apikey = config['api_key']
    target_collection = config['target_collection']

    print("Create C8Client Connection")
    global client
    client = C8Client(
        protocol='https',
        host=region,
        port=443,
        apikey=apikey,
        geofabric=fabric
    )

    input_messages = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
    state = persist_messages(input_messages, target_collection)

    emit_state(state)
    logger.debug("Exiting normally")


if __name__ == '__main__':
    main()
