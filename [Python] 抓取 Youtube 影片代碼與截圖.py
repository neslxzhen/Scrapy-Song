#https://jerrynest.io/python-youtube-hash-img/

import re
import requests
from bs4 import BeautifulSoup

string = "周杰倫";

url = "https://www.youtube.com/results?search_query=" + string
res = requests.get(url, verify=False)
soup = BeautifulSoup(res.text,'html.parser')
last = None

for entry in soup.select('a'):
    m = re.search("v=(.*)",entry['href'])
    if m:
        target = m.group(1)
        if target == last:
            continue
        if re.search("list",target):
            continue
        last = target
        print target