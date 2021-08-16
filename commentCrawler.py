from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium
from selenium.webdriver.common.keys import Keys
import os
import pickle
from selenium.webdriver.common.action_chains import ActionChains
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")
wd = webdriver.Chrome('./chromedriver',chrome_options=chrome_options)

url = "https://www.facebook.com/bathandbodyworks/photos/a.165136625675/10160090757705676/"
postId = "10160090757705676"

url = url.replace("www", "m")
cookies = pickle.load(open("cookies.pkl", "rb"))
wd.get('https://www.facebook.com/')
for cookie in cookies:
    wd.add_cookie(cookie)
    
wd.get(url)
action = ActionChains(wd)

countbreak = 0
import  time

html_len = print(len(wd.page_source))

while True:
    time.sleep(5)
    try:
        
        try:
            element1 = wd.find_element_by_id("""popup_xout""")
            element1.click()
        except:
            pass

                
        try:
            repliesElements = wd.find_elements_by_class_name("_2a_m")
            for element in repliesElements:
                element.find_element_by_xpath('//a[contains(@href,"/comment")]').click()
        except Exception as e:
            pass
        

        element = WebDriverWait(wd, 10).until(
        EC.presence_of_element_located((By.ID, """see_next_{}""".format(postId))) 
        )
        print("found")
        element.click()
        print("click")
            


        print(html_len,len(wd.page_source))
        if html_len == len(wd.page_source):
            break
        else:
            html_len = len(wd.page_source)
            countbreak = 0


    except Exception as e:
        print(e)
        print("countine")
        countbreak += 1
        if countbreak == 5:
            break
        continue


doc = wd.page_source
file = open("./page_source/"+postId+".html", "w", encoding="utf-8") 
file.write(doc) 
file.close() 

file = open("./page_source/"+postId+ ".txt", "w", encoding="utf-8") 
file.write(doc) 
file.close() 