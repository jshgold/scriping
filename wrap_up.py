import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time

url="https://www.naver.com/"
browser= webdriver.Chrome()
browser.maximize_window()
browser.get(url)

browser.find_element_by_id("query").send_keys("송파 헬리오시티\n")

browser.execute_script("window.scrollTo(0,1500)")
time.sleep(2)
browser.find_element_by_class_name("more_icon_inner").click()
time.sleep(2)
elem=browser.find_elements_by_class_name("text")

for e in elem:
    print(e.text)



    




