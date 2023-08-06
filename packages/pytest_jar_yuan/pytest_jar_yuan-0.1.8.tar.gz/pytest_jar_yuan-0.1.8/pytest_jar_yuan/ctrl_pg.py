# -*- coding:utf-8 -*-
# @Author: huang-jy
import psycopg2 as pg


"""
form pytest_jar_yuan.ctrl_pg import ConnectPg, UsePg

ConnectPg.kHost = "127.0.0.1"
ConnectPg.kPort = "5433"
ConnectPg.kUser = "test_user"
ConnectPg.kPassword = "test_password"
ConnectPg.kDatabase = "test_db"
"""


class ConnectPg:
    kHost = ""
    kPort = 0
    kUser = ""
    kPassword = ""
    kDatabase = ""


class UsePg:
    @staticmethod
    def connect_pg():
        if ConnectPg.kHost == "":
            raise AssertionError("ConnectPg.kHost 不能为空")
        if ConnectPg.kPort == 0:
            raise AssertionError("ConnectPg.kPort 端口号未设置")
        if ConnectPg.kUser == "":
            raise AssertionError("ConnectPg.kUser 不能为空")
        if ConnectPg.kPassword == "":
            raise AssertionError("ConnectPg.kPassword 不能为空")
        if ConnectPg.kDatabase == "":
            raise AssertionError("ConnectPg.kDatabase 不能为空")
        return pg.connect(host=ConnectPg.kHost, port=ConnectPg.kPort,
                          user=ConnectPg.kUser, password=ConnectPg.kPassword, database=ConnectPg.kDatabase)

    def insert_to_pg(self, sql_col_name, sql_value):
        sql = f'INSERT INTO test_result({sql_col_name}) VALUE ({sql_value})'
        print(sql)
        with self.connect_pg() as pg_conn:
            pg_conn.cursor().execute(sql)

    def query_from_pg(self, query_sql):
        with self.connect_pg() as pg_conn:
            this_cursor = pg_conn.cursor()
            this_cursor.execute(query_sql)
            for row in this_cursor.fetchall():
                print(row)


if __name__ == '__main__':
    pass
