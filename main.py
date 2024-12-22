import requests
from bs4 import BeautifulSoup
import lxml


from typing import Optional, Union

class Tracker:
    """Amazon product price tracker.
    
    Attributes:
        url (str): Amazon product URL to track
    """
    def __init__(self, url: str):
        """Initialize tracker with product URL.
        
        Args:
            url: Amazon product page URL
        """
        self.url = url

    def get_price(self):
        headers = {'Accept-Language': "en-US,en;q=0.9",
                   'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35"}
        response = requests.get(self.url, headers=headers)

        print(response)

        soup = BeautifulSoup(response.content, "lxml")
        price_data = soup.find("span", class_="a-offscreen")
        price = price_data.getText()
        split_price = float(price.split("$")[1])
        title = soup.find(id="productTitle").get_text().strip()
        print(title)
        return split_price

    def show_price(self):
        print(self.get_price())




