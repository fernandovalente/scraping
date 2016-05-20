import json
import codecs
from bs4 import BeautifulSoup
from urllib.request import urlopen


def open_and_returns_bs4_object(url):
    html = urlopen(url)
    return BeautifulSoup(html)


def create_json_file(data, factory_name):

    json_file = '{}.json'.format(factory_name)

    try:
        with codecs.open(json_file, 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, ensure_ascii=False)
    except Exception as e:
        raise e

    return 'Created {}'.format(json_file)
