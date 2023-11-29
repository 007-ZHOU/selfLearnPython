import scrapy


class MeinvSpider(scrapy.Spider):
    name = "meinv"
    allowed_domains = ["tupianzj.com"]
    start_urls = ["https://www.tupianzj.com/bizhi/DNmeinv/"]

    def parse(self, response,**kwargs):
        print(response.text)
        pass
 