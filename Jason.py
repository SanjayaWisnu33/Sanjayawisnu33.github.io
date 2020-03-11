
import requests
import json
from bs4 import BeautifulSoup
import datetime


my_dict = {}

page = requests.get("https://www.republika.co.id/")
obj = BeautifulSoup(page.text, 'html.parser')
all = []
for headline in obj.find_all('div',class_='teaser_conten1'):
    currentDT = datetime.datetime.now()
    x = (headline.find('h1').text)
    y = (headline.find('h2').text)
    z = (headline.find('div', class_='date').text)
    t = currentDT.strftime("%d %b %Y %H:%M:%S")
    my_dict['Kategori']=x
    my_dict['Judul']=y
    my_dict['Waktu']=z
    my_dict['Waktu_Publish']= t    
    
    all.append( dict(my_dict))    
    

dict_web = all
with open('scrap.json', 'w') as file:
    json.dump(dict_web, file, indent=4)

    '''Helped by Azhar Subhan Fauzi and Mr. Lukmannul'''
