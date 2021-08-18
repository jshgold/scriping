from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import pymysql
import time
import re

lst=[]
con = pymysql.connect(host="127.0.0.1",user="root",password="1234",db="site",charset="utf8")
cur=con.cursor()
sql = "SELECT spot FROM datas"
cur.execute(sql)
while(True):
    row=cur.fetchone()
    if row==None:
        break
    lst.append(row[0])
    

for year in range(2010,2022):
    for month in range(1,13):
        month=str(month)
        if len(month)==1:
            month="0"+month
        url="https://www.mcst.go.kr/kor/s_culture/tour/tourList.jsp?pSeq=&pDetailSeq=&pMenuCd=0530000000&pCurrentPage=1&pOrder=&pRegYear={year}&pRegMonth={month}&pSido=&pSearchType=TITLE&pSearchWord=".format(year=year,month=month)
        res= requests.get(url)
        res.raise_for_status()
        soup=BeautifulSoup(res.text,"lxml")
        page_count=len(soup.find("div",attrs={"class":"paging m"}).find_all("a"))
        
        
        for page in range(page_count):
            page+=1
            url="https://www.mcst.go.kr/kor/s_culture/tour/tourList.jsp?pSeq=&pDetailSeq=&pMenuCd=0530000000&pCurrentPage={page}&pOrder=&pRegYear={year}&pRegMonth={month}&pSido=&pSearchType=TITLE&pSearchWord=".format(page=page,year=year,month=month)
            res=requests.get(url)
            res.raise_for_status()
            soup=BeautifulSoup(res.text,"lxml")
            tourlist_count=int(len(soup.find("ul",attrs={"class":"mediaWrap"}).find_all("li"))/2)
            for count in range(tourlist_count):
            
                options = webdriver.ChromeOptions()
                options.headless=True
                options.add_argument("window-size=1920x1080")
                options.add_argument("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36")
                browser = webdriver.Chrome(options=options)
                browser.get(url)
                browser.find_elements_by_class_name("go")[count].click()
                time.sleep(1)
                title=browser.find_element_by_class_name("view_title").text.strip()
                if title in lst:
                    continue
                dep = browser.find_element_by_class_name("full").text.strip()
                content = browser.find_element_by_class_name("view_con").text.strip()
                if content.find("※") != -1:
                    wich = content.find("※")
                    print(wich)
                elif content.find("문의") != -1:
                    wich = content.find("문의")
                    print(wich)
                content = content[:wich]
                tourimg = browser.find_element_by_css_selector("#content > div.contentWrap > div.viewWarp > div.culture_view_img > img").get_attribute("src")

                

                sql = "INSERT INTO datas (spot,cont,tourimg,dep)"\
                    "values(%s,%s,%s,%s)"
                
                cur.execute(sql,(title,content,tourimg,dep))
                con.commit()
            
            browser.quit()










        
        








        #url="https://www.mcst.go.kr/kor/s_culture/tour/tourList.jsp?pSeq=&pDetailSeq=&pMenuCd=0530000000&pCurrentPage={page}&pOrder=&pRegYear={year}&pRegMonth={month}&pSido=&pSearchType=TITLE&pSearchWord=".format(page=page,year=year,month=month)