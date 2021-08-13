from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import pymysql

con=None
cur=None
sql=""

con = pymysql.connect(host="127.0.0.1",user="root",password="1234",db="example",charset="utf8")
cur=con.cursor()
url="https://www.mcst.go.kr/kor/s_culture/tour/tourList.jsp?pSeq=&pDetailSeq=&pMenuCd=0530000000&pCurrentPage=1&pOrder=&pRegYear=2021&pRegMonth=06&pSido=&pSearchType=TITLE&pSearchWord="
options = webdriver.ChromeOptions()
options.headless=True
options.add_argument("window-size=1920x1080")
options.add_argument("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36")
browser=webdriver.Chrome(options=options)
browser.get(url)
counts =len(browser.find_elements_by_class_name("go"))
browser.quit()


for count in range(counts):
    url="https://www.mcst.go.kr/kor/s_culture/tour/tourList.jsp?pSeq=&pDetailSeq=&pMenuCd=0530000000&pCurrentPage=1&pOrder=&pRegYear=2021&pRegMonth=06&pSido=&pSearchType=TITLE&pSearchWord="
    options = webdriver.ChromeOptions()
    options.headless=True
    options.add_argument("window-size=1920x1080")
    options.add_argument("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36")
    browser=webdriver.Chrome(options=options)
    browser.get(url)
    browser.find_elements_by_class_name("go")[count].click()
    time.sleep(1)
    title = browser.find_element_by_class_name("view_title").text.strip()
    image = browser.find_element_by_css_selector("#content > div.contentWrap > div.viewWarp > div.culture_view_img > img").get_attribute("src")
    
    print("링크 : "+image)
    content = browser.find_element_by_class_name("view_con").text
    spot = content.find("※")
    content = content[0:spot].strip()
    
    sql="INSERT INTO image (spot,content,tourimg)"\
        "values (%s,%s,%s)"
    cur.execute(sql,(title,content,image))
    con.commit()

browser.quit()

