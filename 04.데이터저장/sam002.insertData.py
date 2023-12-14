import pymysql
conn, cur = None, None
data1, data2, data3, data4 = "","","",""
sql=""
conn=pymysql.connect(host = 'localhost',user='root',\
                     db = 'shoppingDB',charset = 'utf8')
cur = conn.cursor()
cur.execute("insert into userTable values('john','John Bann','john@naver.com','1990')")
cur.execute("insert into userTable values('kim','kim mike','kimmike@naver.com','1980')")
cur.execute("insert into userTable values('park','park minseo','park@naver.com','2000')")
conn.commit()
conn.close()