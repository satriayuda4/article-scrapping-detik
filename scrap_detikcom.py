from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd

chrome_options = Options()
chrome_options.add_argument("--headless")

PATH = 'chromedriver.exe'
driver = webdriver.Chrome(PATH, options = chrome_options)

def scrap_link(link):
    for i in range(10):
        j = i+1
        element = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[1]/article[' + str(j) + ']/a')
        href = element.get_attribute('href')
        link.append(href)

def scrap_date():
    date_list = []
    element = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div[1]/article/div[1]/div[2]')
    date = element.text
    date_list.append(date)

def scrap_title():
    title_list = []
    element = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div[1]/article/div[1]/h1/text()')
    title = element.text
    title_list.append(title)

def next_page():
    element = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/a[6]')
    next_link = element.get_attribute('href')
    driver.get(next_link)

tag = 'tag'

link_home = "https://www.detik.com/tag/" + tag + "/?sortby=time&page="
print(link_home)

link_ = []

#scrapp every news link in every page 
page = 18
for n in range(page):
    n += 1
    print(n,'/',str(page))
    link_scrapping = link_home + str(n)
    driver.get(link_scrapping)
    driver.implicitly_wait(2)
    scrap_link(link_)

driver.quit()
df = pd.DataFrame({'link': link_})
df.to_csv('result'+tag+'.csv', index=False)
