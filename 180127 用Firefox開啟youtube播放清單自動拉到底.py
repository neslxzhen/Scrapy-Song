#180127-用Firefox開啟youtube播放清單自動拉到底-----------
from selenium import webdriver
import time,re
from bs4 import BeautifulSoup

d=webdriver.Firefox()
d.implicitly_wait(3)
d.get('https://www.youtube.com/playlist?list=PLO2xQ33wqllDSMWs3CurcY1qf4zmxj2Vq')
for i in range (1,50):
    d.execute_script('window.scrollTo(0,100000000);')
    time.sleep(1)

s=BeautifulSoup(d.page_source)

for b in s.select(".style-scope ytd-playlist-video-renderer"):
    print (b.text)