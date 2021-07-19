from selenium import webdriver
import time


browser = webdriver.Chrome()
browser.maximize_window()
url="https://beta-flight.naver.com/"
browser.get(url)

browser.find_elements_by_class_name("searchBox_option__2CEVQ.select_Date__1aF7Y")[0].click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[3]/button/b').click()
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[4]/td[4]/button/b').click()

browser.find_elements_by_class_name("select_code__d6PLz")[1].click()
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[10]/div[1]/div/input').send_keys("제주")
time.sleep(1)
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[10]/div[2]/section/div/a/div[1]/i[1]').click()



