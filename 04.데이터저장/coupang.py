import csv
import pymysql

conn,cur =None, None

conn = pymysql.connect(host='localhost', user='root', db='shoppingDB', charset='utf8')
cur = conn.cursor()

f = open(r'/Users/choejong-gyu/Downloads/임시쿠팡파일.csv', 'r',encoding='euckr')
csvReader = list(csv.reader(f))

cur.execute("""
    CREATE TABLE IF NOT EXISTS coupang (
        name VARCHAR(255),
        price VARCHAR(255),
        rate VARCHAR(255),
        url VARCHAR(255),
        filename VARCHAR(255)
    );
""")


for data in csvReader[1:]:
    row1 = data[1]
    row2 = data[2]
    row3 = data[3]
    row4 = data[4]
    row5 = data[5]

    sql = """INSERT INTO coupang (name, price, rate, url, filename) VALUES(%s, %s, %s, %s, %s);"""
    cur.execute(sql, (row1, row2, row3, row4, row5))

f.close()
cur.close()
conn.commit()
conn.close()