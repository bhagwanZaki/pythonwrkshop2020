# web scrapping means you are taking the source code of it and it is done by requests library
# to download requests library 
# pip install requests in terminal

# get(website_url) this will tell the website that you r acessing it
# and if you print text then you will get its source code whivh is illegal
#for security purpose the website encode it data in 8 or 16 bit means word a is encoded in 8bit so to check its unicode transformation format(UTF)
# to know the utf 'encoding' keyword is used
# is website allowing u or not to check it 'status_code' is used
# tO CHECK HOW FAST A WEBSITE opens elapsed keyword is used

 #a= requests.get()
    # print(a.encoding)
    # print(a.status_code)
    # # print(a.elapsed)
    # print(a.url)    


# 
# print(a.encoding)
# print(a.status_code)
# print(a.elapsed)
# print(a.url)

import requests
# x=int(input("enter th

a=requests.get("https://www.imdb.com/title/tt5311514/")
    # print(a.encoding)
    # print(a.status_code)
    # print(a.elapsed)
    # print(a.url)
print(a.text[0:1000])