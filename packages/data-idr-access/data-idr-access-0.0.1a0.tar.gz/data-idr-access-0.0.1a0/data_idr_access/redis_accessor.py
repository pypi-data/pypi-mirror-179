import redis
import copy
from data_idr_access.accessor import Accessor


class RedisAccessor(Accessor):
    def __init__(self, config_json):
        super().__init__(config_json)
        config_json_copy = copy.deepcopy(config_json)
        if 'pools' in config_json_copy:
            pool_number = config_json_copy.pop('pools')
            if 'decode_responses' not in config_json_copy:
                self._pool = redis.ConnectionPool(max_connections=pool_number, **config_json_copy, decode_responses=True)
            else:
                self._pool = redis.ConnectionPool(max_connections=pool_number, **config_json_copy)
            self.conn = redis.Redis(connection_pool=self._pool)
        else:
            self._pool = None
            if 'decode_responses' not in config_json_copy:
                self.conn = redis.Redis(**config_json_copy, decode_responses=True)
            else:
                self.conn = redis.Redis(**config_json_copy)

    def reconnect(self):
        self.disconnect()
        config_json = copy.deepcopy(self.config)
        if 'pools' in config_json:
            pool_number = config_json.pop('pools')
            if 'decode_responses' not in config_json:
                self._pool = redis.ConnectionPool(max_connections=pool_number, **config_json, decode_responses=True)
            else:
                self._pool = redis.ConnectionPool(max_connections=pool_number, **config_json)
            self.conn = redis.Redis(connection_pool=self._pool)
        else:
            self._pool = None
            if 'decode_responses' not in config_json:
                self.conn = redis.Redis(**config_json, decode_responses=True)
            else:
                self.conn = redis.Redis(**config_json)

    def disconnect(self):
        if self.conn:
            self.conn.close()
        if self._pool:
            self._pool.disconnect()

    def get_conn(self):
        return self.conn

    def get_pool(self):
        return self._pool

    # 通用方法
    def delete(self, *names):
        return self.conn.delete(*names)

    def exists(self, *names):
        return self.conn.exists(*names)

    def expire(self, name, time):
        return self.conn.expire(name, time)

    def type(self, name):
        return self.conn.type(name)

    # 字符串及数值相关方法
    def set_string(self, name, value, ex=None, **kwargs):
        """向string键添加或修改值"""
        if ex:
            return self.conn.set(name, value, ex=ex, **kwargs)
        else:
            return self.conn.set(name, value, **kwargs)

    def mset_string(self, json):
        """批量设置string键的值"""
        return self.conn.mset(json)

    def get_string(self, name):
        """获取string键的值"""
        return self.conn.get(name)

    def get_string_len(self, name):
        return self.conn.strlen(name)

    def incr(self, name, amount=1):
        if type(amount) == float:
            return self.conn.incrbyfloat(name, amount)
        return self.conn.incr(name, amount)

    def decr(self, name, amount=1):
        return self.conn.decr(name, amount)

    # hash类方法
    def set_hash(self, name, key, value, nx=None):
        if nx:
            return self.conn.hsetnx(name, key, value)
        return self.conn.hset(name, key, value)

    def set_hash_json(self, name, json):
        return self.conn.hset(name, mapping=json)

    def get_hash_keys(self, name):
        return self.conn.hkeys(name)

    def get_hash_values(self, name):
        return self.conn.hvals(name)

    def get_hash_exists(self, name, key):
        return self.conn.hexists(name, key)

    def get_hash_all(self, name):
        return self.conn.hgetall(name)

    def get_hash(self, name, key=None, keys=None):
        if keys:
            return self.conn.hmget(name, keys)
        return self.conn.hget(name, key)

    def del_hash(self, name, *keys):
        return self.conn.hdel(name, *keys)

    def get_hash_scan(self, name, cursor=0, match=None, count=None):
        return self.conn.hscan(name, cursor, match, count)

    # 列表相关方法
    def set_list_index(self, name, index, value):
        return self.conn.lset(name, index, value)

    def set_list_push(self, name, direct='l', *values):
        if direct == 'r':
            return self.conn.rpush(name, *values)
        return self.conn.lpush(name, *values)

    def get_list_len(self, name):
        return self.conn.llen(name)

    def get_list_range(self, name, start=0, end=-1):
        return self.conn.lrange(name, start, end)

    def get_list_index(self, name, index):
        return self.conn.lindex(name, index)

    def del_list_pop(self, name, num=None, direct='l'):
        if direct == 'r':
            if num:
                return self.conn.rpop(name, num)
            return self.conn.rpop(name)
        if num:
            self.conn.lpop(name, num)
        return self.conn.lpop(name)

    def del_list_index(self, name, value, del_num=0):
        return self.conn.lrem(name, value, del_num)

    # 集合相关方法
    def add_set(self, name, *values):
        return self.conn.sadd(name, *values)

    def get_set_len(self, name):
        return self.conn.scard(name)

    def get_set_members(self, name):
        return self.conn.smembers(name)

    def get_set_scan(self, name, cursor=0, match=None, count=None):
        return self.conn.sscan(name, cursor, match, count)

    def get_set_exists(self, name, value):
        return self.conn.sismember(name, value)

    def get_set_diff(self, *keys, dest=None):
        if not dest:
            return self.conn.sdiff(*keys)
        return self.conn.sdiffstore(dest, *keys)

    def get_set_inter(self, *keys, dest=None):
        if not dest:
            return self.conn.sinter(*keys)
        return self.conn.sinterstore(dest, *keys)

    def get_set_union(self, *keys, dest=None):
        if not dest:
            return self.conn.sunion(*keys)
        return self.conn.sunion(dest, *keys)

    def del_set_pop(self, name):
        return self.conn.spop(name)

    def del_set_value(self, name, *values):
        return self.conn.srem(name, *values)

    # 有序集合方法
    def add_zset(self, name, mappings, add_type="", changed=False):
        """向zset中添加元素及对应分值"""
        if add_type == "nx":
            return self.conn.zadd(name, mappings, nx=True, ch=changed)
        if add_type == "xx":
            return self.conn.zadd(name, mappings, xx=True, ch=changed)
        return self.conn.zadd(name, mappings, ch=changed)

    def get_zset_len(self, name):
        """获取zset中元素个数"""
        return self.conn.zcard(name)

    def get_zset_range(self, name, start=0, end=-1, desc=False, with_scores=False):
        """获取zset中索引范围在 [min, max] 中的元素"""
        return self.conn.zrange(name, start, end, desc=desc, withscores=with_scores)

    def get_zset_range_by_score(self, name, min, max, with_scores=False, start=None, num=None):
        """获取zset中分值范围在 [min, max] 中的元素"""
        return self.conn.zrangebyscore(name, min, max, start=start, num=num, withscores=with_scores)

    def get_zset_scan(self, name, cursor=0, match=None, count=None):
        """获取zset中的所有元素"""
        return self.conn.zscan(name, cursor=cursor, match=match, count=count)

    def get_zset_count(self, name, min, max):
        """获取有序集合中分值在 [min, max]之间的元素数"""
        return self.conn.zcount(name, min, max)

    def get_zset_index(self, name, value, desc=False):
        """获取zset中分值对应的索引位置，默认从小到大排序"""
        if desc:
            return self.conn.zrevrank(name, value)
        return self.conn.zrank(name, value)

    def get_zset_score(self, name, value):
        """获取zset中对应元素的分数"""
        return self.conn.zscore(name, value)

    def set_zset_incr(self, name, value, amount):
        """对指定元素分数进行自增"""
        return self.conn.zincrby(name, value, amount)

    def del_zset_value(self, name, *values):
        """删除zset中的元素"""
        return self.conn.zrem(name, *values)

    def del_zset_by_score(self, name, min, max):
        """删除zset中分值范围在 [min, max] 中的元素"""
        return self.conn.zremrangebyscore(name, min, max)

    def del_zset_by_index(self, name, min, max):
        """删除zset中索引范围在 [min, max] 中的元素"""
        return self.conn.zremrangebyrank(name, min, max)
