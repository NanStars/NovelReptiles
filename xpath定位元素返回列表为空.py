# 这是xpath(绝对路径): /html/body/div[2]/div[3]/div[3]/table/tbody/tr[1]/td[1]/a/text()
import requests
from lxml import etree

url = 'https://yz.chsi.com.cn/sch/'
res = requests.get(url).text
if len(res) > 100:  # 是否解析出text
    print('解析成功')
dom = etree.HTML(res)
text = dom.xpath('/html/body/div[2]/div[3]/div[3]/table/tbody/tr[1]/td[1]/a/text()')
print(text)


# 输出为空
# xpath语法[需要手写]：//*[@class="yxk-table"]/table/tbody/tr[1]/td[1]/a/text()
import requests
from lxml import etree

url='https://yz.chsi.com.cn/sch/'
res=requests.get(url).text
if len(res)>100:#是否解析出text
    print('解析成功')
dom=etree.HTML(res)
text=dom.xpath('//*[@class="yxk-table"]/table/tbody/tr[1]/td[1]/a/text()')
print(text)
#正常解析出文本
