from bs4 import BeautifulSoup
import pandas as pd
import requests


START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

page = requests.get(START_URL)
temp_list = []
soup = BeautifulSoup(page.content,"html.parser")

stars = soup.find_all("table",attrs={ "class","wikitable sortable"})

table_rows = stars[1].find_all('tr')

brown_stars_data= []
for i in range(0,len(temp_list)):
    Star_names = temp_list[i][1]
    Distance = temp_list[i][3]
    Mass = temp_list[i][5]
    Radius = temp_list[i][6]

    required_data = [Star_names, Distance, Mass, Radius]
    brown_stars_data.append(required_data)

headers = ["Star name", "Distance", "Mass", "Radius"]

star_df_1 = pd.DataFrame(brown_stars_data,columns=headers)
star_df_1.to_csv('brownstars.csv', index=True, index_label='id')