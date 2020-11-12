from bs4 import BeautifulSoup

from models.Animation import Animation


class ChiaAnime(Animation):
    def __init__(self,soup:BeautifulSoup):
        for blockquote in soup.select('div.post.wrap blockquote div.d'):
            title = blockquote.select_one('span.b').text.strip()[:-1]
            content:str = blockquote.contents[1].strip()
            if title in ['Synonyms','Genres']:
                if ", " in content:
                    self.__setattr__(title,content.split(", "))
            elif title=='Episodes':
                self.Episodes=int(content)
            elif title=='Aired':
                continue
            else:
                self.__setattr__(title,content)
