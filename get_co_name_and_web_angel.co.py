import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uopen
from urllib.request import Request as rq
import csv

with open('test','w') as new_file:
    test_writer = csv.writer(new_file,delimiter = ",")
    my_url = 'https://www.ycombinator.com/companies/'
#     headers = {'Referer': 'https://angel.co/companies','cookie': '__cfduid=d10abb959d5fe18418fe8ada7d6553e2c1559747762; _angellist=0dc8546c036ab97b4a21eae21b71892a; _ga=GA1.2.1915398304.1559747763; _gid=GA1.2.859251978.1559747763; ajs_user_id=null; ajs_group_id=null; ajs_anonymous_id=%220dc8546c036ab97b4a21eae21b71892a%22; _fbp=fb.1.1559747762941.386114124; intercom-id-og2vxfl5=489f4a10-506e-4f19-b481-b4e65b841970; visitor_hash=637f7a002a65fe26863f12a7efcbe275; amplitude_idundefinedangel.co=eyJvcHRPdXQiOmZhbHNlLCJzZXNzaW9uSWQiOm51bGwsImxhc3RFdmVudFRpbWUiOm51bGwsImV2ZW50SWQiOjAsImlkZW50aWZ5SWQiOjAsInNlcXVlbmNlTnVtYmVyIjowfQ==; ALLA_DATA=%7B%7D; _hp2_ses_props.2978638597=%7B%22ts%22%3A1559779428368%2C%22d%22%3A%22angel.co%22%2C%22h%22%3A%22%2Fdirectory%2Fcompanies%2Fa-1%22%7D; __cf_bm=b352c521665e7599100c297ad600302434c3ee2f-1559781619-1800-Ad8pfohWH3xs6cBrN2/eqrvJ8Ko1WWgOA6RZUy0rgTgAmuqloJ00i2DrxLtgSvuPHq7ILv89xGKYp5qyJak3jtE=; amplitude_id_add5896bb4e577b77205df2195a968f6angel.co=eyJkZXZpY2VJZCI6IjNhNTYyZTcyLWQyNzUtNGNjYS05MjEyLTQzMTUwNDAwNGJmNFIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTU1OTc4MjE1MzI1MCwibGFzdEV2ZW50VGltZSI6MTU1OTc4MjE1MzI1MCwiZXZlbnRJZCI6NSwiaWRlbnRpZnlJZCI6MzYsInNlcXVlbmNlTnVtYmVyIjo0MX0=; _hp2_id.2978638597=%7B%22userId%22%3A%227051792584640884%22%2C%22pageviewId%22%3A%221724141470815463%22%2C%22sessionId%22%3A%227806540102719334%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D',
# 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
#         }
    obreq = rq(my_url, headers={'User-Agent': 'Mozilla/5.0'})
    obClient = uopen(obreq)
    obpage_html = obClient.read()
    obClient.close()
    obpage_soup = bs(obpage_html, "html.parser")
    obcon = obpage_soup.findAll('div',{"class":" dc59 frw44 _a _jm"})
    # req = requests.get(my_url, headers=headers)
    print(obcon[0])
    # page_soup = bs(req.text)
    # # containers = page_soup.findAll('div',{"class":"s-grid-colSm12 u-fontSize14 s-vgPadBottom0_5"})
    # print(page_soup)
    # print(containers[0].a['href'])
    # print(containers[0].a.get_text())