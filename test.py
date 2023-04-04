from flask import Flask
import pymysql
import logging
from connect import get_conn


# index_dict = ["Food_Name", "Calorie", "Protein", "Fat", "CHO", "Salt", "Ca", "PP", "Fe", "Type_ID", "Food_ID"]


def ttt(aaa):
    conn = get_conn()
    # cur = conn.cursor(as_dict=True)  # 生成游标对象
    cur = conn.cursor(pymysql.cursors.DictCursor)
    sql = 'select * from nurtition WHERE Type_ID=%d' % aaa
    cur.execute(sql)  # 执行SQL语句
    rest = cur.fetchone()  # 这是获取表中全部数据，fetchall和fetchone

    conn.close()
    return rest


print(ttt(1))
print(type(ttt(1)))
