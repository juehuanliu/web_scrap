from bs4 import BeautifulSoup
import requests
import requests.exceptions
from urllib.parse import urlsplit
from collections import deque
import re
import csv

path = 'f:/PycharmProjects/web scrape/tech/cleaned_tech.csv.csv'
start_at = -1
with open(path,'r') as name_file:
    name_reader = csv.reader(name_file,delimiter = ",")
    with open('tech.csv', 'a', newline='') as new_file:
        test_writer = csv.writer(new_file, delimiter="\t")
        count_test = -1
        for readlines in name_reader:
            count_test += 1
            print(count_test)
            if count_test < start_at:
                continue
                        # a queue of urls to be crawled
            try:
                new_urls = deque([readlines[1]])
            except:
                continue

            # a set of urls that we have already crawled
            processed_urls = set()

            # a set of crawled emails
            emails = set()
            phones = set()
            count = 0

            # process urls one by one until we exhaust the queue
            while len(new_urls) and count < 20:
                # move next url from the queue to the set of processed urls
                url = new_urls.popleft()
                processed_urls.add(url)

                # extract base url to resolve relative links
                parts = urlsplit(url)
                base_url = "{0.scheme}://{0.netloc}".format(parts)
                path = url[:url.rfind('/')+1] if '/' in parts.path else url

                # get url's content
                try:
                    response = requests.get(url)
                    count += 1
                except:
                    continue

                # extract all email addresses and add them into the resulting set
                try:
                    new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.(?:com|net|cn|us|edu|gov|cc|org)", response.text, re.I))
                    new_phones = set(re.findall(r"\s1?[\.\- ()+]*\d\d\d[\.\- ()]?\d\d\d[\.\- ()]?\d\d\d\d", response.text))
                except:
                    continue
                emails.update(new_emails)
                phones.update(new_phones)

                # create a beutiful soup for the html document
                soup = BeautifulSoup(response.text)

                # find and process all the anchors in the document
                if len(new_urls) > (20 - count):
                    continue
                for anchor in soup.find_all("a"):
                    # extract link url from the anchor
                    link = anchor.attrs["href"] if "href" in anchor.attrs else ''
                    # resolve relative links
                    if link.startswith('/'):
                        link = base_url + link
                    elif not link.startswith('http'):
                        link = path + link
                    # add the new url to the queue if it was not enqueued nor processed yet
                    if not link in new_urls and not link in processed_urls:
                        new_urls.append(link)
            emls =''
            for em in emails:
                if str(em).__contains__('example'):
                    continue
                if str(em).__contains__('name'):
                    continue
                emls += (str(em)+', ')
            try:
                emls = emls[:len(emls)-2]
            except:
                pass
            phone = ''
            for ph in phones:
                phone += (str(ph).strip()+', ')
            try:
                phone = phone[:len(phone)-2]
            except:
                pass

            if emls != '' or phone != '':
                test_writer.writerow([readlines[0],'finance',readlines[1],emls,phone] )
                new_file.flush()
                print(count_test,[readlines[0],'finance',readlines[1],emls,phone])

