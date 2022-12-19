from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
START_URL = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
browser = webdriver.Chrome('C:/Users/HP/Desktop/Web scrapping/chromedriver.exe')
browser.get(START_URL)
time.sleep(10)
planets_data = []
def scrap():
        soup = BeautifulSoup(browser.page_source,'html.parser')
        bright_star_table = soup.find("table",attrs={'class',"wikitable"})
        table_body = bright_star_table.find('tbody')
        table_rows = table_body.find_all('tr')
        for row in table_rows:
            table_cols = row.find_all('td')
            temp_list = []
            for col_data in table_cols:
                print(col_data.text)
                data = col_data.text.strip()
                temp_list.append(data)
        planets_data.append(temp_list)

scrap()
stars_data=[]
for i in range(0,len(planets_data)):
    Star_names = planets_data[i][1]
    Distance = planets_data[i][3]
    Mass = planets_data[i][5]
    Radius = planets_data[i][6]
    Lum = planets_data[i][7]
    required_data = [Star_names,Distance,Mass,Radius,Lum]
    stars_data.append(required_data)
headers = ['Star_name','Distance','Mass','Radius','Luminosity']
planets_df_1 = pd.DataFrame(planets_data,columns=headers)
planets_df_1.to_csv('scrapData.csv',index=True, index_label='id')
