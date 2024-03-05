# from parsel import Selector
# import httpx
# import asyncio
#
#
# class AsyncScraper:
#     PLUS_URL = 'https://24.kg/'
#     URL = 'https://24.kg/'
#     HEADERS = {
#         "Accept-Language":
#             "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0"
#     }
#     LINK_XPATH = '//div[@class="one"]/div[@class="h2"]/a/@href'
#     async def fetch_page(self, client, page):
#         try:
#             url = self.URL.format(page=page)
#             response = await client.get(url, timeout=10.0)
#             print(f"Страница : {page}")
#
#             if response.status_code == 200:
#                 return Selector(text=response.text)
#             else:
#                 response.raise_for_status()
#         except httpx.ReadTimeout:
#             print(f"ReadTimeoutError on page: {page}")
#             return None
#
#     async def scrape_page(self, selector):
#         links = selector.xpath(self.LINK_XPATH).getall()
#         print(links)
#
#     async def get_pages(self, limit=10):
#         async with httpx.AsyncClient(headers=self.HEADERS) as client:
#             tasks = [self.fetch_page(client=client, page=page) for page in range(1, limit + 1)]
#             pages = await asyncio.gather(*tasks)
#             scrape_tasks = [self.scrape_page(page) for page in pages if page is not None]
#             await asyncio.gather(*scrape_tasks)
#
#
# if __name__ == "__main__":
#     scraper = AsyncScraper()
#     asyncio.run(scraper.get_pages())
