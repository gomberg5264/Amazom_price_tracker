import requests
import lxml
from bs4 import BeautifulSoup
from django.db import migrations, models

def get_link_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
    }

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "lxml")

    name = soup.select_one(selector="#productTitle").getText()
    name = name.strip()
    
    if(soup.select_one(selector="#priceblock_dealprice")):
        price = soup.select_one(selector="#priceblock_dealprice").getText()
        price = float(price[2:].replace(",",""))
    
    if(soup.select_one(selector="#priceblock_saleprice")):
        price = soup.select_one(selector="#priceblock_saleprice").getText()
        price = float(price[2:].replace(",",""))

    if(soup.select_one(selector="#priceblock_ourprice")):
        price = soup.select_one(selector="#priceblock_ourprice").getText()
        price = float(price[2:].replace(",",""))


    return name, price