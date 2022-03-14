import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import pandas as pd
from bs4 import BeautifulSoup as bs
import time
import urllib.request
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome()
url = "http://books.toscrape.com/?"
driver.get(url)
oururl=urllib.request.urlopen(url)
soup = bs(oururl,'html.parser')

print(soup.prettify())

x = driver.find_elements(By.XPATH, '//*[@id="default"]/div/div/div/div/section/div[2]/ol/li[1]')

print(x)

titre = []
for i in soup.findAll('article',{'class':'product_pod'}):
    img=i.find('h3').text
    print(img)
    titre.append(img)

prix = []

for x in soup.findAll('div',{'class':'product_price'}):
    p=x.find('p').text
    print(p)
    prix.append(p)

    
df = pd.DataFrame(titre)    
df.to_csv("result.csv")

df = pd.read_csv('result.csv', na_values=' ')
df.head()