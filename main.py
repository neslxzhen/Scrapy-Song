import re
import urllib.request
import time
from bs4 import BeautifulSoup

#參數調整---------------------------------------------------------------
from selenium import webdriver

format="mp4" #下載格式
fileName="test.txt"

urls=[]
vedioTitles=[]
songTitles=[]
myTitles=[]

#開啟檔案讀取動畫名稱，使用wiki搜尋後取得OP.ED--------------------------------------------------
print("取得OP.ED...")
browser=webdriver.Chrome()
browser.implicitly_wait(1)

c=0
browser.get("https://zh.wikipedia.org/wiki/Wikipedia:%E9%A6%96%E9%A1%B5") #換網頁
for myTitle in open(fileName,"r",encoding="UTF-8"):
    print(c)
    myTitle=myTitle.strip()
    myTitles.append(myTitle)

    #搜尋
    browser.find_element_by_id("searchInput").send_keys(myTitle+" 動畫")
    browser.find_element_by_id("searchButton").click() #換網頁
    browser.implicitly_wait(1)

    #抓第一個
    x=BeautifulSoup(browser.page_source,"html.parser").find("div","mw-search-result-heading")
    a="https://zh.wikipedia.org"+x.find("a").get("href")
    code=urllib.request.urlopen(a).read() #抓取HTML
    browser.get(a) #換網頁
    browser.implicitly_wait(1)

    #將HTML轉字串
    codeStr=str(code,'utf-8') #使用utf-8閱讀字串

    #尋找歌名
    i=""
    j1=0
    j2=0
    i=codeStr[codeStr.find("片頭曲「"):]
    line=(i[:i.find("」")+1])
    while(line.find("<")>0):
        j1=line.find("<")
        j2=line.find(">")
        line=line[:j1]+line[j2+1:]
    print (line)
    if line !="":
        songTitles.append(line)
    else:
        songTitles.append(None)

    i=codeStr[codeStr.find("片尾曲「"):]
    line=(i[:i.find("」")+1])
    while(line.find("<")>0):
        j1=line.find("<")
        j2=line.find(">")
        line=line[:j1]+line[j2+1:]
    print (line)
    if line !="":
        songTitles.append(line)
    else:
        songTitles.append(None)
    c=c+1
print("已取得OP.ED")
print(songTitles)

#將歌名另存--------------------------------------------------------
print("將歌名另存...")
with open("songTitle.txt","w",encoding="UTF-8") as f:
    i=0
    j=0
    for line in songTitles:
        try:
            f.write(myTitles[j]+','+line+'\n') #line不是int
        except:
            f.write(myTitles[j]+','+"None\n")
        i=i+1
        if i%2==0:j=j+1
print("已將歌名另存")

#將歌名寫入--------------------------------------------------------
print("將歌名寫入...")
songTitles.clear()
for songTitle in open("songTitle.txt","r",encoding="UTF-8"):
    songTitle=songTitle.strip()
    list=songTitle.split(",")
    songTitles.append(list[1])
print("已將歌名寫入")
print(songTitles)

#搜尋YT------------------------------------------------------------------------
for songTitle in songTitles:
    if songTitle!="None":
        browser.get('https://www.youtube.com/results?search_query='+songTitle+"+OP")
        soup=BeautifulSoup(browser.page_source, "html.parser")
        browser.implicitly_wait(0) # 暗示(隱式等待)

        x=soup.find('a','yt-simple-endpoint style-scope ytd-video-renderer') # 找尋第一個 a 區塊且 class="yt-simple-endpoint style-scope ytd-video-renderer"
        vedioTitle=x.get('title')
        href = x.get('href')
        urls.append("https://www.youtube.com"+href)
        vedioTitles.append(vedioTitle)
    else:
        urls.append("None")
        vedioTitles.append("None")
print (urls)
print ('-'*100)

#urls=['https://www.youtube.com/watch?v=PqY8dcRZ06k', 'https://www.youtube.com/watch?v=OYwcXfAYAbg', 'https://www.youtube.com/watch?v=FAOnsPouYGE', 'https://www.youtube.com/watch?v=nrGB04GIePQ', 'https://www.youtube.com/watch?v=xkMdLcB_vNU', 'https://www.youtube.com/watch?v=yi0428jRI9U', 'https://www.youtube.com/watch?v=F9kqColvQhA', 'https://www.youtube.com/watch?v=kLAZja_0cCs', 'https://www.youtube.com/watch?v=8aZ_hMX87eo', 'https://www.youtube.com/watch?v=evwO4B8nxsU', 'https://www.youtube.com/watch?v=CicnGW43Ukw', 'https://www.youtube.com/watch?v=09yPyy9eldI', 'https://www.youtube.com/watch?v=Cp89qis1ddo', 'https://www.youtube.com/watch?v=nHztuf7NRiU', 'https://www.youtube.com/watch?v=0V6mb19viaw', 'https://www.youtube.com/watch?v=BHtgSerQvSI', 'https://www.youtube.com/watch?v=oxxKm_O1xwo', 'https://www.youtube.com/watch?v=gbj_v67IrB4', 'https://www.youtube.com/watch?v=zuoER3g-FTg', 'https://www.youtube.com/watch?v=07XFP6BhGac', 'https://www.youtube.com/watch?v=OC8oadcsPxw', 'https://www.youtube.com/watch?v=_4sEQYAaMhM']

#將url另存--------------------------------------------------------------------
with open('urlFile.txt','w',encoding='UTF-8') as f:
    i=0
    j=0
    for line in urls:
        if urls[i]!="None":
            f.write(myTitles[j]+","+line+','+vedioTitles[i]+'\n') #line不是int
        i=i+1
        if i%2==0:j=j+1

#將url寫入--------------------------------------------------------
urls=urls.clear()
urls=[]
for url in open("urlFile.txt","r",encoding="UTF-8"):
    url=url.strip()
    list=url.split(",")
    urls.append(list[1])

#下載----------------------------------------------------------------------------
i2=0
for url in urls:
    browser.get('https://ytmp3.cc/')
    print ('載入https://ytmp3.cc/')

    i=0
    while (i==0):
        print ('進入網站檢查迴圈:'+myTitles[i2])
        time.sleep(5)
        try:
            print ('尋找關鍵')
            print (browser.find_element_by_id("title"))
            i=1
        except:
            print ('重新整理')
            browser.refresh() #重新整理

    print ('輸入url'+url)
    browser.find_element_by_id('input').send_keys(url)
    browser.find_element_by_id("mp4").click()
    browser.find_element_by_id('submit').click()

    #判斷download按鈕存在與否
    i1=0
    while (i1==0):
        print ('進入檢查download鈕迴圈:')
        try:
            print ('尋找download')
            browser.find_element_by_id("download").click()
            print ('存在並點擊')
            i1=1
        except:
            print ('不存在')

    i2=i2+1
