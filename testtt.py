import pymysql
from connect import get_conn

# 连接数据库返回值带有字段名
def connectDB():
    conn = get_conn()
    cursor = conn.cursor(as_dict=True)
    sql = 'select * from nurtition WHERE Type_ID=%d' % aaa
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            print(row['EQUIP_NAME'], row['UNCERTAINTY'], row['STATUS'])

    except:
        print('列名错误！')
    cursor.close()
    conn.close()


if __name__ == '__main__':
    connectDB()
