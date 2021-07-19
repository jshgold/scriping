from selenium import webdriver

import time


browser=webdriver.Chrome()
browser.maximize_window()

url="https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%84%A4%EC%9D%B4%EB%B2%84+%ED%95%AD%EA%B3%B5%EA%B6%8C"
browser.get(url)
time.sleep(2)
browser.find_elements_by_class_name("sp_flight.flight_btn_txt")[0].click()

