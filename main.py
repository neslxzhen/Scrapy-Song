import re
import urllib.request
import time
from bs4 import BeautifulSoup
from utils.session import Session

html = Session().request("GET", "http://www.chia-anime.me/index/")
print(html)
