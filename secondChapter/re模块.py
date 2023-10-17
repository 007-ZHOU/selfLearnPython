import re

lst=re.findall(pattern=r'\d+',string='我的电话号码是10086')
print(lst)


#finditer,匹配字符串中所有的内容（返回的是迭代器）,效率更高
lst1=re.finditer(pattern=r'\d+',string='我的电话号码是10086')

for  i in lst1:
    print(i.group())

