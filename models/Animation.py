from dataclasses import dataclass
from datetime import datetime
from enum import Enum, auto
from typing import List, Optional


class Status(Enum):
    FinishedAiring = auto()

@dataclass
class Animation:
    English: str = None
    link: str = None
    Japanese:str = None
    Chinese:str = None
    Synonyms:List[str]= None
    Type: str = None
    Episodes: str = None
    Status: Status= None
    Aired: datetime= None
    Premiered: str= None
    Genres: List[str]= None
    Duration: str= None
    Rating: str= None

    def __jsonencode__(self):
        d={}
        for i in vars(self):
            d[i]=self.__getattribute__(i)
        return d
