
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
            "db": 1
        }
        redis = RedisAccessor(config_json)
        set_result = redis.set_string('set_redis', 'redis-connection')
        print("set_result", set_result)
        get_result = redis.get_string('set_redis')
        print("set_result", get_result, type(get_result))
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
