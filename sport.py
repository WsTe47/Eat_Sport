from connect import get_conn


# 2名称 3个数 4热量 5运动建议
# 返回一个包含运动内容的数组，其中有运动名称、运动个数、消耗热量、运动建议。
def Get_Day_Sport(id, date):
    conn = get_conn()
    cur = conn.cursor()  # 生成游标对象
    sql = 'select * from sport WHERE User_ID=%s' % id
    cur.execute(sql)  # 执行SQL语句
    rest = cur.fetchall()  # 这是获取表中全部数据，fetchall和fetchone
    s = []
    for i in rest:
        if i[1].year == date.year and i[1].month == date.month and i[1].day == date.day:
            s += [i]
    conn.close()
    return s


def Get_Day_Sport_cal(id, date):
    cal = 0
    for i in Get_Day_Sport(id, date):
        cal += i[4]
    return cal


# 查询某一日的饮食种类
def Get_Day_Sport_type(id, date):
    t = []
    for i in Get_Day_Sport(id, date):
        t += [i]
    return t
