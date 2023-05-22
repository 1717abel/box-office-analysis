import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

month = []
day = []
year = []
day_of_week = []
top_10 = []
top_release = []
total_releases = []
top_grossing = []

#Get box office data for the year 2020
response = requests.get('https://www.boxofficemojo.com/daily/2020/?sort=date&sortDir=asc&ref_=bo_di__resort#table')
soup = bs(response.text,features="lxml")
data = soup.findAll("tr")[1:]

for n in data:
    month.append(n.a.text.split()[0])
    day.append(n.a.text.split()[1])
    year.append(2020)
    day_of_week.append(n.find("td",{"class":"a-text-left mojo-field-type-date_interval"}).text)
    money = n.findAll("td",{"class":"a-text-right mojo-field-type-money"})
    top_10.append(money[0].text[1:])
    top_release.append(n.find("td",{"class":"a-text-left mojo-field-type-release mojo-cell-wide"}).text)
    total_releases.append(n.find("td",{"class":"a-text-right mojo-field-type-positive_integer"}).text)
    top_grossing.append(money[1].text[1:])

#Get box office data for the year 2021 
response = requests.get('https://www.boxofficemojo.com/daily/2021/?sort=date&sortDir=asc&ref_=bo_di__resort#table')
soup = bs(response.text,features="lxml")
data = soup.findAll("tr")[1:]

for n in data:
    month.append(n.a.text.split()[0])
    day.append(n.a.text.split()[1])
    year.append(2021)
    day_of_week.append(n.find("td",{"class":"a-text-left mojo-field-type-date_interval"}).text)
    money = n.findAll("td",{"class":"a-text-right mojo-field-type-money"})
    top_10.append(money[0].text[1:])
    top_release.append(n.find("td",{"class":"a-text-left mojo-field-type-release mojo-cell-wide"}).text)
    total_releases.append(n.find("td",{"class":"a-text-right mojo-field-type-positive_integer"}).text)
    top_grossing.append(money[1].text[1:])

#Get box office data for the year 2022
response = requests.get('https://www.boxofficemojo.com/daily/2022/?sort=date&sortDir=asc&ref_=bo_di__resort#table')
soup = bs(response.text,features="lxml")
data = soup.findAll("tr")[1:]

for n in data:
    month.append(n.a.text.split()[0])
    day.append(n.a.text.split()[1])
    year.append(2022)
    day_of_week.append(n.find("td",{"class":"a-text-left mojo-field-type-date_interval"}).text)
    money = n.findAll("td",{"class":"a-text-right mojo-field-type-money"})
    top_10.append(money[0].text[1:])
    top_release.append(n.find("td",{"class":"a-text-left mojo-field-type-release mojo-cell-wide"}).text)
    total_releases.append(n.find("td",{"class":"a-text-right mojo-field-type-positive_integer"}).text)
    top_grossing.append(money[1].text[1:])


#Save data to csv
data = {"Month":month,"Day":day,"Year":year,"Day of Week":day_of_week,"Top 10 Gross":top_10,"Top Release":top_release,"Total Releases":total_releases,"Top Release Grossing":top_grossing}
df = pd.DataFrame(data)
df.to_csv("box_office.csv",index=False)
