# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class  CaiPiaoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    qiHao=scrapy.Field()
    redBall=scrapy.Field()
    blueBall=scrapy.Field()

