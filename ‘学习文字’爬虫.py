# 负责连接网站处理http 协议
import requests
import sys
import time
import pyttsx3

from lxml import etree

print('请输入小说序号')
a = input()
url = "http://www.fanyibbs.com"  # /artdetail_32486.html
path = a
b = '/artdetail_324'
c = '.html'
URL = url + b + a + c
# URL = parse.urljoin(url, path)  # 地址拼接
response = requests.get(URL)
response.encoding = "utf-8"  # 编码转换

html = response.text  # 获取网页源代码
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
print('开始下载')


# 进度条
def progress_bar():
    for io in range(1, 101):
        print("\r", end="")
        print("Download progress: {}%: ".format(io), "▋" * (io // 2), end="")
        sys.stdout.flush()
        time.sleep(0.05)
        print()


progress_bar()
print('下载完成，开始阅读')


def talkWith(engine, line):
    """ 朗读内容 """
    engine.say(line)
    engine.runAndWait()


def talkContent(line):
    """ 朗读字符串内容 使用系统文字转语音 """

    engine = pyttsx3.init()
    # 设置朗读速度
    engine.setProperty('rate', 160)
    # 如果字符串过长 通过句号分隔 循环读取
    if len(line) > 20:
        con_list = line.split('。')
        for item in con_list:
            time.sleep(1)
            talkWith(engine, item)
    else:
        talkWith(engine, line)


# 打开名为1.txt的文件并且读取
content = open('{0}.txt'.format(e), 'r', encoding='utf-8')
line = content.read()

talkContent(line)
print('阅读结束，十秒后关闭')


# 十秒钟倒计时
def jindut_a():
    for i in range(10, 0, -1):
        print(i)
        time.sleep(1)


jindut_a()
print('程序退出')
