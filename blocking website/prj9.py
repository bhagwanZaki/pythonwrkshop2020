# this program is use to block some website for goven period of time
# so for this we first need to get the current  time
#this can be done by a library of time and datetime
#now() is a function which give current date and time

# import time
# from datetime import datetime as dt

# website_list=['www.google.com','facebook.com','www.facebook.com','google.com']

# host_path="/etc/hosts"      #for windows "C:\windows\System32\drivers\etc\hosts"
# temp=r"hosts"
# redirect="127.0.0.1"       # when the user will try to open the block website he will be redirected here(matlab jab bhi woh website open karega yah pg khulega)

# while True:
#     if dt(dt.now().year,dt.now().month,dt.now().day,8)<dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,16):
#         print("Working Hours",dt.now())                        #if loop is used to write in the hosts to block the website
#         with open (host_path,'r+')as file:                      # with is used to handle the file with no extension
#             content=file.read()                                 #read() will read whole file as whole
#             for website in website_list:
#                 if website in content:
#                     pass
#                 else:
#                     file.write(redirect +" "+website+ "\n")
#     else:
#         with open(host_path,'r+')as file:                           #else is used to delete the content written in  hosts so that website get unblock
#             content=file.readlines()                                   #readlines() is used to write read the file by line by line
#             file.seek(0)
#             for line in content:
#                 if not any(website in line for website in website_list):
#                     file.write(line)
#             file.truncate()
#         print("Non Working hour",dt.now())
#     time.sleep(1)


