from bs4 import BeautifulSoup
from models.Animation import Animation
from models.Song import Song
from utils.session import Session

host="http://www.chia-anime.me/soundtracks/"

class ChiaList():
    def __init__(self,soup:BeautifulSoup):
        for a in soup.select('#tbAnimes .ma_menu a'):
            self.anime=Animation()
            self.anime.English=a.text
            self.sub_page(BeautifulSoup(Session().request("GET", host+a["href"]).content, 'html.parser'))

    def sub_page(self,soup):
        for tr in soup.select('#tbMusicas tr'):
            song=Song()
            song.anime=self.anime
            song.other=tr.select('td')[0].text
            song.title=tr.select('td')[1].text
            song.size=tr.select('td')[3].text
            song.long=tr.select('td')[4].text
            song.link="http://s9000.animepremium.tv/"+tr.select('td')[6].select_one('a')['href']


