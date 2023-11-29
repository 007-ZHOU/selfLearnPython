import scrapy


class ZhipinSpider(scrapy.Spider):
    name = "zhipin"
    allowed_domains = ["zhipin.com"]
    start_urls = ["https://www.zhipin.com/web/geek/job?query=python&city=101210300"]

    def parse(self, response):
        print(response.text)
f