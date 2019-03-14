from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

browser=webdriver.Chrome()
browser.implicitly_wait(1)
browser.get('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Fnext%3D%252F%253Fgl%253DTW%2526hl%253Dzh-TW%26hl%3Den%26app%3Ddesktop%26action_handle_signin%3Dtrue&passive=true&service=youtube&uilel=3&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

browser.find_element_by_id('identifierId').send_keys('###')
browser.find_element_by_id('identifierId').send_keys(Keys.RETURN)
browser.find_element_by_name('password').send_keys('###')
browser.find_element_by_name('password').send_keys(Keys.RETURN)
time.sleep(5)
soup=BeautifulSoup(browser.page_source)
print ('Login OK')