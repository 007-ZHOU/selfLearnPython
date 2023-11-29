# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

from caipiao.settings import MSQL

"""
存储数据的方案
1.数据要存储在csv文件中
2.数据存储在mysql数据库中
3.数据存储在mongodb数据库中
4.文件的存储
"""

class CaipiaoPipeline:
    """
    我们希望的是，在爬虫开始的时候，打开这个文件
    在执行过程中，不断的往里存储数据
    在执行完毕时，关掉这个文件
    """

    def open_spider(self,spider):#固定的函数名
        print('我要开始了，注意，小心点')
        self.f=open(file='./双色球.csv',mode='a',encoding='utf-8')
    def close_spider(self,spider):#固定的函数名
        print('我要结束了')
        if self.f:
            self.f.close()

    def process_item(self, item, spider):
        self.f.write(f"{item['qiHao']},{'_'.join(item['redBall'])},{item['blueBall']}\n")
        return item


class CaiPiaoMySQLPipeline:

    def open_spider(self,spider):#固定的函数名
        self.conn=pymysql.connect(
            host=MSQL['host'],
            port=MSQL['port'],
            user=MSQL['user'],
            password=MSQL['password'],
            database=MSQL['database']
        )

    def close_spider(self,spider):#固定的函数名
        if self.conn:
            self.conn.close()


    def process_item(self, item, spider):
        try:
            cursor=self.conn.cursor()
            sql='insert into caipiao (id,qiHao,redBall,blueBall) values (%s,%s,%s,%s)'
            cursor.execute(sql,(item['qiHao'],item['qiHao'] ,'_'.join(item['redBall'] ),item['blueBall']))
            self.conn.commit()
        except:
            self.conn.rollback()
        finally:
            if cursor:
                cursor.close()
        return item


