from bs4 import BeautifulSoup
import re
import pandas as pd
f = open("page_source.txt", "r",encoding="utf8")
text = f.read()
soup = BeautifulSoup(text, 'html.parser')

postId = "3994102397294836"
commnets = soup.find_all("div", {'data-sigil': 'comment',"data-store":re.compile(postId)})

print(len(commnets))


def commentExtractor(comment):
    avatar = comment[0]
    divComment = list(comment[1])
    DivText = list(divComment[0])

    # for div in divComment:
    #     if re.search("Xem thêm",div.getText()):
    #         DivDate = div

    # date = DivDate.getText().replace("Xem thêm","")
    try:
        reply = divComment[2]
        replyFlag = True
    except:
        replyFlag = False

    text = []
    try:
        name, text = DivText[0]
    except:
        name = DivText[0]
    
    try:
        name = name.getText()
    except:
        pass


    if not text:
        return[name,None,None,replyFlag]


    tagName = None
    textComment = None
    if len(text) == 1:
        textComment = text.getText()
    else:
        tagName = [ tagname.getText() for tagname in text.find_all("a")]
        textComment = text.getText()

    

    return[name,textComment,tagName,replyFlag]



df = pd.DataFrame(columns=["name","textComment","tagName","replyFlag"])


for i,comment in enumerate(commnets):
    df.loc[len(df)] = commentExtractor(list(comment))
    
print(df)

df.to_csv("./data"+"/"+postId+".csv",index = False, encoding='utf-8-sig')