import requests
from bs4 import BeautifulSoup 

def make_soup(url: str) -> BeautifulSoup:
    res = requests.get(url, headers={
        "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'
    })
    res.raise_for_status()
    return BeautifulSoup(res.text, 'lxml')

def parse_product_page(soup: BeautifulSoup) -> dict:
    title = soup.select_one('title').text.strip()
    price = soup.select_one('span', {"dir":"data-price"}).text.strip()
   
    return {
        'title': title ,
         'price': price
    }

if __name__ == "__main__":
    url = 'https://www.jumia.co.ke/xiaomi-mi-a2-lite-5.84-4g-32gb-3g-ram-fingerprint-12mp-5mp-dual-rear-camera-gold-13401333.html'
    soup = make_soup(url)
    info = parse_product_page(soup)
    print(info)

 