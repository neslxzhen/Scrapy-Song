#-------------------------------------------------
from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver=webdriver.Chrome()
driver.get('http://www.eyny.com/video.php')
time.sleep(2)

soup=BeautifulSoup(driver.page_source) #page_source=�������e

for i in soup.find('div','img_div_width'): # ��M�Ĥ@�� <div> �϶��B class="img_div_width"
    print (i)
    print ('-'*50)
    a = i.get('href')
    print (a)
    
    #URL=a+"http://www.eyny.com"

#------------------------------------------------------
from selenium import webdriver
import time
from bs4 import BeautifulSoup

browser=webdriver.Chrome()
browser.implicitly_wait(1)
browser.get('http://www.eyny.com/member.php?mod=logging&action=login&referer=/video.php')

browser.find_element_by_name('username').send_keys('###')
browser.find_element_by_name('password').send_keys('###')
browser.find_element_by_name('loginsubmit').click()
time.sleep(5)
soup=BeautifulSoup(browser.page_source)

URL=""
for data in open('test_eyny.txt','r',encoding='UTF-8'):
    data=data.strip()
    browser.find_element_by_name('srchtxt').send_keys(data+" OP")
    browser.find_element_by_class_name('button').click()
    time.sleep(2)

    for i in soup.find('div','img_div_width'): # ��M�Ĥ@�� <div> �϶��B class="img_div_width"
        a = i.get('href')
        URL="http://www.eyny.com"+a
        print (URL)

    browser.find_element_by_name('srchtxt').clear()