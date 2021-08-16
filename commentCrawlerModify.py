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

url = "https://www.facebook.com/LOrealParisUSA/posts/10159057547456251"
postId = "10159057547456251"

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

        element = WebDriverWait(wd, 10).until(
        EC.presence_of_element_located((By.ID, """see_next_{}""".format(postId))) 
        )
        print("found")

        element.click()
        print("click")

        if html_len == len(wd.page_source):
            break
        else:
            html_len = len(wd.page_source)
            countbreak = 0


    except:
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