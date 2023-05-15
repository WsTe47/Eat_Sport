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

    @app.route('/Login/<User,Pwd>', methods=['GET', 'POST'])
    def Login(User,Pwd):
        conn = get_conn()
        cur = conn.cursor()  # 生成游标对象
        sql = 'select * from person WHERE User=%s and Password=%s' % User,Pwd
        cur.execute(sql)  # 执行SQL语句
        rest = cur.fetchall()  # 这是获取表中全部数据，fetchall和fetchone
        if rest:
            return True
        else:
            return False


app.run(host='0.0.0.0',port=666)
