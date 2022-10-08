import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import collections
import numpy as np

#import data from wikipedia
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
country  = data_break[data_break.columns[2]]
country = collections.Counter(country)
a, b = zip(*collections.Counter(country).items())

data_country = []
df = pd.DataFrame({'Country' : a, 'Number of occurrences' : b})    
df = df.sort_values(by=['Number of occurrences'],ascending=False)
df.to_csv('Country.csv', index=False, encoding='utf-8')

#Question - 3

succesfull = data_break[['Country','Succeeded']]
pom = data_break[['Succeeded']] 
pom = pom.values.tolist()
n = 0 
for x in pom:
    if x == ['Yes']:
        n += 1
    else:
        succesfull = succesfull.drop(index =n)
        n += 1

country = collections.Counter(succesfull[succesfull.columns[0]])
a,b = zip(*collections.Counter(country).items())

data_country = []
df = pd.DataFrame({'Country' : a, 'Number of succeeded occurrences' : b})    
df = df.sort_values(by=['Number of succeeded occurrences'],ascending=False)
df.to_csv('Succeeded_country.csv', index=False, encoding='utf-8')
