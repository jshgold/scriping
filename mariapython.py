import pymysql


conn = None
cur = None

sql=""

conn = pymysql.connect(host="127.0.0.1",user="root",password="1234",db="example",charset="utf8")
cur = conn.cursor()

#sql = "CREATE TABLE IF NOT EXISTS image("\
#    "spot char(30),"\
#    "tourimg longblob,"\
#    "primary key(spot))"
#cur.execute(sql)

sql ="ALTER TABLE image add column dep varchar(100)"
cur.execute(sql)
conn.commit()
conn.close()


