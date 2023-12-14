import csv
import pymysql

conn=pymysql.connect(host = 'localhost',user='root',\
                     db = 'shoppingDB',charset = 'utf8')

cur = conn.cursor()

f = open(r'/Users/choejong-gyu/Documents/04.데이터베이스/data/data.csv','r',encoding='CP949')



csvReader = list(csv.reader(f))

cur.execute("CREATE TABLE IF NOT EXISTS person( char(10),sex char(1),class char(1), attend char(1))")



for data in csvReader[1:]:
    row1 = data[0]
    row2 = data[1]
    row3 = data[2]
    row4 = data[3]
    
    sql = """insert into person (name,sex,class,attend) values(%s,%s,%s,%s);"""
    cur.execute(sql, (row1,row2,row3,row4))


f.close()
conn.commit()
conn.close()


