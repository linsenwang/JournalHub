from lib.types import Route
from lib.utils.requests import requests
from bs4 import BeautifulSoup

def handler():
    host = 'https://www.aeaweb.org/journals/articles/sgml?journal=1'
    response = requests(host)
    soup = BeautifulSoup(response.content, 'html.parser')
    volume = soup.select('#volumeSelect option')[-1].attrs['value']

    url = f'https://www.aeaweb.org/journals/articles/sgml?journal=1&volume={volume}'
    response = requests(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    issue = soup.select('#issueSelect option')[-1].attrs['value']

    url = f'https://www.aeaweb.org/journals/articles/sgml-export?issueid={issue}'
    response = requests(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    items = list(map(lambda item: {
        'title': item.find('ti').text,
        'link': item.find('art_url').text,
        'description': item.find('ab').text if item.find('ab') else '',
        # 'pubDate': item.find('h6').get_text(strip=True) if item.find('h6') else ''
    }, soup.select('head')))

    return {
        'title': 'American Economic Review',
        'item': items,
        'link': host
    }

route = Route(
    path = '/aer',
    name = 'American Economic Review',
    url = 'www.aeaweb.org/journals/aer',
    handler = handler
)
