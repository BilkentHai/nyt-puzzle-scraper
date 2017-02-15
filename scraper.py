import requests
import re
import json
import base64


def scrape():
    URL = 'http://www.nytimes.com/crosswords/game/mini?page=mini&type=mini&date=&_r=02'

    s = requests.session()
    s.headers= {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:53.0) Gecko/20100101 Firefox/53.0'}

    response = s.get(URL)

    print(re.search( r"window.preload = '(.*?)';", response.text))
    searched = re.search( r"window.preload = '(.*?)';", response.text).group(1)
    decoded = base64.b64decode(searched)

    data = json.loads( decoded)
    print(json.dumps( data, indent = 4, sort_keys = True))
    return data[0]