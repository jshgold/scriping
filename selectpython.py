import pymysql

#lst=[]
#con=pymysql.connect(host="127.0.0.1",user="root",password="1234",db="site",charset="utf8")
#cur=con.cursor()
#sql="SELECT spot FROM datas"
#cur.execute(sql)
#while(True):
#    row = cur.fetchone()
#    if row == None:
#        break
#    lst.append(row[0])
#print(lst)


juso=[]

con = pymysql.connect(host="127.0.0.1",user="root",password="1234",db="site",charset="utf8")
cur = con.cursor()
sql = "SELECT dep FROM datas"
cur.execute(sql)
while(True):
    row=cur.fetchone()
    if row==None:
        break
    row=row[0]
    space=row.find(" ")
    if row.startswith("충북"):
        row=row.replace(row[:space],"충청북도")
        space=row.find(" ")
    elif row.startswith("충남"):
        row=row.replace(row[:space],"충청남도")
        space=row.find(" ")
    elif row.startswith("경북"):
        row=row.replace(row[:space],"경상북도")
        space=row.find(" ")
    elif row.startswith("경남"):
        row=row.replace(row[:space],"경상남도")
        space=row.find(" ")
    elif row.startswith("전북"):
        row=row.replace(row[:space],"전라북도")
        space=row.find(" ")
    elif row.startswith("전남"):
        row=row.replace(row[:space],"전라남도")
        space=row.find(" ")

    if row[:space] not in juso:
        juso.append(row[:space])

print(juso)



    

