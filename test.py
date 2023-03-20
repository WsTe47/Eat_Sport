import pymysql
import datetime
import json
import insert
from connect import get_conn

# a = open(r"C:\Users\76138\Desktop\test.json", "r", encoding='utf_8_sig')
# out = a.read()
# tmp = json.dumps(out)
# tmp = json.loads(out)
# print(tmp)
insert.insert_sport()

# def Test():
#     conn = get_conn()
#     cur = conn.cursor()  # 生成游标对象
#     sql = 'select * from test '
#     cur.execute(sql)  # 执行SQL语句
#     rest = cur.fetchall()  # 这是获取表中全部数据，fetchall和fetchone
#     for i in rest:
#       print(i)
#     conn.close()
# Test()
# insert.insert_test()


# # datetime.datetime(2023, 3, 4, 0, 27, 31)       MySQL中的datetime返回为此值    <class 'datetime.datetime'>
#
#
# # 查询某一日的饮食摄入
#
# def Get_Day_Eat(id, date):
#     conn = get_conn()
#     cur = conn.cursor()  # 生成游标对象
#     sql = 'select * from eat WHERE User_ID=%s' % id
#     cur.execute(sql)  # 执行SQL语句
#     rest = cur.fetchall()  # 这是获取表中全部数据，fetchall和fetchone
#     cal=0
#     for i in rest:
#         if i[1].year == date.year and i[1].month == date.month and i[1].day == date.day:
#             cal+=i[3]
#     conn.close()
#     return cal
#
#
# def Get_Day_Sport(id, date):
#     conn = get_conn()
#     cur = conn.cursor()  # 生成游标对象
#     sql = 'select * from sport WHERE User_ID=%s' % id
#     cur.execute(sql)  # 执行SQL语句
#     rest = cur.fetchall()  # 这是获取表中全部数据，fetchall和fetchone
#     cal=0
#     for i in rest:
#         if i[1].year == date.year and i[1].month == date.month and i[1].day == date.day:
#             cal+=i[3]
#     conn.close()
#     return cal
#
#
# id = 1
# date = datetime.datetime.now()  # 测试用
# print(Get_Day_Eat(id, date))
