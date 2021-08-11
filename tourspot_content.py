from bs4 import BeautifulSoup
import re
import requests



url = "https://www.mcst.go.kr/kor/s_culture/tour/tourList.jsp?pSeq=&pDetailSeq=&pMenuCd=0530000000&pCurrentPage=1&pOrder=&pRegYear=2021&pRegMonth=06&pSido=&pSearchType=CONTS&pSearchWord="

res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")
datas=soup.find_all("div",attrs={"class":"text"})


for data in datas:
    
    data=data.get_text().strip()
    data = data.replace("\n\n","\n")
    print(data)



