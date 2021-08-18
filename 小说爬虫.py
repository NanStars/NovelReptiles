import requests
from lxml import etree

print('请输入小说序号')
a = input()
url = "http://www.fanyibbs.com"  # /artdetail_32486.html
path = a
b = '/artdetail_'
c = '.html'
URL = url + b + a + c
# URL = parse.urljoin(url, path)  # 地址拼接
response = requests.get(URL)
response.encoding = "utf-8"  # 编码转换

html = response.text
ele = etree.HTML(html)
# book_neir = ele.xpath("//div[@class='']/div[@class='tablel']/tbody/tr/td/a/@href")
book_names = ele.xpath("//div[@class='content']/p/text()")  # 标签筛选规则

s = ''


def remove_upprintable_chars(t):
    return ''.join(x for x in t if x.isprintable())


print("请输入书籍名字下载")
e = input()
for book_name in range(len(book_names)):
    s += book_names[book_name] + '\n'
with open('{0}.txt'.format(e), 'w', encoding='utf-8') as file:
    file.writelines(s)
print("输入完成")
