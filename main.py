import asyncio
import functools
from bs4 import BeautifulSoup, element
from const import *
from models.ChiaAnime import ChiaAnime
from models.Animation import Status, Animation
from models.GoogleAnime import GoogleAnime
from utils.session import Session


def main():
    link_set = {}
    soup = BeautifulSoup(Session().request("GET", "http://www.chia-anime.me/index/").content, 'html.parser')
    for a in soup.select("div.post h4 div#ddmcc_container div.ddmcc ul ul li a[itemprop='url']"):
        en_title = a.select_one('span[itemprop="name"]').text
        link_set[en_title] = a['href']
        asyncio.run(run(link_set))

def googleChinese(keyword):
    keyword=keyword.replace(" ","+")
    return GoogleAnime( BeautifulSoup(Session().request("GET", "https://www.google.com/search?q="+keyword).content, 'html.parser')).Chinese

def save(animate:Animation):
    s=str(animate.__jsonencode__())
    open(DB_FILE,'a',encoding='utf-8').write(s+",\n")
    print(s)

async def run(link_set):
    async def fetch(title, url):
        res = await asyncio.get_event_loop().run_in_executor(None, functools.partial(
            Session().request,
            method="GET",
            url=url,
            title=title
        ))
        animate=ChiaAnime(BeautifulSoup(res.content, 'html.parser'))
        animate.Chinese = await asyncio.get_event_loop().run_in_executor(None, functools.partial(
            googleChinese,
            animate.English
        ))
        save(animate)

    await asyncio.gather(
        *[fetch(link, title) for link, title in link_set.items()]
    )


asyncio.run(run({"link_set": "http://www.chia-anime.me/episode/one-punch-man/",
                 # "link_set2":"http://www.chia-anime.me/episode/guilty-crown/",
                 }))
# main()
