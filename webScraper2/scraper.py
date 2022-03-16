from bs4 import BeautifulSoup
import time
import csv 
import requests
import pandas as pd 

startUrl ="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page = requests.get(startUrl)
print(page)
soup = BeautifulSoup(page.content, 'html.parser')
tempList = []
startTable = soup.find('table')
tableRows = startTable.find_all('tr')

for tr in tableRows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    tempList.append(row)
    
starNames = []
distance = []
mass = []
radius = []
lum = []

for i in range(1, len(tempList)):
    starNames.append(tempList[i][1])
    distance.append(tempList[i][3])
    mass.append(tempList[i][5])
    radius.append(tempList[i][6])
    lum.append(tempList[i][7])

df2 = pd.DataFrame({'Star Name': starNames, 'Distance': distance, 'Mass': mass, 'Radius': radius, 'Luminosity': lum})

print(df2)
df2.to_csv('stars.csv')
