
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uopen
from urllib.request import Request as rq
import csv


with open('test','w') as new_file:
    test_writer = csv.writer(new_file,delimiter = ",")

    my_url = 'https://pokemondb.net/pokedex/national'
    req = rq(my_url, headers = {'User-Agent':'Mozilla/5.0'})
    uClient = uopen(req)
    page_html = uClient.read()
    uClient.close()
    page_soup = bs(page_html, "html.parser")
    containers = page_soup.findAll('div',{"class":"infocard-list infocard-list-pkmn-lg"})
    cont_g1 = containers[0]
    ob_1 = cont_g1.findAll('div',{"class":"infocard"})
    for ob in ob_1:
        ob_name = ob.a['href'].split("/")[2]
        ob_url = 'https://pokemondb.net/pokedex/'+ ob_name
        obreq = rq(ob_url, headers={'User-Agent': 'Mozilla/5.0'})
        obClient = uopen(obreq)
        obpage_html = obClient.read()
        obClient.close()
        obpage_soup = bs(obpage_html, "html.parser")
        obcon = obpage_soup.findAll('table',{"class":"vitals-table"})
        obtab = obcon[0].findAll('tr')
        for line in obtab:
            if line.th.get_text() == 'Weight':
                weight = line.td.get_text().encode('ascii', 'ignore').decode('ascii', 'ignore')
            elif line.th.get_text() == 'Height':
                height = line.td.get_text().encode('ascii', 'ignore').decode('ascii', 'ignore')
        print([ob_name,weight,height])
        test_writer.writerow([ob_name,weight,height])