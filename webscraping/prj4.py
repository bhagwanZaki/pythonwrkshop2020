import requests
from requests_html import HTMLSession,HTML,HTMLResponse
import csv
session = HTMLSession()
r =  session.get("https://www.imdb.com/movies-in-theaters/")
listerlist=r.html.find('.sub-list',first=True)
title=listerlist.find('.overview-top    ')
genre=listerlist.find('.cert-runtime-genre span')
plot=listerlist.find('.outline')
director=listerlist.find('.txt-block')
actor=listerlist.find('.txt-block')
rating=listerlist.find('.rating_txt')
count=0

for i in range(0,len(title)):
    print(title[i].text)
    print(genre[i].text)
    print(plot[i].text)
    print(director[i].text)
    print(actor[i].text)
    print(rating[i].text)
    print()
    

# csv_file=open('movies.csv','w')
# csv_writer= csv.writer(csv_file,lineterminator='\n')


# csv_writer.writerow(['TITLE','PLOT','RUNTIME'])
# title=[]
# plot=[]
# runtime=[]
# count=1

















