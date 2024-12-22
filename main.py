from bs4 import BeautifulSoup
import aiohttp
import asyncio

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
        self.HEADERS = {'Accept-Language': "en-US,en;q=0.9",
                            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35"}

    async def get_item_info(self) -> tuple[float, str]:
        """     Returns:
                [0] Price
                [1] Title
         """

        async with aiohttp.ClientSession() as session:
            async with session.get(self.url, headers=self.HEADERS) as response:
                soup = BeautifulSoup(await response.text(), "lxml")
                price_data = soup.find("span", class_="a-offscreen")
                price = price_data.getText()
                split_price = float(price.split("$")[1])
                title = soup.find(id="productTitle").get_text().strip()
                return split_price, title

    async def show_price_in_console(self) -> None: # Primarily a debugging feature
        item_info = await self.get_item_info()
        print(item_info[1], item_info[0])
