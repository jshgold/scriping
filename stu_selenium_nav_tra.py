from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome()
browser.maximize_window()
url="https://flight.naver.com/flights/"
browser.get(url)


browser.find_element_by_link_text("가는날 선택").click()

#날짜선택
time.sleep(1)
browser.find_elements_by_link_text("27")[0].click()
browser.find_elements_by_link_text("28")[1].click()

#제주설정
browser.find_element_by_xpath('//*[@id="recommendationList"]/ul/li[1]/div/span').click()

#검색
browser.find_element_by_link_text("항공권 검색").click()

#첫번째 결과 출력
try:
    elem = WebDriverWait(browser,10).until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="content"]/div[2]/div/div[4]/ul')))
    for e in elem:
        print(e.text)

finally:
    browser.quit()

