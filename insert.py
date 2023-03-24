import datetime
import json
from connect import get_conn


def insert_sport(s):
    conn = get_conn()
    cur = conn.cursor()  # 生成游标对象
    out = s.read()
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
                         User_ID, dt, Sport_Type, Sport_Number, Sport_Consume, Propose)
        result = cur.execute(sql_insert)  # 执行上述sql命令
        print(result)

    conn.commit()  # 提交推送
    cur.close()  # 关闭游标
    conn.close()  # 关闭连接


# f是传来的json，里面包含ID，Food_Name、Height
def insert_food_nutrition(Food_Name, Height):
    conn = get_conn()
    cur = conn.cursor()  # 生成游标对象
    sql = "select * from nurtition WHERE Food_Name=(%s) and Height=(%f) " % (Food_Name, Height)
    cur.execute(sql)  # 执行SQL语句
    rest = cur.fetchall()  # 这是获取表中全部数据，fetchall和fetchone
    s = []
    for i in rest:
        s += [i]
    conn.close()
    return s


def insert_food(f):
    conn = get_conn()
    cur = conn.cursor()  # 生成游标对象
    out = f.read()
    tmp = json.loads(out)
    for i in range(len(tmp)):
        User_ID = tmp[i]['User_ID']
        dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Food_Name = tmp[i]['Food_Name']
        Height = tmp[i]['Height']
        s = insert_food_nutrition(Food_Name, Height)
        sql_insert = "insert into sport (User_ID,Date,Food_Name,Height)" \
                     "values ('%d','%s','%s','%f')" % (
                         User_ID, dt, Food_Name, Height)
        result = cur.execute(sql_insert)  # 执行上述sql命令
        print(result)

    conn.commit()  # 提交推送
    cur.close()  # 关闭游标
    conn.close()  # 关闭连接
