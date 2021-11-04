import requests
from bs4 import BeautifulSoup

page = requests.get("https://finance.detik.com/lainnya/d-5654920/sikat-bank-indonesia-buka-lowongan-jalur-pcpm-nih")
print(page.status_code)

#print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())

#print(list(soup.children))

#print([type(item) for item in list(soup.children)])

html = list(soup.children)[2]

body = list(html.children)[3]
#print(list(body.children))

p = list(body.children)[1]
#print(p.get_text())

#Finding all instances of a tag at once
soup = BeautifulSoup(page.content, 'html.parser')
par = soup.find_all('p')

file1 = open("myfile.txt","w")

for i in range(len(par)):
    txt = par[i]
    file1.write(txt.get_text())
    file1.write('\n')

print(txt.get_text())

soup = BeautifulSoup(page.content, 'html.parser')
date = soup.find_all(class_ = "detail__date")

date = date[0]

print(date.get_text())
title = soup.find_all(class_ = "detail__title")

title = title[0]

print(title.get_text())