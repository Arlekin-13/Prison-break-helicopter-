import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import collections
import numpy as np

def data_URL(url,tag_name,class_name):
    response = requests.get(url)
    if response.status_code != 200:
        print('Page not found')
    else:
        soup = BeautifulSoup(response.text,'html.parser')
        html_output = soup.find(tag_name,{'class':class_name})
        output = pd.read_html(str(html_output))
    return output[0]

data_break = data_URL('https://en.wikipedia.org/wiki/List_of_helicopter_prison_escapes','table','wikitable')


#Question - 1
year = data_break[data_break.columns[0]]

data_year = []

for i in year:
    if ', ' in i:
        i = i[i.find(', '):] 
        i = i.replace(', ','')
        data_year.append(i)
    else:
        i = i[i.find(' '):]
        i = i.replace(' ','')
        data_year.append(i)

year = collections.Counter(data_year)

a, b = zip(*collections.Counter(year).items())

l = list(range(1,len(a)+1))

fig, ax = plt.subplots(figsize= (16,9))

ax.barh(a, b)

ax.xaxis.set_ticks_position('none')

ax.yaxis.set_ticks_position('none')

ax.invert_yaxis()

ax.set_title('Number of helicopter escapes in a given year',loc ='left', )

plt.savefig('break.png')

#Question - 2
