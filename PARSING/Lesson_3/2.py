'''
2. Написать функцию, которая производит поиск и выводит на экран вакансии
с заработной платой больше введённой суммы.
'''

import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint


header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
url = 'https://www.rabota.ru'


def get_data(zp):
    resp = requests.get(f'https://www.rabota.ru/?sort=relevance&min_salary={zp}', headers=header)
    soup = bs(resp.text, 'lxml')
    result = []
    work = soup.find_all(class_="vacancy-preview-card__title")
    link = soup.find_all(class_='vacancy-preview-card__title')
    price = soup.find_all(class_="vacancy-preview-card__salary vacancy-preview-card__salary-blue")
    for i in range(20):
        result.append({
            'Вакансия': work[i].text.strip(),
            'Зарплата': price[i].text.strip().replace('\xa0', ' '),
            'Ссылка': url + link[i].find('a').get('href')
        })
        pprint(result[i])
        print('-' * 90)


get_data(80000)  # Требуемая зарплата
