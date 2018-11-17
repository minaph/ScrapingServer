#%%

import pandas as pd
from urllib.error import HTTPError, URLError
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://dancekeepers.com/%E3%82%B8%E3%83%A3%E3%83%B3%E3%83%AB%E5%88%A5/%E6%8A%80%E3%81%AE%E8%A7%A3%E8%AA%AC/"
url=urlopen(url)
keeper= BeautifulSoup(url)


# while True:
#     keeper.script.extract()
#     if not keeper.find_all("script"):
#         break

def extracter(bs,key):
    while True:
        bs.find(key).extract()
        if not bs.find_all(key):
            break
    return bs

keeper=extracter(keeper,"script")
print(keeper)

# print(keeper.get_text())

