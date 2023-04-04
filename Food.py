from connect import get_conn
def Get_Food_Type(type_id):
    conn = get_conn()
    cur = conn.cursor()  # 生成游标对象
    sql = 'select * from nurtition WHERE Type_ID=%d' % type_id
    cur.execute(sql)  # 执行SQL语句
    rest = cur.fetchall()  # 这是获取表中全部数据，fetchall和fetchone
    s = []
    for i in rest:
        s += [i]
    conn.close()
    return s

def Get_Food_ID(food_id):
    conn = get_conn()
    cur = conn.cursor()  # 生成游标对象
    sql = 'select * from nurtition WHERE Food_ID=%d' % food_id
    cur.execute(sql)  # 执行SQL语句
    rest = cur.fetchall()  # 这是获取表中全部数据，fetchall和fetchone

    conn.close()
    return rest




