import requests


"downloading with requests"
for i in range(10,26):
    stri = str(i)
    url = 'http://staff.ustc.edu.cn/~zhaojin/courseware/chap{}.pdf'.format(i)
    r = requests.get(url)
    with open("chap{}.pdf".format(i), "wb") as code:
        code.write(r.content)