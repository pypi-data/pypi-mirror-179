#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import logging
import hashlib
from gevent.lock import Semaphore

import data_idr_access.accessor as accessor
from data_idr_access.kafka_accessor import KafkaAccessor
from data_idr_access.pgsql_accessor import PgSqlAccessor
from data_idr_access.redis_accessor import RedisAccessor

logger = logging.getLogger(__name__)


ACCESS_SELECTOR = {
    "pgsql": PgSqlAccessor,
    "redis": RedisAccessor,
    "kafka": KafkaAccessor
}

ACCESS_SUPPORTED = ['pgsql', 'redis', 'kafka']


def string_to_md5(content):
    """将string转化为MD5"""
    md5hash = hashlib.md5(content)
    md5 = md5hash.hexdigest()
    return md5


class AccessorSingleton:
    lock = Semaphore()
    __instance = {}

    def __init__(self):
        logger.info("init Singleton function.")

    @classmethod
    def list_keys(cls):
        return cls.__instance.keys()

    @classmethod
    def list_instances(cls):
        return cls.__instance.values()

    @classmethod
    def delete_instance(cls, instance_key):
        return cls.__instance.pop(instance_key)

    @classmethod
    def get_instance(cls, db_type, config_json=None) -> accessor.Accessor:
        """
        缓存初始化方法
        :return: accessor.Accessor
        """
        assert db_type in ACCESS_SUPPORTED, "Database Type Error: {}".format(db_type)
        key_md5 = db_type + ":" + string_to_md5(json.dumps(config_json, sort_keys=True) if config_json else "")
        with cls.lock:
            if key_md5 in cls.__instance:
                return cls.__instance[key_md5]
            logger.info("Init accessor with {}...".format(config_json))
            AccessorSingleton.__instance[key_md5] = ACCESS_SELECTOR[type](config_json)

        return AccessorSingleton.__instance[key_md5]

    @classmethod
    def clean_instance(cls, db_type, config_json):
        key_md5 = db_type + ":" + string_to_md5(json.dumps(config_json, sort_keys=True) if config_json else "")
        if key_md5 in AccessorSingleton.__instance:
            AccessorSingleton.__instance.pop(key_md5)
