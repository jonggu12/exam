import pymysql

conn, cur = None, None

data1, data2, data3, data4 = '','','',''

sql = ""

conn = pymysql.connect(host='localhost',user='root', \
                        db='shoppingDB', charset='utf8')


cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS userTable (id char(4),userName \
            char(15),email char(20),birthYear int)")

conn.close()