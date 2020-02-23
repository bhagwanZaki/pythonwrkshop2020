from bs4 import BeautifulSoup
from requests_html import HTMLSession
import csv

session= HTMLSession()

urls=[]
for i in range(1,51):
    urls.append(f'https://www.zomato.com/mumbai/order-food-online?utm_source=google&utm_medium=cpc&utm_term=zomato&utm_campaign=Gsearch_P-MWeb_O-NA_C-Brand_A-NewUser_SC-Generic_L-Mumbai&gclid=CjwKCAiA-P7xBRAvEiwAow-VaS6hMYOo6dAcrA_YllyLapjxobUJJEUylq6fBFxNSAbO_68PHEUeuxoCBTYQAvD_BwE&page={i}')

csv_file=open('food.csv','w')
csv_writer=csv.writer(csv_file,lineterminator="\n")


csv_writer.writerow(['Name','Price','Rating','imageurl'])
count=1
for url in urls:
    source= session.get(url).html.html
    soup=BeautifulSoup(source,'lxml')
    box= soup.find(class_='cards')

    elements=box.find_all(class_='card')
    name=[]
    price=[]
    types=[]
    images=[]

    for element in elements:
        title=element.select('a')[0]('title')
        name.append(title)
        
        cost=element.find(class_='grey-text nowrap   ln24 ')
        price.append(cost)

        rate=element.find(class_='rating-popup')
        types.append(rate)

        image=element.find("div",class_='search_left_featured clearfix').div.attrs["style"]
        image_url=r"https://www.zomato.com/"+image
        images.append(image_url)

        csv_writer.writerow([title,cost,rate,image_url])
        print(count,end='  ')
        count += 1

