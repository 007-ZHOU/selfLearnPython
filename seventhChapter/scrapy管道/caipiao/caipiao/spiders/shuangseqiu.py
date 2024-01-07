import scrapy
from caipiao.items import CaiPiaoItem#内部包


class ShuangseqiuSpider(scrapy.Spider):

    def parse(self, response,**kwargs):
        # print(resp.text)
        trs=response.xpath("//tbody[@id='tdata']/tr")
        

        for tr in trs:
            if tr.xpath('./@class').extract_first()=='tdbck':
                continue
            redBall=tr.xpath('./td[@class="chartBall01"]/text()').extract()#红球
            #scrapy支持xpath和css混着用
            # redBall=tr.css(".chartBall01::text").extract()
            # print(redBall)
            blueBall=tr.xpath('./td[@class="chartBall02"]/text()').extract_first()#蓝球
            # print(blueBall)
            qiHao=tr.xpath('./td[@align="center"]/text()').extract_first().strip()
            # print(qiHao)


            cai=CaiPiaoItem()#dic
            cai['qiHao']=qiHao
            cai['redBall']=redBall
            cai['blueBall']=blueBall

            yield cai

        


