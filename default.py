from bs4 import BeautifulSoup
from urllib.request import urlopen


def open_and_returns_bs4_object(url):
    """ Receives a url and return an BS4 object """

    html = urlopen(url)
    return BeautifulSoup(html)
