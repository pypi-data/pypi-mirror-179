#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class UnimplementedException(Exception):
    def __init__(self, message, status):
        super().__init__(message, status)
        self.message = "UnimplementedFunction: " + message
        self.status = status


class Accessor(object):
    def __init__(self, config_json):
        self.config = config_json
        self.conn = None

    def reconnect(self):
        raise UnimplementedException('Unimplemented reconnect', 0)

    def disconnect(self):
        raise UnimplementedException('Unimplemented disconnect', 0)

    def run(self):
        raise UnimplementedException('Unimplemented run', 0)


