import re,urllib.parse,urllib.request,urllib.error
from bs4 import BeautifulSoup as BS

baseUrl = 'http://www.bing.com/search?'
word = 'Yapstone+email'
print(word)
word = word.encode(encoding='utf-8', errors='strict')
#print(word)

data = {'q':word}
data = urllib.parse.urlencode(data)
#print(data)
url = baseUrl+data
print(url)

try:
    html = urllib.request.urlopen(url)
except urllib.error.HTTPError as e:
    print(e.code)
except urllib.error.URLError as e:
    print(e.reason)

soup = BS(html,"html.parser")
count = soup.findAll(class_="b_caption")
print(count[0].p.get_text())
