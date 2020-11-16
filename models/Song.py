from dataclasses import dataclass
from typing import List

from models.Animation import Animation


@dataclass
class Song:
    title: str = None
    link: str = None
    size:str=None
    long:str=None
    anime:Animation=None
    other:str=None

    def __jsonencode__(self):
        d={}
        for i in vars(self):
            d[i]=self.__getattribute__(i)
        return d
