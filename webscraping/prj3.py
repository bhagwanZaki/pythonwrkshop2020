import requests
from requests_html import HTMLSession
session = HTMLSession()
r =  session.get("https://www.imdb.com/title/tt5311514/?ref_=fn_al_tt_4")

Title=r.html.find('.title_block .title_wrapper h1',first=True)
cast=r.html.find('.cast_list')
print(Title.text)
for i in range(0,len(cast)):
    print(cast[i].text)
poster=r.html.find('.poster a img')
for i in poster:
    print(i.attrs['src'])
rating=r.html.find('.ratingValue strong')
# for i in rating:
#     print(rating[i].text)
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# print(Rating[i].text)

# img= listerlist.find('.posterColumn a img')
# for i in img:
#     print(i.attrs['src'])
    
# print(listerlist)