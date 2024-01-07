import requests
from lxml import etree
import execjs

cookies = {
    '_ga': 'GA1.1.1545732235.1701918936',
    '__gads': 'ID=a64dab1706b39a4f:T=1701918936:RT=1701923849:S=ALNI_MbDLFBKvUK4U454o6bwb7jrlrHNYA',
    '__gpi': 'UID=00000d1608f535a3:T=1701918936:RT=1701923849:S=ALNI_MY6RiQ0sYxqgy68QFR4Roz-zeUN6g',
    '_ga_QDQFF6KFGD': 'GS1.1.1701922095.2.1.1701923849.0.0.0',
}

headers = {
    'authority': 'www.proxynova.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7',
    'cache-control': 'no-cache',
    # 'cookie': '_ga=GA1.1.1545732235.1701918936; __gads=ID=a64dab1706b39a4f:T=1701918936:RT=1701923849:S=ALNI_MbDLFBKvUK4U454o6bwb7jrlrHNYA; __gpi=UID=00000d1608f535a3:T=1701918936:RT=1701923849:S=ALNI_MY6RiQ0sYxqgy68QFR4Roz-zeUN6g; _ga_QDQFF6KFGD=GS1.1.1701922095.2.1.1701923849.0.0.0',
    'pragma': 'no-cache',
    'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
}

resp = requests.get('https://www.proxynova.com/proxy-server-list/country-us/', cookies=cookies, headers=headers)
print(resp.status_code)
tree =etree.HTML(text=resp.text)
# //*[@id="tbl_proxy_list"]/tbody/tr[1]/td[1]/abbr/script
# //*[@id="tbl_proxy_list"]/tbody/tr[2]/td[1]/abbr/script/text()
# //*[@id="tbl_proxy_list"]/tbody/tr[3]/td[1]/script/text()
for i in range(20):

    text=tree.xpath(f'//*[@id="tbl_proxy_list"]/tbody/tr[{i+1}]/td[1]//script/text()')
    try:
        print(text[0])
        import re
        # 原始字符串
        original_string =text[0]
    #     # 使用正则表达式去除函数字符串
    #     modified_string = re.sub(r'document\.write\((.*?)\)', r'\1', original_string)
    #     print('modified_string',modified_string)
    #     # print(eval(modified_string))
    #     ctx = execjs.compile('''
    #     function test(str) {
    #                 return str;
    #     }
    # ''')
    #     result = ctx.call('test',original_string)
    #     print('result',result)  

        # 用正则表达式提取函数字符串
        function_match = re.search(r'document.write\((.*?)\)', original_string)
        if function_match:
            function_string = function_match.group(1)
            
            # 使用eval执行提取的函数字符串
            result = eval(function_string)

            print('result:',result)
        else:
            print("No function string found in the original string")
    except:
        print('error')
        continue
