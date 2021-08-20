import requests
from lxml import etree

url = "https://www.xbiquge.la/xiaoshuodaquan/"
response = requests.get(url)
response.encoding = "utf-8"

html = response.text
# ele
ele = etree.HTML(html)
book_names = ele.xpath("//div[@id='main']/div[@class='novellist']/ul/li/a/text()")
book_urls = ele.xpath("//div[@id='main']/div[@class='novellist']/ul/li/a/@href")
s = ''
for book_name in range(len(book_names)):
    s += book_names[book_name] + '\n' + book_urls[book_name] + '\n'
with open('title.txt', 'w') as file:
    file.writelines(s)
print("输入完成")
