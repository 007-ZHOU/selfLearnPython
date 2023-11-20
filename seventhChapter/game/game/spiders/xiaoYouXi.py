import scrapy


class XiaoyouxiSpider(scrapy.Spider):
    name = "xiaoYouXi"#爬虫名字
    allowed_domains = ["4399.com"]#允许的域名
    start_urls = ["http://www.4399.com/flash/"]#起始页面url

    def parse(self, response):#该方法默认是用来处理解析的 
        print(response)
        # print(self)
        #拿到页面源代码
        # print(response.text)
        #提取数据
        # response.json()
        # response.xpath()
        # response.css()#css选择器

        #获取到页面中所有的游戏名字
        text=response.xpath('//ul[@class="n-game cf"]/li/a/b/text()').extract()#提取内容
        # print(text)

        #分块提取
        li_list=response.xpath('//ul[@class="n-game cf"]/li')
        for li in li_list:
            name=li.xpath('./a/b/text()').extract_first()#extract_first()提取一项，没有不会报错
            categroy=li.xpath('./em/a/text()').extract_first()
            data=li.xpath('./em/text()').extract_first()
            dic={
                "name":name,
                "categroy":categroy,
                "data":data
            }
            

            #需要用yield将数据传递给管道de
            yield dic #省内存,不需要列表；如果返回的是数据。直接可以认为是给了管道pipeline
        

