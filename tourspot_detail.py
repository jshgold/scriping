from bs4 import BeautifulSoup
import re
import requests


url="https://www.mcst.go.kr/kor/s_culture/tour/tourView.jsp?pSeq=&pDetailSeq=830&pRegYear=2021&pRegMonth=06&pSearchType=CONTS&pSearchWord=&pCurrentPage=1&pSido=&pOrder="

res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

title = soup.find("div",attrs={"class":"view_title"}).get_text()+"\n"
dep = soup.find("dd",attrs={"class":"full"}).get_text()

con = soup.find("div",attrs={"class":"view_con"}).get_text()
#print(con)
wi=con.replace("\t","")
wich= wi.find("※")
di=wi[0:wich]+"\n"
#print(di)

number= soup.find("p",attrs={"class":"blue pt30"}).find("strong").get_text()
#print(number)

total = title+dep+di+number

print(total)

"""
div view title
dd full
div view_con
p blue pt30.strong

"""



