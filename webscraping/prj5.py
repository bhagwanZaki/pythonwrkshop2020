from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession
session = HTMLSession()


# r=session.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")

# listerlist=r.html.find('.lister',first=True)
# title=listerlist.find('.titleColumn a')
# data=listerlist.text
# soup=BeautifulSoup(data,'lxml')
# for i in range(0,len(title)):
#     print(soup.prettify())

# in above program requests is used and we have to go in list and then in title but by using bs4 we can directly go to titleColumn rather then first declarin lister


# url="https://www.imdb.com/chart/top/?ref_=nv_mv_250" 
# response=requests.get(url)
# data=response.text
# soup=BeautifulSoup(data,'lxml')
# title=soup.find_all(class_='titleColumn')
# for i in title:
#     print(i.get_text())

# using bs4 you can also scrape many website at instant 
# urls=[]
# for i in range(1,51):
#         urls.append('http://books.toscrape.com/catalogue/page-9.html')
# for i in urls:
#     print(urls)


# urls=[]
# for i in range(1,51):
#         urls.append(f'http://books.toscrape.com/catalogue/page-{i}.html')
# for i in urls:
#     print(urls)

y=int(input("enter the start page"))
z=int(input("enter the last page"))
for i in range(y,z+1):
    url = "https://www.freepik.com/search?dates=any&format=search&page={}&query=wallpaper&selection=1&sort=popular&type=vector".format(i)
    print(url)
    response=requests.get(url)
    data=response.text
    soup=BeautifulSoup(data,'lxml')
    print(soup.prettify)
    

#the above 3 method mean the same