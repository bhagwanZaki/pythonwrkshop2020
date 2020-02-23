from bs4 import BeautifulSoup
from requests_html import HTMLSession
import csv

session= HTMLSession()

urls=[]
for i in range(1,51):
    urls.append(f'http://books.toscrape.com/catalogue/page-{i}.html')

csv_file=open('book.csv','w')
csv_writer=csv.writer(csv_file,lineterminator="\n")

csv_writer.writerow(['Title','Price','imageurl'])
count=1
for url in urls:
    source= session.get(url).html.html
    soup=BeautifulSoup(source,'lxml')

    box=soup.find('ol')
    elements=box.find_all('li')
    title=[]
    price=[]
    images=[]

    for element in elements:
        name=element.select('h3 a')[0]['title']
        title.append(name)
        image=element.select('img')[0]['src']
        image_url=r"http://books.toscrape.com/"+image
        images.append(image_url)
        cost=element.find('p', class_='price_color').text
        price.append(cost)
        csv_writer.writerow([name,cost,image_url])
        print(count,end='  ')
        count += 1

csv_file.close()
