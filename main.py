import time
from bs4 import BeautifulSoup
from selenium import webdriver
import re

#參數調整---------------------------------------------------------------
format="mp4" #下載格式
fileName="test.txt"

#------------------------------------------------------------
browser=webdriver.Chrome()
browser.implicitly_wait(1)

urls=[]
vedioTitles=[]
songTitles=[]
songTitles=[]
myTitles=[]

#開啟檔案讀取歌名--------------------------------------------------
for myTitle in open(fileName,"r",encoding="UTF-8"):
    myTitle=myTitle.strip()
    myTitles.append(myTitle)
    browser.get("https://zh.wikipedia.org/wiki/Wikipedia:%E9%A6%96%E9%A1%B5") #換網頁

    browser.find_element_by_id("searchInput").send_keys(myTitle+" 動畫")
    browser.find_element_by_id("searchButton").click()
    browser.implicitly_wait(1) #換網頁

    x=BeautifulSoup(browser.page_source,"html.parser").find("div","mw-search-result-heading")
    print (x.find("a").get("string")) #get要用在前後都有包起來並且最底層的情況下才抓的到
    browser.get("https://zh.wikipedia.org"+x.find("a").get("href")) #換網頁
    soup=BeautifulSoup(browser.page_source,"html.parser") #到這邊已不會再改變網頁，所以我寫死

    try:
        songTitles.append(soup.find("dt", string=re.compile("\u7247\u982d\u66f2\u300c+")).string)
        #用正規表達式搜尋 ^()=開頭為... u7247=unicode"片" u982d="頭" u5c3e=尾 u66f2=曲 u300c=「
        #string=抓其中的字串，跟get()不同
    except:
        print(myTitle+"-OP出現例外")
        print(soup.find("dt", string=re.compile("\u7247\u982d\u66f2+")))
        x=soup.find("dt", string=re.compile("\u7247\u982d\u66f2+")).parent.contents#列出其父親的所有子孫
        print(x)

        songTitles.append(None)
    try:
        songTitles.append(soup.find("dt", string=re.compile("\u7247\u5c3e\u66f2\u300c+")).string)
    except:
        songTitles.append(None)
        print(myTitle+"-ED出現例外")

    print(songTitles)
print(songTitles)
browser.close()
