import sys # Used to add the BeautifulSoup folder the import path
import urllib # Used to read the html document
from bs4 import BeautifulSoup as BS

### Open page & generate soup
### the "start" variable will be used to iterate through 10 pages.
url = "https://www.linkedin.com/search/results/companies/?keywords=philadelphia%20real%20estate&origin=GLOBAL_SEARCH_HEADER&page=3"
try:
    html = urllib.request.urlopen(url)
except urllib.error.HTTPError as e:
    print(e.code)
except urllib.error.URLError as e:
    print(e.reason)

soup = BS(html,"html.parser")

### Parse and find
### Looks like google contains URLs in <cite> tags.
### So for each cite tag on each page (10), print its contents (url)
for cite in soup.findAll('a'):
    print(cite)