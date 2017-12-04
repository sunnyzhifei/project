import unittest
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner
from time import sleep

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get("file:///C:/Users/Administrator/Desktop/login_test.html")
        sleep(3)
    def send_key(self,local,ele,val):
        self.driver.find_element(local,ele).send_keys(val)
    def clickm(self,local,ele):
        self.driver.find_element(local, ele).click()
    def test_login(self):
        f=open("C:/Users/Administrator/Desktop/登录数据.txt")
        x=f.readlines()
        f.close()

        for i in x[1:]:
            l=i.split(" ")
            self.send_key("id","un",l[0])
            sleep(1)
            self.send_key("id","ps",l[1])
            sleep(1)
            self.clickm("id","btlogin")
            sleep(1)
    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    suite=unittest.TestSuite()
    suite.addTest(TestLogin("test_login"))
    fp=open("C:/Users/Administrator/Desktop/test.html","wb")
    runner = HTMLTestRunner(stream=fp,title="自动化测试报告",description="用例执行情况")
    runner.run(suite)
    fp.close()




import xlrd
fp=xlrd.open_workbook("c:/Book1.xls")#打开xls文件
openSheet=fp.sheets()[0]#获得第一个表单的内容
sheetCountNum=openSheet.nrows#获取第一个表的所有的总行数
for i in range(sheetCountNum):#遍历所有的行
    if i==0:
        pass
    else:
        getList=openSheet.row_values(i)#获取单行的值
        print(getList[0],int(getList[1]))#获取单行单列的值