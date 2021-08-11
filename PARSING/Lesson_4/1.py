'''
Написать приложение, которое собирает основные новости с сайтов mail.ru, lenta.ru, yandex-новости.
Для парсинга использовать XPath. Структура данных должна содержать:
название источника;
наименование новости;
ссылку на новость;
дата публикации.
'''

from lxml import html
import requests


header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}


def request_to_mail(_str):
    try:
        response = requests.get('https://news.mail.ru/', params={'text': _str}, headers=header)
        root = html.fromstring(response.text)
        for i in range(1, 5):
            result = root.xpath(f'//*[@id="index_page"]/div[7]/div[2]/div[3]/div/div/div/div[{i}]/div/div[2]/span[2]/a/span')
            link = root.xpath(f'//*[@id="index_page"]/div[7]/div[2]/div[3]/div/div/div/div[{i}]/div/div[2]/span[2]/a/@href')
            ist = root.xpath(f'//*[@id="index_page"]/div[7]/div[2]/div[3]/div/div/div/div[{i}]/div/div[2]/div/span[2]/text()')
            tim = root.xpath(f'//*[@id="index_page"]/div[7]/div[2]/div[3]/div/div/div/div[{i}]/div/div[2]/div/span[1]')
            print([ist[0]], result[0].text, ' ', link[0], tim[0].text)
    except:
        print('Ошибка запроса')


request_to_mail('')
