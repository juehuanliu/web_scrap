
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uopen
from urllib.request import Request as rq
import csv


with open('test','w') as new_file:
    test_writer = csv.writer(new_file,delimiter = ",")

    my_url = 'https://www.amazon.com/'
    req = rq(my_url, headers = {'User-Agent':'Mozilla/5.0'})
    uClient = uopen(req)
    page_html = uClient.read()
    uClient.close()
    page_soup = bs(page_html, "html.parser")
    containers = page_soup.findAll('div')
    print(containers)


