import requests
from bs4 import BeautifulSoup
import pandas as pd

df = pd.read_csv("result.csv") 
news_list = df.link

def extract_text(txt):
    tmp = ''
    for i in txt:
        tmp += i.get_text()
        tmp += '\n'
    return tmp

title_list = []
date_list = []
text_list = []

for i in range(len(news_list)):
    page = requests.get(news_list[i])
    print(news_list[i])
    print('status code:',page.status_code)
    soup = BeautifulSoup(page.content, 'html.parser')
    title_ = soup.find_all(class_ = "detail__title")
    date_ = soup.find_all(class_ = "detail__date")
    par_ = soup.find_all('p')
    print(title_[0].get_text())
    print(date_[0].get_text())
    text = extract_text(par_)
    title_list.append(title_[0].get_text())
    date_list.append(date_[0].get_text())
    text_list.append(text)
    print(str(i),'/',str(len(news_list)))

df = pd.DataFrame({'link': news_list,
                   'title': title_list,
                   'date': date_list,
                   'text': text_list})
df.to_csv('result-txt-title.csv', index=False)
