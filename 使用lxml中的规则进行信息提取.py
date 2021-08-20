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
# s = ''
print(book_names[0])
print(book_urls[0])
