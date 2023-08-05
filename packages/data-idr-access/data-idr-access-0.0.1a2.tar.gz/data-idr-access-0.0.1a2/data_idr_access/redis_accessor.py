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
                self._pool = redis.ConnectionPool(max_connections=pool_number, **config_json_copy,
                                                  decode_responses=True)
            else:
                self._pool = redis.ConnectionPool(max_connections=pool_number, **config_json_copy)
            self.conn = redis.Redis(connection_pool=self._pool)
        else:
            self._pool = None
            if 'decode_responses' not in config_json_copy:
                self.conn = redis.Redis(**config_json_copy, decode_responses=True)
            else:
                self.conn = redis.Redis(**config_json_copy)

        self.string = RedisString(self.conn)
        self.hash = RedisHash(self.conn)
        self.list = RedisList(self.conn)
        self.set = RedisSet(self.conn)
        self.zset = RedisZset(self.conn)

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

        self.string = RedisString(self.conn)
        self.hash = RedisHash(self.conn)
        self.list = RedisList(self.conn)
        self.set = RedisSet(self.conn)
        self.zset = RedisZset(self.conn)

    def disconnect(self):
        if self.conn:
            self.conn.close()
        if self._pool:
            self._pool.disconnect()
        self.string = None
        self.hash = None
        self.list = None
        self.set = None
        self.zset = None

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


class RedisString:

    def __init__(self, redis_conn):
        self.redis = redis_conn

    # 字符串及数值相关方法
    def set_string(self, name, value, ex=None, **kwargs):
        """向string键添加或修改值"""
        if ex:
            return self.redis.set(name, value, ex=ex, **kwargs)
        else:
            return self.redis.set(name, value, **kwargs)

    def set_strings(self, json):
        """批量设置string键的值"""
        return self.redis.mset(json)

    def get_string(self, name):
        """获取string键的值"""
        return self.redis.get(name)

    def get_length(self, name):
        """获取string的值长度"""
        return self.redis.strlen(name)

    def incr(self, name, amount=1):
        """自增对应string键的值"""
        if type(amount) == float:
            return self.redis.incrbyfloat(name, amount)
        return self.redis.incr(name, amount)

    def decr(self, name, amount=1):
        """自减对应string键的值"""
        return self.redis.decr(name, amount)


class RedisHash:

    def __init__(self, redis_conn):
        self.redis = redis_conn

    # hash类方法
    def set_hash(self, name, key, value, nx=None):
        """设置hash键的值"""
        if nx:
            return self.redis.hsetnx(name, key, value)
        return self.redis.hset(name, key, value)

    def set_hash_json(self, name, json):
        """使用mapping批量设置hash键的多个键值"""
        return self.redis.hset(name, mapping=json)

    def get_all_keys(self, name):
        """获取hash键的所有的key值"""
        return self.redis.hkeys(name)

    def get_all_values(self, name):
        """获取hash键的所有的value值"""
        return self.redis.hvals(name)

    def key_exists(self, name, key):
        """判断hash键中指定key是否存在"""
        return self.redis.hexists(name, key)

    def get_all(self, name):
        """获取hash键中所有的键值对"""
        return self.redis.hgetall(name)

    def get_value(self, name, key=None, keys=None):
        """获取hash键中指定键的值"""
        if keys:
            return self.redis.hmget(name, keys)
        return self.redis.hget(name, key)

    def del_by_keys(self, name, *keys):
        """删除hash键中指定的键值对"""
        return self.redis.hdel(name, *keys)

    def get_scan(self, name, cursor=0, match=None, count=None):
        """有条件的获取hash键的中的键值对"""
        return self.redis.hscan(name, cursor, match, count)


class RedisList:

    def __init__(self, redis_conn):
        self.redis = redis_conn

    # 列表相关方法
    def push_value(self, name, direct='l', ex=False, *values):
        """从指定方向向list键中添加值"""
        if direct == 'r':
            if ex:
                return self.redis.rpushx(name, *values)
            return self.redis.rpush(name, *values)
        if ex:
            return self.redis.lpushx(name, *values)
        return self.redis.lpush(name, *values)

    def set_value(self, name, index, value):
        """设置list键中指定index的值"""
        return self.redis.lset(name, index, value)

    def insert_value(self, name, value, ref, where="after"):
        """向list键中指定位置插值"""
        return self.redis.linsert(name, where, ref, value)

    def get_length(self, name):
        """获取list键中的元素数量"""
        return self.redis.llen(name)

    def get_range(self, name, start=0, end=-1):
        """获取list键中指定范围的所有值"""
        return self.redis.lrange(name, start, end)

    def get_by_index(self, name, index):
        """获取list键中制定index的值"""
        return self.redis.lindex(name, index)

    def pop(self, name, num=None, direct='l'):
        """按指定方向删除并返回list键中的值"""
        if direct == 'r':
            if num:
                return self.redis.rpop(name, num)
            return self.redis.rpop(name)
        if num:
            self.redis.lpop(name, num)
        return self.redis.lpop(name)

    def del_by_index(self, name, value, del_num=0):
        """删除list键中指定的值"""
        return self.redis.lrem(name, value, del_num)


class RedisSet:

    def __init__(self, redis_conn):
        self.redis = redis_conn

    # 集合相关方法
    def add_members(self, name, *values):
        """向set键集合中添加元素"""
        return self.redis.sadd(name, *values)

    def get_length(self, name):
        """获取set键中的元素数量"""
        return self.redis.scard(name)

    def get_members(self, name):
        """获取set键中的所有元素"""
        return self.redis.smembers(name)

    def get_scan(self, name, cursor=0, match=None, count=None):
        """有条件的获取set键中的所有元素"""
        return self.redis.sscan(name, cursor, match, count)

    def get_exists(self, name, value):
        """判断set键中是否存在指定值"""
        return self.redis.sismember(name, value)

    def get_diff(self, *keys, dest=None):
        """计算并获取（存储）指定多个set键的差集"""
        if not dest:
            return self.redis.sdiff(*keys)
        return self.redis.sdiffstore(dest, *keys)

    def get_inter(self, *keys, dest=None):
        """计算并获取（存储）指定多个set键的交集"""
        if not dest:
            return self.redis.sinter(*keys)
        return self.redis.sinterstore(dest, *keys)

    def get_union(self, *keys, dest=None):
        """计算并获取（存储）指定多个set键的并集"""
        if not dest:
            return self.redis.sunion(*keys)
        return self.redis.sunion(dest, *keys)

    def move_member(self, src, dst, value):
        """将指定值从一个set键中取出并存入另一个set键中"""
        return self.redis.smove(src, dst, value)

    def pop_rand(self, name):
        """随机删除并返回set键中的元素"""
        return self.redis.spop(name)

    def del_by_value(self, name, *values):
        """删除set键中的指定元素"""
        return self.redis.srem(name, *values)


class RedisZset:

    def __init__(self, redis_conn):
        self.redis = redis_conn

    # 有序集合方法
    def add_member(self, name, mappings, add_type="", changed=False):
        """向zset中添加元素及对应分值"""
        if add_type == "nx":
            return self.redis.zadd(name, mappings, nx=True, ch=changed)
        if add_type == "xx":
            return self.redis.zadd(name, mappings, xx=True, ch=changed)
        return self.redis.zadd(name, mappings, ch=changed)

    def get_length(self, name):
        """获取zset中元素数量"""
        return self.redis.zcard(name)

    def get_range_by_index(self, name, start=0, end=-1, desc=False, with_scores=False):
        """获取zset中索引范围在 [min, max] 中的元素"""
        return self.redis.zrange(name, start, end, desc=desc, withscores=with_scores)

    def get_range_by_score(self, name, min, max, with_scores=False, start=None, num=None):
        """获取zset中分值范围在 [min, max] 中的元素"""
        return self.redis.zrangebyscore(name, min, max, start=start, num=num, withscores=with_scores)

    def get_scan(self, name, cursor=0, match=None, count=None):
        """有条件的获取zset中的所有元素"""
        return self.redis.zscan(name, cursor=cursor, match=match, count=count)

    def get_count_by_score(self, name, min, max):
        """获取有序集合中分值在 [min, max]之间的元素数"""
        return self.redis.zcount(name, min, max)

    def get_index_by_value(self, name, value, desc=False):
        """获取zset中分值对应的索引位置，默认从小到大排序"""
        if desc:
            return self.redis.zrevrank(name, value)
        return self.redis.zrank(name, value)

    def get_score_by_value(self, name, value):
        """获取zset中对应元素的分数"""
        return self.redis.zscore(name, value)

    def set_value_incr(self, name, value, amount):
        """对指定元素分数进行自增"""
        return self.redis.zincrby(name, value, amount)

    def del_values(self, name, *values):
        """删除zset中的元素"""
        return self.redis.zrem(name, *values)

    def del_by_score(self, name, min, max):
        """删除zset中分值范围在 [min, max] 中的元素"""
        return self.redis.zremrangebyscore(name, min, max)

    def del_by_index(self, name, min, max):
        """删除zset中索引范围在 [min, max] 中的元素"""
        return self.redis.zremrangebyrank(name, min, max)
