from urllib import parse

url = 'https://blog.csdn.net'  # 主址
a = input()  # 自定义结尾拼接
path = a
URL = parse.urljoin(url, path)  # 主网址在前   url+path
print(URL)
