from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium
from selenium.webdriver.common.keys import Keys
import os
from selenium.webdriver.common.action_chains import ActionChains
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")
driver = webdriver.Chrome('./chromedriver',chrome_options=chrome_options)
import pickle
from time import sleep 
usr = "khoa.tranbk99@gmail.com"
pwd = "Rubick135.2009"
cookies = pickle.load(open("cookies.pkl", "rb"))
driver.get('https://www.facebook.com/')
for cookie in cookies:
    driver.add_cookie(cookie)
driver.get("https://www.facebook.com/LOrealParisUSA/posts/10159057547456251")
# print ("Opened facebook")
# sleep(1)
  
# username_box = driver.find_element_by_id('email')
# username_box.send_keys(usr)
# print ("Email Id entered")
# sleep(1)
  
# password_box = driver.find_element_by_id('pass')
# password_box.send_keys(pwd)
# print ("Password entered")
  
# login_box = driver.find_element_by_xpath('//button[text()="Đăng nhập"]')
# login_box.click()
# sleep(1)
# driver.get("https://www.facebook.com/LOrealParisUSA/posts/10159057547456251")

# pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
# print ("Done")
# # # driver.quit()


