import requests
from bs4 import BeautifulSoup

URL = 'https://www.jumia.co.ke/xiaomi-redmi-8a-6.22-inches-2-gb-32-gb-dual-sim-blue-25188941.html'

headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'}

page = requests.get(URL,headers = headers)

soup1 = BeautifulSoup(page.content, 'html.parser')

soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')

title = soup2.select_one('title').text.strip()
price = soup2.select_one('data-price').text.strip()


# try:
#     title = soup2.find(id = "title").get_text()
# except AttributeError:
#     print ("title Number: -")


# #price = soup.find(id = "priceblock_ourprice").get_text()
# #converted_price = price[0:5]


print(title)
