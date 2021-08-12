'''
2. Написать функцию, которая производит поиск и выводит на экран вакансии
с заработной платой больше введённой суммы.
'''

import requests
from pprint import pprint
from lxml import html
from bs4 import BeautifulSoup as bs
import requests as req

http = 'https://www.superjob.ru'
s = input('Желаемая зарплата от: ')
url = f'{http}/vacancy/search/?payment_value={s}'


respond = req.get(url)
soup = bs(respond.text, 'lxml')
vac = [i.text.strip() for i in soup.find_all(class_="_1h3Zg _2rfUm _2hCDz _21a7u")]
price = [str(i.text).replace('\xa0', ' ') for i in soup.find_all(class_="_1h3Zg _2Wp8I _2rfUm _2hCDz _2ZsgW")]

vacans = []
link = []

for i in vac:
    vacans.append(i)

result = []
for i in range(20):
    result.append({
        'Вакансия': vacans[i],
        'Зарплата': price[i]
    })

for i in result:
    print(i)
