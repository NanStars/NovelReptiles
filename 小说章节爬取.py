import requests
from lxml import etree

with open("title.txt", 'r') as file:
    s = file.read()
    # print(s)
s = s.split("\n")

title = s[0]
url = s[1]
# print(title)
# print(url)
response = requests.get(url)
response.encoding = "utf-8"
html = response.text
# print(html)
ele = etree.HTML(html)
book_chapters = ele.xpath("//div[@class='box_con']/div[@id='list']/dl/dd/a/text()")
# book_author = ele.xpath("")
book_c_urls = ele.xpath("//div[@class='box_con']/div[@id='list']/dl/dd/a/@href")

s = ""
for book_chapter in range(len(book_chapters)):
    s += book_chapters[book_chapter] + "\n" + book_c_urls[book_chapter] + "\n"
with open("chapter.txt", "w") as f:
    f.write(s)
print("输入完成！")
