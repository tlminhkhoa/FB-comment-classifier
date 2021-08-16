from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium
from selenium.webdriver.common.keys import Keys
import os
import re
import pickle
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import pandas as pd
chrome_options = webdriver.ChromeOptions()
postId = "10160090757705676"
f = open(postId+ ".txt", "r",encoding="utf8")
text = f.read()
soup = BeautifulSoup(text, 'html.parser')


commnets = soup.find_all("div", {'data-sigil': re.compile('comment'),"data-store":re.compile(postId)})

def commentExtractor(comment):
    name = comment.find("div", {"class": "_2b05"}).getText()
    textComment = comment.find("div",{'data-sigil':"comment-body"}).getText()

    try:
        tagName =  comment.find("div",{'data-sigil':"comment-body"}).find("a",href =True).getText()
    except Exception as e:
        tagName = None
    date = comment.find("abbr",{'class':"_4ghv _2b0a"}).getText()

    subcomments = comment.find_all("div", {'class': "_2a_i"})
    if not subcomments:
        replyFlag = None
    else:
        replyFlag = []

        for tag in subcomments:
            if 'id' in tag.attrs:
               replyFlag.append(tag['id'])


    return[name,textComment,tagName,date,replyFlag]



df = pd.DataFrame(columns=["name","textComment","tagName","date","replyFlag"])


for i,comment in enumerate(commnets):
    df.loc[len(df)] = commentExtractor(comment)
    
# print(commentExtractor(commnets[0]))
print(df)

# print(len(commnets))
