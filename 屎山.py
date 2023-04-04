#import pymysql
import datetime
import eat
import json
import insert
from connect import get_conn
# a=datetime.datetime.now()
# print(eat.Get_Day_Eat_cal(2,a))

# print(insert.insert_food_nutrition('KFC', 1.1)[0])
def ttt(aaa):
    conn = get_conn()
    cur = conn.cursor()  # 生成游标对象
    sql = 'select * from nurtition WHERE Type_ID=%d' % aaa
    cur.execute(sql)  # 执行SQL语句
    rest = cur.fetchall()  # 这是获取表中全部数据，fetchall和fetchone
    s = []
    for i in rest:
        s += [i]
    conn.close()
    return s
print(ttt(1)[1])
# a = open(r"food_test.json", "r", encoding='utf_8_sig')
# insert.insert_food(a)
# print(Get_Food_Type(2))
# from Food import Get_Food_ID
# print(Get_Food_ID(2))
# a = open(r"C:\Users\76138\Desktop\sport_test.json", "r", encoding='utf_8_sig')
# out = a.read()
# tmp = json.dumps(out)
# tmp = json.loads(out)
# print(tmp)
# insert.insert_sport()

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

# # 这个版本的insert  可以插入测试数据，接下来编写可以传入数据的插入
# def insert_sport_testNumber():
#     conn = get_conn()
#     cur = conn.cursor()  # 生成游标对象
#     t = datetime.datetime.now()
#     dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     sql = "insert into sport (User_ID,Date,Sport_Type,Sport_Number,Sport_Consume,Propose)" \
#           "values ('%d','%s','%s','%d','%f','%s')" % (
#               555, dt, "test", 2, 2.5, "testtt")
#     sql1 = "insert into sport(User_ID,Date)values('%s')" % (dt)
#     result = cur.execute(sql)  # 执行SQL语句
#     print(result)
#     conn.commit()  # 提交推送
#     cur.close()  # 关闭游标
#     conn.close()  # 关闭连接
#
#
# # 测试一下是否可以插入时间
# def insert_test():
#     conn = get_conn()
#     cur = conn.cursor()  # 生成游标对象
#     t = datetime.datetime.now()
#     dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     sql1 = "insert into test(time)values('%s')" % (dt)
#     result = cur.execute(sql1)  # 执行SQL语句
#     print(result)
#     conn.commit()  # 提交推送
#     cur.close()  # 关闭游标
#     conn.close()  # 关闭连接
