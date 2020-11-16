from bs4 import BeautifulSoup

from models.Animation import Animation


class GoogleAnime(Animation):
    def __init__(self,soup:BeautifulSoup):
        self.Chinese = soup.select_one("h2.qrShPb span").text
