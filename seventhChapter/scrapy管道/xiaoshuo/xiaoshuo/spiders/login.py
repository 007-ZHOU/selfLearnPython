import scrapy

 
class LoginSpider(scrapy.Spider):
    name = "login"
    allowed_domains = ["17k.com"]
    start_urls = ["https://user.17k.com/www/"]

    """
    需要重新定义一下，scrapy原来对于start_urls的处理
    只需要重写start_requests()方法即可
    """
    def start_requests(self):

        #用cookies登录
        """
        cookie_str=r"
GUID=aff1e857-6788-42cb-ab93-9c80118fbe6c; c_channel=0; c_csc=web; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22aff1e857-6788-42cb-ab93-9c80118fbe6c%22%2C%22%24device_id%22%3A%2218b5a092bb09d3-0b6c953bd160a7-745d5771-1327104-18b5a092bb11433%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22aff1e857-6788-42cb-ab93-9c80118fbe6c%22%7D; Hm_lvt_9793f42b498361373512340937deb2a0=1701003187; Hm_lpvt_9793f42b498361373512340937deb2a0=1701003265
"
        lst=cookie_str.split('; ')
        dic={}
        for item in lst:
            k,v=item.split('=')
            dic[k.strip()]=v.strip()
        print(dic)
        yield scrapy.Request(
            url=self.start_urls[0],
            cookies=dic,
            # callback=self.parse(),
        )
        """

        #输入账号密码登陆

        urlLogin='https://passport.17k.com/ck/user/login'
        userName='19857181251'
        password='aqz145...'
        #发送post请求的第一种方案，不好
        yield scrapy.Request(
            url=urlLogin,
            method='post',
            body=f'loginName={userName}&password={password}',
            callback=self.parse,
        )

    def parse(self, response):
        yield scrapy.Request(url=LoginSpider.start_urls[0],callback=self.parse_detail)

    def parse_detail(self,response):
        print(response.text)

