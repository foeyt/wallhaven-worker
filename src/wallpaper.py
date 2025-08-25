import requests
import random
from lxml import etree

class WallHaven:
    def __init__(self):
        self.url = "https://wallhaven.cc/search?categories=110&purity=100&atleast=1920x1080&sorting=random&order=desc&seed=HmUG9N&page=" + str(random.randint(2, 8056))
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }

    def get_page(self, url):
        page = requests.get(url, headers=self.headers, timeout=10000).content.decode("utf-8")
        return page

    def get_wallpaper(self):
        html = self.get_page(self.url)
        wallpaper_list = etree.HTML(html).xpath("//figure/a/@href")
        if len(wallpaper_list) == 0:
            print("FAILED, RETRYING...")
            self.get_wallpaper()
        return wallpaper_list
    
    def download_image(self, wallpaper):
        print("GETTING... " + wallpaper)
        html = etree.HTML(self.get_page(wallpaper))
        names = html.xpath("//div[@class=\"scrollbox\"]//img/@src")
        with open("wallpaper.png", "wb") as f:
            f.write(requests.get(url=names[0], headers=self.headers, timeout=30).content)

wallhaven = WallHaven()
wallhaven.download_image(wallhaven.get_wallpaper()[random.randint(0, len(wallhaven.get_wallpaper()) - 1)])
print("SUCCESSFUL")

