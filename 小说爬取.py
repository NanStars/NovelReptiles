import requests
from lxml import etree
from tqdm import tqdm

with open("chapter.txt", 'r') as file:
    s = file.read()
    # print(s)
s = s.split("\n")

chapter_titles = s[::2]
chapter_urls = s[1::2]


def remove_upprintable_chars(s):
    """移除所有不可见字符"""
    return ''.join(x for x in s if x.isprintable())


o_url = "https://www.xbiquge.la"
# new_url =  o_url +  chapter_urls[0]
pbar = tqdm(range(len(chapter_urls)))
for i in pbar:
    new_url = o_url + chapter_urls[i]

    # print(new_url)
    response = requests.get(new_url)
    response.encoding = "utf-8"
    html = response.text
    # print(html)
    ele = etree.HTML(html)
    book_bodys = ele.xpath("//div[@id='content']/text()")
    # print(book_bodys[0])
    s = "\n" + chapter_titles[i] + "\n"

    for book_body in book_bodys:
        c = "".join(book_body.split())
        c = remove_upprintable_chars(c)
        s += c
    with open("牧神记.txt", "a") as f:
        f.write(s)

print("文章《牧神记》 下载完毕！")
