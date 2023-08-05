import collections
import psycopg2
from data_idr_access.accessor import Accessor


class PgSqlAccessor(Accessor):
    def __init__(self, config_json):
        super().__init__(config_json)
        self.conn = psycopg2.connect(**config_json)

    def reconnect(self):
        self.disconnect()
        self.conn = psycopg2.connect(self.config)

    def disconnect(self, commit=False):
        if self.conn:
            if commit:
                self.conn.commit()
            self.conn.close()

    def get_conn(self):
        return self.conn

    def get_connect_info(self):
        return self.conn.info()

    def run_execute(self, sql, commit=True):
        try:
            cur = self.conn.cursor()
            cur.execute(sql)
            if commit:
                self.conn.commit()
        except Exception:
            self.conn.rollback()
            return False
        return True

    def run_query(self, sql):
        result_list = []
        try:
            cur = self.conn.cursor()
            cur.execute(sql)
            result_list = cur.fetchall()
            self.conn.close()
        except Exception as e:
            print(e)
        return result_list

    def create_table(self, table_name, structs: list):
        # 名称，类型，是否主键，是否为空，是否可重复，默认值
        structs_statments = []
        for col in structs:
            col_name = col.get('name')
            col_type = col.get('type')
            stat = f"{col_name} {col_type}"
            primary = col.get('primary', False)
            not_null = col.get('not_null', False)
            unique = col.get('unique', False)
            default = col.get('default')
            if primary:
                stat += " PRIMARY KEY"
            if not_null:
                stat += " NOT NULL"
            if unique:
                stat += " UNIQUE"
            if default:
                stat += " DEFAULT {}".format(default)

            structs_statments.append(stat)

        structs = ",\n".join(structs_statments)
        sql = f"CREATE TABLE {table_name} ({structs});"
        print("Create table statement: {}".format(sql))
        try:
            cur = self.conn.cursor()
            cur.execute(sql)
            self.conn.commit()
        except Exception:
            self.conn.rollback()
            return False
        return True

    def show_user_table(self):
        tables = []
        cur = self.conn.cursor()
        cur.execute(f"SELECT tablename,tableowner FROM pg_tables WHERE schemaname='public';")
        rows = cur.fetchall()
        for row in rows:
            tables.append([row[0], row[1]])
        return tables

    def rename_table(self, src_name, dest_name):
        try:
            cur = self.conn.cursor()
            cur.execute(f"RENAME TABLE {src_name} to {dest_name};")
            self.conn.commit()
        except Exception:
            self.conn.rollback()
            return False
        return True

    def add_table_col(self, table_name, col_name, col_type):
        try:
            cur = self.conn.cursor()
            cur.execute(f"ALTER TABLE {table_name} ADD {col_name} {col_type};")
            self.conn.commit()
        except Exception:
            self.conn.rollback()
            return False
        return True

    def drop_table_col(self, table_name, col_name):
        try:
            cur = self.conn.cursor()
            cur.execute(f"ALTER TABLE {table_name} DROP {col_name};")
            self.conn.commit()
        except Exception:
            self.conn.rollback()
            return False
        return True

    def rename_table_col(self, table_name, src_name, dest_name):
        try:
            cur = self.conn.cursor()
            cur.execute(f"ALTER TABLE {table_name} RENAME COLUMN {src_name} TO {dest_name};")
            self.conn.commit()
        except Exception:
            self.conn.rollback()
            return False
        return True

    def alter_table_col_type(self, table_name, col_name, col_type):
        try:
            cur = self.conn.cursor()
            cur.execute(f"ALTER TABLE {table_name} ALTER COLUMN {col_name} TYPE {col_type};")
            self.conn.commit()
        except Exception:
            self.conn.rollback()
            return False
        return True

    def alter_table(self, table_name, alter_sql):
        raise Exception("Not implemented")

    def truncate_table(self, table_name):
        try:
            cur = self.conn.cursor()
            cur.execute(f"TRUNCATE TABLE {table_name};")
            self.conn.commit()
        except Exception:
            self.conn.rollback()
            return False
        return True

    def drop_table(self, table_name):
        try:
            cur = self.conn.cursor()
            cur.execute(f"DROP TABLE {table_name};")
            self.conn.commit()
        except Exception:
            self.conn.rollback()
            return False
        return True

    def create_index(self, index_name, table, columns, unique=False):
        try:
            cur = self.conn.cursor()
            if isinstance(columns, list):
                columns = ", ".join(columns)
            if unique:
                cur.execute(f"CREATE UNIQUE INDEX {index_name} ON {table}({columns});")
            else:
                cur.execute(f"CREATE INDEX {index_name} ON {table}({columns});")
            self.conn.commit()
        except Exception:
            self.conn.rollback()
            return False
        return True

    def delete_index(self, index_name):
        try:
            cur = self.conn.cursor()
            cur.execute(f"DROP INDEX {index_name};")
            self.conn.commit()
        except Exception:
            self.conn.rollback()
            return False
        return True

    # CRUD
    def create_data(self, table, data: dict):
        keys, values = [], []
        for key, value in data.items():
            keys.append(key)
            values.append(f'\'{value}\'' if isinstance(value, str) else value)
        sql = f"INSERT INTO {table} ({', '.join(keys)}) VALUES ({', '.join(values)});"
        print("Create data statement: {}".format(sql))
        try:
            cur = self.conn.cursor()
            cur.execute(sql)
            self.conn.commit()
        except Exception:
            self.conn.rollback()
            return False
        return True

    def read_data(self, table, data_filter, condition=None, distinct=False):
        if isinstance(data_filter, list):
            data_filter = ', '.join(data_filter)
        cur = self.conn.cursor()
        distinct_stat = ""
        if distinct:
            distinct_stat = "DISTINCT "
        if condition:
            sql = f"SELECT {distinct_stat}{data_filter} FROM {table} WHERE {condition};"
        else:
            sql = f"SELECT {distinct_stat}{data_filter} FROM {table};"
        print("Retrieve data statement: {}".format(sql))
        cur.execute(sql)
        rows = cur.fetchall()
        for row in rows:
            yield row
        return None

    def update_data(self, table, update_data, condition=None):
        statement = []
        for key, value in update_data.items():
            statement.append(f'{key} = \'{value}\'' if isinstance(value, str) else f'{key} = {value}')

        if condition:
            sql = f"UPDATE {table} SET {', '.join(statement)} WHERE {condition};"
        else:
            sql = f"UPDATE {table} SET {', '.join(statement)};"
        print("Update data statement: {}".format(sql))
        try:
            cur = self.conn.cursor()
            cur.execute(sql)
            self.conn.commit()
        except Exception:
            self.conn.rollback()
            return False
        return True

    def delete_data(self, table, condition=None):
        if condition:
            sql = f"DELETE FROM {table} WHERE {condition};"
        else:
            sql = f"DELETE FROM {table};"
        print("Delete data statement: {}".format(sql))
        try:
            cur = self.conn.cursor()
            cur.execute(sql)
            self.conn.commit()
        except Exception:
            self.conn.rollback()
            return False
        return True
