from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

url = "https://play.google.com/store/movies/top"

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

#지정한 위치로 스크롤 내리기
#browser.execute_script('window.scrollTo(0,3080)')

#가장 아래로 스크롤내리기
#browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

interval = 2

prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    time.sleep(interval)

    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        
        break

    prev_height = curr_height

print("스크롤 완료")
soup=BeautifulSoup(browser.page_source,"lxml")

movies = soup.find_all("div",attrs={"class":"Vpfmgd"})
print(len(movies))

#with open("movie.html","w",encoding="utf8") as f:
#    f.write(soup.prettify())

for movie in movies:
    title = movie.find("div",attrs={"class":"WsMG1c nnK0zc"}).get_text()
    


    #할인전 가격 정보
    original_price= movie.find("span",attrs={"class":"SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else:
        #print(title, "< 할인되지 않은 영화 제외>")
        continue


    #할인된 가격 정보
    price = movie.find("span",attrs={"class":"VfPpfd ZdBevf i5DZme"}).get_text()

    link = movie.find("a",attrs={"class":"JC71ub"})["href"]
    print(f"제목:{title}")
    print(f"할인 전 금액: {original_price}")
    print(f"할인 후 금액: {price}")
    print("링크: https://play.google.com"+link)
    print('-'*120)
browser.quit()





    
