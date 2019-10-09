from bs4 import BeautifulSoup
import requests
import requests.exceptions
from urllib.parse import urlsplit
from collections import deque
import re
import csv
import glob
import os

os.chdir("C:/data")

with open('list.csv','w') as new_file:
    test_writer = csv.writer(new_file, delimiter=",")
    bigset = []
    for i in range(1,16):
        path = "C:/Users/ljhgo/Documents/laogong/internship2019summer/p"+str(i)+'.html'
        htmlfile = open(path, 'r', encoding='utf-8')
        htmlhandle = htmlfile.read()
        soup = BeautifulSoup(htmlhandle, "html.parser")
        contents = soup.findAll('div', {"class": "VkpGBb"})
        for content in contents:
            try:
                name = content.findAll('div',{"class":"dbg0pd"})[0].div.text
                web = content.findAll('a',{"class":"yYlJEf L48Cpd"})[0]['href']
                addresses = content.findAll('a',{"style":"cursor:pointer"})[0]['data-url'].split('/')[4].split(',')
                street = (addresses[-3]+', ' +addresses[-2]+', ' +addresses[-1]).replace('+',' ').replace('%2', '#')
                phone = ''
                try:
                    phone = re.findall(r"[\.\- ()+]*\d\d\d[\.\- ()]*\d\d\d[\.\- ()]?\d\d\d\d", content.text)[0]
                except:
                    pass
                listhere = [name, web, street, phone]
                test_writer.writerow(listhere)
            except:
                continue

                # if name is not None and web is not None:
                #     print(name)
                #     test_writer.writerow([name , web])
            # except:
            #     continue
    # test_writer = csv.writer(new_file,delimiter = ",")
    #
    # contents = soup.findAll('div',{"class":"dc59 frw44 _a _jm"})
    # for content in contents:
    #     try:
    #         name = content.findAll('a',{"class":"startup-link"})[0]['title']
    #         web = content.findAll('div',{"class":"website"})[0].a['href']
    #         if name is not None and web is not None:
    #             print(name)
    #             test_writer.writerow([name , web])
    #     except:
    #         continue
    # print(len(contents))


