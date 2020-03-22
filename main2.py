import re
import urllib.request
import time
from bs4 import BeautifulSoup
from session import Session
import re
from const import *
from util import *


def get_song(res):
    def func1(r):
        print("func1")
        html_maybe = re.search("(片頭曲「)+.+(」)+",r.text).group(0)
        return BeautifulSoup(html_maybe,'html.parser').text

    def func2(r):
        # is table
        print("func2")
        soup=BeautifulSoup(r.content,'html.parser')
        soup=soup.find(id="主題曲").parent.find_next_sibling()
        return soup

    # op=defense(res,func1,func2)
    op=func2(res)
    print(op)

# main
session=Session()
for line in open(IN_FILE_NAME,"r",encoding="UTF-8"):
    line=line.strip()
    print(line)
    res = session.request("GET", "https://zh.wikipedia.org/wiki/"+line)
    arr= get_song(res)

