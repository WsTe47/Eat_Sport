from flask import Flask
import pymysql
import logging
from connect import get_conn


# index_dict = ["Food_Name", "Calorie", "Protein", "Fat", "CHO", "Salt", "Ca", "PP", "Fe", "Type_ID", "Food_ID"]
log = logging.getLogger("monitor.default")
app = Flask(__name__)
app.debug = True
if __name__ == "__main__":
    @app.route('/Hello', methods=['GET', 'POST'])
    def Hello():
        return "Hello"


    @app.route('/t1/<aa>', methods=['GET', 'POST'])
    def t1(aa):
        return aa
    @app.route('/ttt/<aaa>', methods=['GET', 'POST'])
    def ttt(aaa):
        conn = get_conn()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        # 生成游标对象
        sql = 'select * from nurtition WHERE Food_ID=%d' % int(aaa)
        cur.execute(sql)  # 执行SQL语句
        rest = cur.fetchone()  # 这是获取表中全部数据，fetchall和fetchone
        conn.close()
        return rest
app.run(host='0.0.0.0',port=666)

