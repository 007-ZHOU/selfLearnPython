import scrapy


class EnterSpider(scrapy.Spider):
    name = "enter"
    allowed_domains = ["alibaba.com"]
    def start_requests(self):
        urls = [
            'https://www.alibaba.com/product-detail/Design-Home-Light-Luxury-Furniture-Sofa_1600992749835.html',
            'https://www.alibaba.com/product-detail/Simple-Modern-Design-Living-Room-Sofa_1600992771942.html',
            'https://www.alibaba.com/product-detail/Modern-Sectional-Corner-Couch-Sofa-Set_1600992872124.html',
        ]
        for i in range(50):
            for url in urls:
                # yield scrapy.Request(url=url, callback=self.parse,meta={'proxy':'http://'+'89.109.252.139:8081'})
                yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        type=response.xpath('//*[@id="container"]/div[2]/div[1]/div[1]/div[6]/div/div/div[2]/div[7]/div[2]/span/text()').extract_first()
        print(type)
        # 处理响应的代码

