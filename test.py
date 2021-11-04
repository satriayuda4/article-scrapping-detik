from selenium import webdriver
import pandas as pd
import time

PATH = 'chromedriver.exe'
driver = webdriver.Chrome(PATH)

def scrap_link():
    for i in range(10):
        j = i+1
        element = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[1]/article[' + str(j) + ']/a')
        href = element.get_attribute('href')
        link.append(href)

def scrap_date():
    element = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div[1]/article/div[1]/div[2]')
    date = element.text
    date_list.append(date)

def scrap_title():
    element = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div[1]/article/div[1]/h1/text()')
    title = element.text
    title_list.append(title)

def next_page():
    element = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/a[6]')
    next_link = element.get_attribute('href')
    driver.get(next_link)

link_home = "https://www.detik.com/tag/bank-indonesia/?sortby=time&page="
link = []
date_list = []
title_list = []

#scrapp every news link in every page 
for n in range(20):
    n += 1
    print(n,'/20')
    link_scrapping = link_home + str(n)
    driver.get(link_scrapping)
    driver.implicitly_wait(2)
    scrap_link()


driver.quit()
df = pd.DataFrame({'link': link})
df.to_csv('result.csv', index=False)