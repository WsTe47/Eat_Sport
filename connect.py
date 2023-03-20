import pymysql
import datetime

def get_conn():
    conn = pymysql.connect(host='123.60.48.133'  # 连接名称，默认127.0.0.1
                           , user='Climber47'  # 用户名
                           , passwd='Abcd4321'  # 密码
                           , port=3306  # 端口，默认为3306
                           , db='eat_sport'  # 数据库名称
                           , charset='utf8mb4'  # 字符编码
                           )
    return conn
