import requests
import json
import os
from bs4 import BeautifulSoup as bs
from datetime import datetime
now = datetime.now()

page = requests.get("https://republika.co.id/")
data = []
obj = bs(page.text, 'html.parser')
# Deklarasi list kosong
# Lokasi file json
with open(f'{os.getcwd()}\JSON\data_atribut.json','w') as file:
    for atribut in obj.find_all('div',class_='conten1'):
    # append headline ke variable data
        data.append({"judul":atribut.find('h2').text,"kategori":atribut.find('a').text,"waktu_publish":atribut.find('div',class_='date').text,"waktu_scraping":now.strftime("%Y-%m-%d %H:%M:%S")})
    # dump list dictionary menjadi json
    jdumps=json.dumps(data, indent=2)
    file.writelines(jdumps)