import requests
from lxml import etree

url = "http://www.fanyibbs.com/artdetail_32489.html"
response = requests.get(url)
response.encoding = "utf-8"

html = response.text
ele = etree.HTML(html)
book_names = ele.xpath("//div[@class='content']/p/text()")  # 标签筛选规则
s = ''


def remove_upprintable_chars(s):
    return ''.join(x for x in s if x.isprintable())


for book_name in range(len(book_names)):
    s += book_names[book_name] + '\n'
with open('title.txt', 'w') as file:
    file.writelines(s)
print("输入完成")
