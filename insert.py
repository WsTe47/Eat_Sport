import datetime

from connect import get_conn


def insert_sport():
    conn = get_conn()
    cur = conn.cursor()  # 生成游标对象
    t = datetime.datetime.now()
    dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sql1 = "insert into user(id,age,name,create_time,update_time)values('%d','%d','%s','%s','%s')" % (1, 1, "1", dt, dt)
    sql = "insert into sport (User_ID,Date,Sport_Type,Sport_Number,Sport_Consume,Propose)values (%d,%s,%s,%d,%f,%s)" % (
        1, dt, "test", 2, 2.5, "testtt")
    result = cur.execute(sql)  # 执行SQL语句
    print(result)
    conn.commit()  # 提交推送
    cur.close()  # 关闭游标
    conn.close()  # 关闭连接

#测试一下是否可以插入时间
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
