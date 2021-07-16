import requests
from bs4 import BeautifulSoup

idx=0
limit=4
for year in range(2015,2020):
    url="https://search.daum.net/search?w=tot&q="+str(year)+"%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
    res=requests.get(url)
    res.raise_for_status()
    soup=BeautifulSoup(res.text,"lxml")
    images=soup.find_all("img",attrs={"class":"thumb_img"})
    for image in images:
        if idx>limit:
            break
        image_url = image["src"]
        if image_url.startswith("//"):
            image_url="https:"+image_url

        print(image_url)
        image_res = requests.get(image_url)
        image_res.raise_for_status()

        with open("movie{}.jpg".format(idx+1),"wb") as f:
            f.write(image_res.content)
        idx+=1
    limit+=5
  
        
