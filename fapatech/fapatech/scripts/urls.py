import requests
from utils.helper import (
    TSOFT_BASED_URL_LIST
)

import re

def tsoft_based_url_crawl():
    urls = list()
    for url in TSOFT_BASED_URL_LIST:
        content = requests.get(url).text
        url_output = re.findall(r"<loc>(.+)<\/loc>", content)
        urls.append(url_output)
    
    url_list = [item for sublist in urls for item in sublist]
    return url_list
    

def fetch_url():
    res = tsoft_based_url_crawl()
    print(res)

fetch_url()