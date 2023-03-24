from connect import get_conn


# 查询某一日的饮食(被之后函数调用）
def Get_Day_Eat(id, date):
    conn = get_conn()
    cur = conn.cursor()  # 生成游标对象
    sql = 'select * from eat WHERE User_ID=%s' % id
    cur.execute(sql)  # 执行SQL语句
    rest = cur.fetchall()  # 这是获取表中全部数据，fetchall和fetchone
    s = []
    for i in rest:
        if i[1].year == date.year and i[1].month == date.month and i[1].day == date.day:
            s += [i]
    conn.close()
    return s


# 查询某一日的饮食摄入卡路里
def Get_Day_Eat_cal(id, date):
    cal =0
    for i in Get_Day_Eat(id, date):
        cal += i[4]
    return cal


# 查询某一日的饮食种类
def Get_Day_Eat_type(id, date):
    t = []
    for i in Get_Day_Eat(id, date):
        t += [i]
    return t
