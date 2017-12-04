#导入驱动模块

from selenium import webdriver
import time
#打开网址
driver=webdriver.Chrome()

#设置窗口大小
#driver.set_window_size(1080,900)
#等待10秒
driver.implicitly_wait(10)

#打开网址
driver.get("https://kyfw.12306.cn/otn/login/init")
time.sleep(2)
#
#点击登录
driver.find_element_by_id("login_user").click()
time.sleep(2)
#输入用户名
driver.find_element_by_id("username").send_keys("Lizhifei")
time.sleep(2)
#输入密码
driver.find_element_by_id("password").send_keys("lizhifei123456")
#
#半自动化
input("请点击选取验验证码图片，并点击回车继续\n")

driver.find_element_by_id("loginSub").click()

time.sleep(2)
#点击车票预订
driver.find_element_by_link_text(u"车票预订").click()

time.sleep(1)

#点击出发站
driver.find_element_by_id("fromStationText").click()

# 浏览器console设置窗口抓取 setTimeout(function(){debugger;},5000)
time.sleep(1)
#出发站点击成都
driver.find_element_by_css_selector(u"[title=天津]").click()
time.sleep(1)
#点击到达站
driver.find_element_by_id("toStationText").click()

# 浏览器console设置窗口抓取 setTimeout(function(){debugger;},5000)
time.sleep(1)
#到达站点击天津
driver.find_element_by_css_selector(u"[title=北京]").click()
time.sleep(1)
#点击出发时间
driver.find_element_by_id("train_date").click()
time.sleep(1)
#选择时间：
driver.find_element_by_css_selector(
    u'body > div.cal-wrap > div:nth-child(1) > div.cal-cm > div:nth-child(21) > div').click()
time.sleep(1)

driver.find_element_by_css_selector("#_ul_station_train_code > li:nth-child(1)").click()

time.sleep(1)
#点击查询
driver.find_element_by_id("query_ticket").click()

zuowei=driver.find_element_by_id("ZE_25000C20020I")
zuowei.click()

while True:
    try:
        if zuowei.text in ("无","--"):
            print("暂时无票，继续查询")
            time.sleep(1)
        else:
            print("有票，购买")
            #点击预订按钮
            driver.find_element_by_link_text("预订").click()
            #选择乘客
            driver.find_element_by_id("normalPassenger_0").click()
            #点击提交按钮
            driver.find_element_by_id("submitOrder_id").click()
            break
    except:
        pass
