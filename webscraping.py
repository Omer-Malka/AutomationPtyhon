from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome('C:\Program Files\ProgFiles\chromedriver.exe')

name = []
ratings = []

driver.get("https://www.imdb.com/chart/top/")

content = driver.page_source
soup = BeautifulSoup(content)

for a in soup.find_all('td', attrs={'class': 'titleColumn'}):
    name.append(str(a.text).strip())

for b in soup.find_all('td', attrs={'class': 'ratingColumn imdbRating'}):
    ratings.append(str(a.text).strip())

df = pd.DataFrame({'Product Name': name, 'Ratings': ratings})
df.to_csv('products.csv', index=False, encoding='utf-8')
