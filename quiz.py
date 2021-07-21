import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time


url="https://new.land.naver.com/complexes/125354?ms=37.48653,127.155095,17&a=APT:ABYG:JGC&b=B1&e=RETAIL"

#browser = webdriver.Chrome()
#browser.maximize_window()
#browser.get(url)
#
#browser.find_element_by_class_name("tf_keyword").send_keys("송파 헬리오시티\n")
#time.sleep(2)
#browser.find_element_by_xpath('//*[@id="estateColl"]/div[2]/div/div[2]/div[1]/a').click()
#
#time.sleep(6)
#
#browser.find_element_by_class_name("rn-obd0qt rn-1efd50x rn-14skgim rn-rull8r rn-mm0ijv rn-13yce4e rn-fnigne rn-ndvcnb rn-gxnn5r rn-deolkf rn-6koalj rn-16y2uox rn-1wbh5a2 rn-1ro0kt6 rn-18u37iz rn-1w6e6rj rn-1mnahxq rn-61z16t rn-p1pxzi rn-11wrixw rn-ifefl9 rn-bcqeeo rn-wk8lta rn-9aemit rn-1mdbw0j rn-gy4na3 rn-bnwqim rn-13qz1uu rn-1lgpqti").click()
#

headers ={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36",
    "Accept-Language":"ko-KR,ko"
    }

res= requests.get(url,headers=headers)
res.raise_for_status()
soup=BeautifulSoup(res.text,"lxml")

budongs=soup.find("div",attrs={"class":"item_area"})
print(len(budongs))

