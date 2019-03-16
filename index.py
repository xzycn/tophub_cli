import fire
import requests
from scrapy.selector import Selector
import webbrowser

URL = "https://tophub.today/"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"
}


class Reader:

    def getlist(self, t="all"):
        content = requests.get(URL, headers=headers)
        se = Selector(text=content.text)
        # if t == "all":
        top_eles = se.xpath("//*[@id='Sortable']/div")
        for ele in top_eles:
            site = ele.xpath(".//div[@class='cc-cd-lb']/text()").extract_first()
            hot_list = ele.xpath(".//div[contains(@class,'nano-content')]/a/div/span[2]/text()").extract()
            print(site + ": ")
            for i,hot in enumerate(hot_list, start=1):
                print(f"{site}-{i}-{hot}")


if __name__ == '__main__':
    fire.Fire(Reader)
