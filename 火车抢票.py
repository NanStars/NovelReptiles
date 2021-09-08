import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
a = input("出发地")
b = input("目的地")
c = input("出发时间(格式必须是M-d的方式)")
d = input("列车号")
e = input("乘车人")
class Qiangpiao():
    def __init__(self, from_station, to_station, depart_time, train_num, passenger):
        self.login_url = 'https://kyfw.12306.cn/otn/resources/login.html'
        self.init_my_url = 'https://kyfw.12306.cn/otn/view/index.html'
        self.order_url = 'https://kyfw.12306.cn/otn/confirmPassenger/initDc'
        # input("出发地：")
        self.from_station = from_station
        # input("目的地：")
        self.to_station = to_station
        # 时间格式必须是M-d的方式
        # input("出发时间(格式必须是M-d的方式)：")
        self.depart_time = depart_time
        # input("列车号：")
        self.train_num = train_num
        self.passenger = passenger
        # 获取当前月份
        self.now_month = datetime.date.today().month

        self.leave_month = int(self.depart_time.split('-')[0])
        self.leave_day = int(self.depart_time.split('-')[1])

        self.driver = webdriver.Chrome()

    def _login(self):
        self.driver.get(self.login_url)
        # 窗口最大化
        # self.driver.maximize_window()
        # 设置窗口大小
        self.driver.set_window_size(1300, 800)
        # print('调整前尺寸:', self.driver.get_window_size())
        # 显式等待
        # 这里进行手动登录，可以扫码，也可以输入账号密码点击登录
        WebDriverWait(self.driver, 1000).until(EC.url_to_be(self.init_my_url))
        print('登录成功！')

    def _pop_window(self):
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@class="dzp-confirm"]/div[2]/div[3]/a').click()

    def _enter_order_ticket(self):
        action = ActionChains(self.driver)
        element = self.driver.find_element_by_link_text('车票')
        # 鼠标移动到 '车票' 元素上的中心点
        action.move_to_element(element).perform()
        # 点击'单程'
        self.driver.find_element_by_xpath('//*[@id="J-chepiao"]/div/div[1]/ul/li[1]/a').click()
        # 消除第二次弹窗
        self.driver.find_element_by_link_text('确认').click()

    def _search_ticket(self):
        # 出发地输入
        self.driver.find_element_by_id("fromStationText").click()
        self.driver.find_element_by_id("fromStationText").send_keys(self.from_station)
        self.driver.find_element_by_id("fromStationText").send_keys(Keys.ENTER)
        # 目的地输入
        self.driver.find_element_by_id("toStationText").click()
        self.driver.find_element_by_id("toStationText").send_keys(self.to_station)
        self.driver.find_element_by_id("toStationText").send_keys(Keys.ENTER)
        # 出发日期输入
        self.driver.find_element_by_id("date_icon_1").click()
        if self.leave_month == self.now_month:
            xpath_str = f"//div[37]/div[1]/div[2]/div[{self.leave_day}]/div"  # //*[@id="toolbar_Div"]/div[37]/div[1]/div[2]/div[10]/div
            if EC.element_to_be_clickable(
                    (By.XPATH, xpath_str)):  # //*[@id="toolbar_Div"]/div[37]/div[1]/div[2]/div[8]/div
                self.driver.find_element_by_xpath(xpath_str).click()
            else:
                print("当前日期未到或已过售票日期，无法购票！")
        elif self.leave_month == self.now_month + 1:
            xpath_str = f"//div[37]/div[1]/div[2]/div[{self.leave_day}]/div"
            if EC.element_to_be_clickable((By.XPATH, xpath_str)):
                self.driver.find_element_by_xpath(xpath_str).click()
            else:
                print("当前日期未到或已过售票日期，无法购票！")
        else:
            print("月份超前一个月以上，无法购票！")
        # 等待查询按钮是否可用
        WebDriverWait(self.driver, 1000).until(EC.element_to_be_clickable((By.ID, "query_ticket")))
        # 执行点击事件
        search_btn = self.driver.find_element_by_id("query_ticket")
        search_btn.click()
        # 等待查票信息加载
        WebDriverWait(self.driver, 1000).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="queryLeftTable"]/tr')))

    def _order_ticket(self):
        train_num_list = []
        train_num_ele_list = self.driver.find_elements_by_xpath('//tr/td[1]/div/div[1]/div/a')
        for t in train_num_ele_list:
            train_num_list.append(t.text)
        tr_list = self.driver.find_elements_by_xpath('//*[@id="queryLeftTable"]/tr[not(@datatran)]')
        if self.train_num in train_num_list:

            for tr in tr_list:
                train_num = tr.find_element_by_xpath("./td[1]/div/div[1]/div/a").text
                if self.train_num == train_num:
                    # 动车二等座余票信息
                    text_1 = tr.find_element_by_xpath("./td[4]").text
                    # 火车二等座余票信息
                    text_2 = tr.find_element_by_xpath("./td[8]").text
                    if (text_1 == "有" or text_1.isdigit()) or (text_2 == "有" or text_2.isdigit()):
                        # 点击预订按钮
                        order_btn = tr.find_element_by_class_name("btn72")
                        order_btn.click()
                        # 等待订票页面
                        WebDriverWait(self.driver, 1000).until(EC.url_to_be(self.order_url))
                        # 选定乘车人
                        self.driver.find_element_by_xpath(
                            f'//*[@id="normal_passenger_id"]/li/label[contains(text(),"{self.passenger}")]').click()
                        # 提交订单
                        self.driver.find_element_by_id('submitOrder_id').click()
                        time.sleep(2)
                        # 点击确认
                        self.driver.find_element_by_id('qr_submit_id').click()
                        #座位选择//*[@id="1A"]
                        self.driver.find_element_by_id('1A')
                        print("购票成功！")
                        break

                    print("二等座无票！")
        else:

            print("无此列车！")

    def run(self):
        # 登录
        self._login()
        # 消除登录后（第一次）的弹窗
        self._pop_window()
        # 进入购票页面
        self._enter_order_ticket()
        # 查票
        self._search_ticket()
        # 订票
        self._order_ticket()
        # 关闭浏览器
        time.sleep(6)
        self.driver.quit()


if __name__ == '__main__':
    qiangpiao = Qiangpiao(a, b, c, d, e)
    qiangpiao.run()
# 出发地 目的地 9-19 列车号 name
