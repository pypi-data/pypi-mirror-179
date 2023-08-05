
import unittest


class AccessorTestCase(unittest.TestCase):

    def test_pgsql(self):
        from data_idr_access.pgsql_accessor import PgSqlAccessor
        config_json = {
            "host": "127.0.0.1",
            "port": "5432",
            "user": "admin",
            "password": "admin",
            "dbname": "userdb"
        }
        pg_connect = PgSqlAccessor(config_json)
        for item in pg_connect.read_data('speaker', ['id', 'name', 'code', 'gender'], "gender = 'male'"):
            print(item, type(item))

        self.assertTrue(True)

    def test_redis(self):
        from data_idr_access.redis_accessor import RedisAccessor
        config_json = {
            "pools": 100,
            "host": '127.0.0.1',
            "port": 6379,
            "db": 10
        }
        redis = RedisAccessor(config_json)
        set_result = redis.string.set_string('set_redis', 'redis-connection11111')
        print("set_result", set_result)
        get_result = redis.string.get_string('set_redis')
        print("set_result", get_result, type(get_result))

        set_zset = redis.zset.add_member("myzset", {"fra": 10, "spn": 5, "gen": 8})
        print("set_z_set", set_zset)
        get_zset = redis.zset.get_range_by_score("myzset", 8, 10, with_scores=True)
        print("get_z_set", get_zset)

        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
