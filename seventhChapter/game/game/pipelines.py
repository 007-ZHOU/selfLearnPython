# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

#记住，管道默认是不生效的，需要去settings里面去开启管道,settings 中的ITEM_PIPELINES
class GamePipeline:
    def process_item(self, item, spider):#这个方法是定死的
        print('item:',item)
        print('spider.name:',spider.name)
        return item  #返回给下一个管道了

# 类名可以随便取，方法的接口需要一致
class NewPipeLine:
    def process_item(self, item, spider):#这个方法是定死的
        item['love']='我爱周杰伦'
        return item  #返回给下一个管道了