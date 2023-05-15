from flask import Flask, jsonify
import pymysql
import logging
def get_conn():
    conn = pymysql.connect(host='123.60.48.133'  # 连接名称，默认127.0.0.1
                           , user='Climber47'  # 用户名
                           , passwd='Abcd4321'  # 密码
                           , port=3306  # 端口，默认为3306
                           , db='eat_sport'  # 数据库名称
                           , charset='utf8mb4'  # 字符编码
                           )
    return conn

log = logging.getLogger("monitor.default")
app = Flask(__name__)
app.debug = True
if __name__ == "__main__":

    @app.route('/Hello', methods=['GET', 'POST'])
    def Hello():
        return "Hello"
    @app.route('/Get_Food_Type', methods=['GET', 'POST'])
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
    @app.route('/Get_Food_ID/<food_id>', methods=['GET', 'POST'])
    def Get_Food_ID(food_id):
        conn = get_conn()
        cur = conn.cursor(pymysql.cursors.DictCursor)  # 生成游标对象
        sql = 'select * from nurtition WHERE Food_ID=%d' % int(food_id)
        cur.execute(sql)  # 执行SQL语句
        rest = cur.fetchone()  # 这是获取表中全部数据，fetchall和fetchone

        conn.close()
        return jsonify(rest)


    # 查询某一日的饮食(被之后函数调用）
    def Get_Day_Eat(id, date):
        conn = get_conn()
        cur = conn.cursor()  # 生成游标对象
        sql = 'select * from eat WHERE User_ID=%d' % id
        cur.execute(sql)  # 执行SQL语句
        rest = cur.fetchall()  # 这是获取表中全部数据，fetchall和fetchone
        s = []
        for i in rest:
            if i[1].year == date.year and i[1].month == date.month and i[1].day == date.day:
                s += [i]
        conn.close()
        return s


    # 查询某一日的饮食摄入卡路里
    @app.route('/Get_Day_Eat_cal', methods=['GET', 'POST'])
    def Get_Day_Eat_cal(id, date):
        cal = 0
        for i in Get_Day_Eat(id, date):
            cal += i[4]
        return cal


    # 查询某一日的饮食种类
    @app.route('/Get_Day_Eat_type', methods=['GET', 'POST'])
    def Get_Day_Eat_type(id, date):
        t = []
        for i in Get_Day_Eat(id, date):
            t += [i]
        return t


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

    @app.route('/Get_Day_Sport_cal', methods=['GET', 'POST'])
    def Get_Day_Sport_cal(id, date):
        cal = 0
        for i in Get_Day_Sport(id, date):
            cal += i[4]
        return cal

    @app.route('/Get_Day_Sport_type', methods=['GET', 'POST'])
    def Get_Day_Sport_type(id, date):
        t = []
        for i in Get_Day_Sport(id, date):
            t += [i]
        return t

app.run(host='0.0.0.0',port=666)
