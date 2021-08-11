#from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import re
import time

#count=0
#url ="https://www.mcst.go.kr/kor/s_culture/tour/tourList.jsp?pSeq=&pDetailSeq=&pMenuCd=0530000000&pCurrentPage=1&pOrder=&pRegYear=2021&pRegMonth=01&pSido=&pSearchType=TITLE&pSearchWord="
#
#res = requests.get(url)
#res.raise_for_status()
#
#soup = BeautifulSoup(res.text,'lxml')
#
#numbers = soup.find("div",attrs={"class":"paging m"})
#print(numbers)
#if numbers != None:
#    numbers=numbers.get_text()
#    
#    for number in numbers:
#        if re.search(r'[0-9]',number):
#            count+=1
#    print(count)


#lst=[]
#for i in range(5):
#    num=i+1
#
#    url="https://www.mcst.go.kr/kor/s_culture/tour/tourList.jsp?pCurrentPage={}&pRegYear=2021&pRegMonth=06&pSearchType=&pSearchWord=&pSeq=&pDetailSeq=&pOrder=&pSido=&pMCurrentPage=".format(num)
#
#    res = requests.get(url)
#    res.raise_for_status()
#    soup = BeautifulSoup(res.text,'lxml')
#
#    tourlists = soup.find("ul",attrs={"class":"mediaWrap"}).find_all("img")
#
#    print(tourlists)
#
#    for tourlist in tourlists:
#        image_url = tourlist['src']
#        tourlist_name = tourlist['alt']
#        if tourlist_name not in lst:
#            lst.append(tourlist_name)
#            print(tourlist_name)
#
#            if image_url.startswith("/"):
#                image_url = "https://www.mcst.go.kr"+image_url
#
#
#            image_res = requests.get(image_url)
#            image_res.raise_for_status()
#
#            with open("{}.jpg".format(tourlist_name),"wb") as f:
#                f.write(image_res.content)
    

    
lst=[]
for ye in range(2010,2022):
    for mo in range(1,13):
        counts=0
        mo=str(mo)
        if len(mo)==1:
            mo='0'+mo
            print(mo)
        url ="https://www.mcst.go.kr/kor/s_culture/tour/tourList.jsp?pSeq=&pDetailSeq=&pMenuCd=0530000000&pCurrentPage=1&pOrder=&pRegYear={year}&pRegMonth={month}&pSido=&pSearchType=TITLE&pSearchWord=".format(year=ye,month=mo)
        time.sleep(2)
        res = requests.get(url)
        res.raise_for_status()

        soup = BeautifulSoup(res.text,'lxml')

        numbers = soup.find("div",attrs={"class":"paging m"})
        if numbers != None:
            numbers=numbers.get_text()
            for number in numbers:
                if re.search(r'[0-9]',number):
                    counts+=1
        
        for count in range(counts):
            pa = count+1
            url = "https://www.mcst.go.kr/kor/s_culture/tour/tourList.jsp?pSeq=&pDetailSeq=&pMenuCd=0530000000&pCurrentPage={page}&pOrder=&pRegYear={year}&pRegMonth={month}&pSido=&pSearchType=TITLE&pSearchWord=".format(year=ye,month=mo,page=pa)
            res = requests.get(url)
            res.raise_for_status()
            soup = BeautifulSoup(res.text,'lxml')

            tourlists = soup.find("ul",attrs={"class":"mediaWrap"}).find_all("img")

            print(tourlists)

            for tourlist in tourlists:
                image_url = tourlist['src']
                tourlist_name = tourlist['alt']
                if tourlist_name not in lst:
                    lst.append(tourlist_name)
                    print(tourlist_name)

                    if image_url.startswith("/"):
                        image_url = "https://www.mcst.go.kr"+image_url


                    image_res = requests.get(image_url)
                    image_res.raise_for_status()

                    with open("tourspots/{}_{}_{}.jpg".format(ye,mo,tourlist_name),"wb") as f:
                        f.write(image_res.content)

        
            