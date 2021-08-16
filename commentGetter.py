from bs4 import BeautifulSoup
import re
import pandas as pd

postId = "10160090757705676"
f = open("./page_source/"+postId+ ".txt", "r",encoding="utf8")
text = f.read()
soup = BeautifulSoup(text, 'html.parser')


commnets = soup.find_all("div", {'data-sigil': re.compile('comment'),"data-store":re.compile(postId)})




def commentExtractor(comment):
    name = comment.find("div", {"class": "_2b05"}).getText()
    id = comment["id"]
    textComment = comment.find("div",{'data-sigil':"comment-body"}).getText()

    try:
        tagName =  comment.find("div",{'data-sigil':"comment-body"}).find("a",href =True).getText()
    except Exception as e:
        tagName = None
    date = comment.find("abbr",{'class':"_4ghv _2b0a"}).getText()

    subcomments = comment.find_all("div", {'class': "_2a_i"})
    if not subcomments:
        ChildrenReply = None
    else:
        ChildrenReply = []

        for tag in subcomments:
            if 'id' in tag.attrs:
               ChildrenReply.append(tag['id'])


    return[name,id,textComment,tagName,date,ChildrenReply,None]


df = pd.DataFrame(columns=["name","id","textComment","tagName","date","ChildrenReply","ParentReply"])


for i,comment in enumerate(commnets):
    df.loc[len(df)] = commentExtractor(comment)

for i,replyIds in enumerate(df["ChildrenReply"]):
    for j,commentId in enumerate(df["id"]):
        if commentId in replyIds:
            df.loc[j,"ParentReply"] = df.loc[i,["id"]]

    

print(df)

df.to_csv("./data/"+ postId + ".csv",index = False, encoding='utf-8-sig')