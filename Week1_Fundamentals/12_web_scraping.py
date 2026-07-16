import requests
import time
from fake_useragent import UserAgent
url=https://www.flipkart.com/mobile-accessories/power-banks/pr?sid=tyy%2C4mr%2Cfu6&p%5B%5D=facets.price_range.from%3D1999&sort=popularity&param=43764743&BU=EmergingElectronics&p%5B%5D=facets.price_range.to%3DMax&p%5B%5D=facets.capacity%255B%255D%3D13000%2B-%2B19999%2BmAh&p%5B%5D=facets.capacity%255B%255D%3DAbove%2B20000%2BmAh


session = requests.session()

header = {
    "User-Agent": UserAgent().random,
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Connection": "keep-alive",
    "Referer": "https://www.google.com/"
}

time.sleep(2)
r = session.get(url, proxies=proxies, headers= headers)

with open("file.html","w") as f:
    f.write(r.text)