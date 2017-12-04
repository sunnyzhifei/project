# # from selenium import webdriver
# # from time import sleep
# # driver=webdriver.Firefox()
# # #driver.get("http://www.qq.com")
# # driver.get("http://www.baidu.com")
# # #driver.back()
# # #driver.forward()
# # #driver.set_window_size(400,400)
# # driver.find_element_by_id("kw").send_keys("TEST")
# # driver.find_element_by_id("su").click()
# # driver.maximize_window()
# # #driver.refresh()
# #
# # sleep(5)
# # #driver.quit()
# # #driver.close()
#
#



# # from selenium import webdriver
# # from time import sleep
# # driver=webdriver.Firefox()
# # driver.get("http://mail.126.com ")
# # sleep(5)
# # driver.switch_to_frame("x-URS-iframe")
# # driver.find_element_by_xpath("//input[@name='email']").send_keys("lizhifei")
# # sleep(3)
# # driver.find_element_by_xpath("//input[@name='password']").send_keys("123456")
# # sleep(3)
# # driver.find_element_by_id("dologin").click()
#
#



# from selenium import webdriver
# from time import sleep
#
# driver = webdriver.Firefox()
# driver.get("https://www.jd.com/")
# sleep(5)
# driver.find_element_by_link_text("免费注册").click()
# sleep(5)
# driver.find_element_by_xpath("//button[contains(@style,'display')]").click()
# driver.find_element_by_id("form-account").send_keys("11011011011")
# driver.find_element_by_id("form-pwd").send_keys("11011011011abc")
# driver.find_element_by_id("form-equalTopwd").send_keys("11011011011abc")
# driver.find_element_by_id("form-phone").send_keys("18980809005")
# driver.find_element_by_id("authCode").send_keys("4vss")
# driver.find_element_by_id("phoneCode").send_keys("8888")
# driver.find_element_by_class_name("btn-register").submit()
#
#




# from selenium import webdriver
# from time import sleep
## driver = webdriver.Firefox()
# driver.get("https://tieba.baidu.com/index.html")
# sleep(10)
# driver.find_element_by_link_text("高级搜索").click()
# sleep(5)
#
# driver.find_element_by_xpath("//input[contains(@name,'kw')]").send_keys("汇智")
# driver.find_element_by_xpath("//input[contains(@name,'qw')]").send_keys("动力")
# driver.find_element_by_xpath("//input[contains(@name,'un')]").send_keys("动力")
#
# driver.find_element_by_css_selector(".wrap2>form>table>tbody>tr>td>select>option").click()


# from selenium import webdriver
# from time import sleep
# driver = webdriver.Ie()
# driver.get("http://localhost/login_test.html")
# driver.find_element_by_css_selector("input[name=username]").send_keys("test6")
# driver.find_element_by_css_selector("input[name$=name]").send_keys("test7")
# driver.find_element_by_css_selector("input[name^=user]").send_keys("test8")
# sleep(3)
# print(driver.find_element_by_css_selector("tbody:contains['用户']").text)




# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# import logging
# from time import sleep
# driver=webdriver.Firefox()
# driver.get("http://www.baidu.com/ ")
# #sleep(3)
# logging.basicConfig(level=logging.DEBUG,
#                 format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                 datefmt='%a, %d %b %Y %H:%M:%S',
#                 filename='d://myapp.log',
#                 filemode='w')
#
# logging.warning("test")
# def deco(func):
#     def test():
#         logging.info ("enter {}()".format(func.__name__))
#         func()
#     return test
# @deco
# def send_input():
#     driver.find_element_by_id("kw").send_keys("test")
# send_input()



# from selenium import webdriver
# from time import sleep
# driver = webdriver.Ie()
# driver.get("http://localhost/login_test.html")
# k=driver.find_elements_by_tag_name("input")
# for i in k:
#     i.send_keys("test")


# from selenium import webdriver
# from time import sleep
# driver = webdriver.Chrome()
# driver.get("https://tieba.baidu.com/index.html")
# sleep(10)
# driver.find_element_by_link_text("高级搜索").click()
# sleep(5)
# driver.find_element_by_xpath("//select[@name='sm']").find_element_by_xpath("//option[@value='2']").click()


#
# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
#
# driver = webdriver.Ie()
# driver.get("https://www.baidu.com/")
# #driver.set_window_size(400,400)
# baidu=driver.current_window_handle
# print('百度的句柄:%s' %baidu)
# sleep(3)
# tb=driver.find_element_by_link_text("贴吧")
# ActionChains(driver).context_click(tb).perform()
# for i in range(3):
#     ActionChains(driver).send_keys(Keys.DOWN).perform()
#     sleep(1)
# tb.send_keys(Keys.ENTER)
# sleep(5)
# all=driver.window_handles
# print("所有句柄%s" %all)
# driver.switch_to_window(baidu)
# driver.find_element_by_id("kw").send_keys("test")
# driver.switch_to_window(all[1])
# driver.find_element_by_id("wd1").send_keys("test")
#
# from selenium.webdriver.support.select import Select


#练习题
# from time import sleep
# from selenium import webdriver
# driver=webdriver.Ie()
# driver.get("http://www.zhiizhii.com/")
# sleep(5)
# driver.find_element_by_link_text("注册").click()
# sleep(3)
# driver.find_element_by_id("InputEmail").send_keys("5164973416")
#
# driver.find_element_by_name("password").send_keys("5164973416")
#
# driver.find_element_by_xpath("//input[@id='InputName']").send_keys("32432534")
#
# driver.find_element_by_xpath("//input[contains(@placeholder,'职位')]").send_keys("sadadadasd")
#
# for i in range(2):
#     driver.find_element_by_name("agree").click()
# driver.find_element_by_xpath(".//*[@id='register-form']/input[3]").click()





# import unittest
# from selenium import webdriver
# from time import sleep
#
# class Test(unittest.TestCase):
#     def setUp(self):
#             self.driver = webdriver.Ie()
#     def test_baidu(self):
#         self.driver.get("http://www.baidu.com/")
#         sleep(5)
#         self.send_keys("id","kw","test")
#         sleep(5)
#     def send_keys(self,local,ele,value):
#         self.driver.find_element(local,ele).send_keys(value)
#     def tearDown(self):
#         self.driver.quit()
#
# if __name__ == '__main__':
#     unittest.main()














#
# import unittest
# from selenium import webdriver
# from HTMLTestRunner import HTMLTestRunner
#
# class Test(unittest.TestCase):
#     def setUp(self):  # 重写setUp方法-----》该方法属于初始化方法
#         self.driver = webdriver.Ie()
#
# def test_baiduSend(self):
#     self.driver.get("http://www.baidu.com/")
#     self.send_key("id", "kw", "test_baiduSend")
#     sValue = self.driver.find_element_by_id("kw").get_attribute("value")
#     self.assertEqual("test", sValue)
#     self.assertDictEqual({"name": "andy"}, {"name": "andy"})
#     self.assertFalse(False)
#
# def test_baiduSend1(self):
#     self.driver.get("http://www.baidu.com/")
#     self.send_key("id", "kw", "test_baiduSend1")
#     sValue = self.driver.find_element_by_id("kw").get_attribute("value")
#     self.assertEqual("test", sValue)
#     self.assertDictEqual({"name": "andy"}, {"name": "andy"})
#     self.assertFalse(False)
#
# def test_baiduSend2(self):
#     self.driver.get("http://www.baidu.com/")
#     self.send_key("id", "kw", "test_baiduSend2")
#     sValue = self.driver.find_element_by_id("kw").get_attribute("value")
#     self.assertEqual("test", sValue)
#     self.assertDictEqual({"name": "andy"}, {"name": "andy"})
#     self.assertFalse(False)
#
#
# def send_key(self, local, ele, value):
#     self.driver.find_element(local, ele).send_keys(value)
#
# def tearDown(self):  # 清除环境的方法
#     self.driver.quit()
#
# if __name__ == '__main__':
#     suite1 = unittest.TestSuite(tests=[Test('test_baiduSend1'), Test('test_baiduSend2')])
#     suite = unittest.TestSuite(tests=(suite1, Test('test_baiduSend')))
#     fp=open("./test.html","wb")
#     runner = HTMLTestRunner(stream=fp,title="自动化测试报告",description="用例执行情况")
#     runner.run(suite)









# import unittest
# from selenium import webdriver
# from HTMLTestRunner import HTMLTestRunner
# from time import sleep
#
# class TestLogin(unittest.TestCase):
#     def setUp(self):
#         self.driver=webdriver.Chrome()
#         self.driver.get("file:///C:/Users/Administrator/Desktop/login_test.html")
#         sleep(3)
#     def send_key(self,local,ele,val):
#         self.driver.find_element(local,ele).send_keys(val)
#     def clickm(self,local,ele):
#         self.driver.find_element(local, ele).click()
#     def test_login(self):
#         f=open("C:/Users/Administrator/Desktop/登录数据.txt")
#         x=f.readlines()
#         f.close()
#
#         for i in x[1:]:
#             l=i.split(" ")
#             self.send_key("id","un",l[0])
#             sleep(1)
#             self.send_key("id","ps",l[1])
#             sleep(1)
#             self.clickm("id","btlogin")
#             sleep(1)
#     def tearDown(self):
#         self.driver.quit()
#
# if __name__=="__main__":
#     suite=unittest.TestSuite()
#     suite.addTest(TestLogin("test_login"))
#     fp=open("C:/Users/Administrator/Desktop/test.html","wb")
#     runner = HTMLTestRunner(stream=fp,title="自动化测试报告",description="用例执行情况")
#     runner.run(suite)
#     fp.close()







# import xlrd
# fp=xlrd.open_workbook("c:/Book1.xls")#打开xls文件
# openSheet=fp.sheets()[0]#获得第一个表单的内容
# sheetCountNum=openSheet.nrows#获取第一个表的所有的总行数
# for i in range(sheetCountNum):#遍历所有的行
#     if i==0:
#         pass
#     else:
#         getList=openSheet.row_values(i)#获取单行的值
#         print(getList[0],int(getList[1]))#获取单行单列的值




# import time
# from selenium import webdriver
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# def host():
#     t={"http://192.168.8.75:5555/wd/hub ":'chome',"http://192.168.8.75:4444/wd/hub ":'chome'}
#     return t
# for host,nav in host().items():
#     driver=webdriver.Remote(command_executor=host,desired_capabilities={'browserName': nav,'' 'platform': 'WINDOWS'})
#     driver.get("http://www.baidu.com")


