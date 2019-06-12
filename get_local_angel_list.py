from bs4 import BeautifulSoup
import requests
import requests.exceptions
from urllib.parse import urlsplit
from collections import deque
import re
import csv

path = 'F:/2019 intern/week 1/AngelList_software.html'
adj = path.split("/")[-1]

with open('company_name_web_'+adj+'.csv','w') as new_file:
    test_writer = csv.writer(new_file,delimiter = ",")
    htmlfile = open(path, 'r', encoding='utf-8')
    htmlhandle = htmlfile.read()
    soup = BeautifulSoup(htmlhandle,"html.parser")
    contents = soup.findAll('div',{"class":"dc59 frw44 _a _jm"})
    for content in contents:
        try:
            name = content.findAll('a',{"class":"startup-link"})[0]['title']
            web = content.findAll('div',{"class":"website"})[0].a['href']
            if name is not None and web is not None:
                print(name)
                test_writer.writerow([name , web])
        except:
            continue
    print(len(contents))


