import datetime
import json
from connect import get_conn


def insert_sport():
    conn = get_conn()
    cur = conn.cursor()  # 生成游标对象
    a = open(r"test.json", "r", encoding='utf_8_sig')
    out = a.read()
    tmp = json.loads(out)
    for i in range(len(tmp)):
        User_ID = tmp[i]['User_ID']
        dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Sport_Type = tmp[i]['Sport_Type']
        Sport_Number = tmp[i]['Sport_Number']
        Sport_Consume = tmp[i]['Sport_Consume']
        Propose = tmp[i]['Propose']
        value = [User_ID, dt, Sport_Type, Sport_Number, Sport_Consume, Propose]
        # sql_insert = "insert into sport (User_ID,Date,Sport_Type,Sport_Number,Sport_Consume,Propose)" \
        #              "values ('d','%s','s','d','f','s')" ,value
        sql_insert = "insert into sport (User_ID,Date,Sport_Type,Sport_Number,Sport_Consume,Propose)" \
                     "values ('%d','%s','%s','%d','%f','%s')" % (
              User_ID, dt, Sport_Type, Sport_Number, Sport_Consume,  Propose)
        result = cur.execute(sql_insert)  # 执行上述sql命令
        print(result)

    conn.commit()  # 提交推送
    cur.close()  # 关闭游标
    conn.close()  # 关闭连接


# 这个版本的insert  可以插入测试数据，接下来编写可以传入数据的插入
def insert_sport_testNumber():
    conn = get_conn()
    cur = conn.cursor()  # 生成游标对象
    t = datetime.datetime.now()
    dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sql = "insert into sport (User_ID,Date,Sport_Type,Sport_Number,Sport_Consume,Propose)" \
          "values ('%d','%s','%s','%d','%f','%s')" % (
              555, dt, "test", 2, 2.5, "testtt")
    sql1 = "insert into sport(User_ID,Date)values('%s')" % (dt)
    result = cur.execute(sql)  # 执行SQL语句
    print(result)
    conn.commit()  # 提交推送
    cur.close()  # 关闭游标
    conn.close()  # 关闭连接


# 测试一下是否可以插入时间
def insert_test():
    conn = get_conn()
    cur = conn.cursor()  # 生成游标对象
    t = datetime.datetime.now()
    dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sql1 = "insert into test(time)values('%s')" % (dt)
    result = cur.execute(sql1)  # 执行SQL语句
    print(result)
    conn.commit()  # 提交推送
    cur.close()  # 关闭游标
    conn.close()  # 关闭连接
