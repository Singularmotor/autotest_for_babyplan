#coding=utf8
from selenium import webdriver
import time,os
import pymysql
import HTMLTestRunner
import unittest

wf = webdriver.Firefox()
ps=pymysql
bp=ps.connect(host='192.168.17.33',port=3306,user='root',passwd='123123',db='babyplan',charset='utf8')
#connect to the database ,if you want to use chinese in you request on pymysql, please type charset='utf8' at last
res=bp.cursor()

def logind(lun,lpwd,dd):
    #lun==username lpwd==password  dd is a way to identify the reports' types(except pass=1, except fail=0)
    a=0 #reset "a"
    wf.get("http://192.168.17.33:8080/BabyPlan/login.jsp") #connect the web
    wf.implicitly_wait(2)
    wf.find_element_by_id("userName").send_keys(lun) #input username
    time.sleep(1)
    wf.find_element_by_id("password").send_keys(lpwd) #type in password
    time.sleep(1)
    wf.find_element_by_id("loginbtn").click() #complete the login
    time.sleep(1)
    if dd==1:
        try:
            wf.find_element_by_xpath("html/body/div[1]/div[2]/p/a").click() #loginout
        except:
            print("fail")
            a=1
        if a!=1:
            print("pass")
    else:
        try:
            wf.find_element_by_xpath("html/body/div[1]/div[2]/p/a").click() #loginout
        except:
            print("pass")
            a=1
        if a!=1:
            print("fail")

def login_guest01():
    wf.get("http://192.168.17.33:8080/BabyPlan/login.jsp")  # connect the web
    wf.implicitly_wait(2)
    wf.find_element_by_id("userName").send_keys("test")  # input username
    time.sleep(1)
    wf.find_element_by_id("password").send_keys("test11")  # type in password
    time.sleep(1)
    wf.find_element_by_id("loginbtn").click()  # complete the login
    time.sleep(1)
    return

def login_guest02():
    wf.get("http://192.168.17.33:8080/BabyPlan/login.jsp")  # connect the web
    wf.implicitly_wait(2)
    wf.find_element_by_id("userName").send_keys("yzx")  # input username
    time.sleep(1)
    wf.find_element_by_id("password").send_keys("123456")  # type in password
    time.sleep(1)
    wf.find_element_by_id("loginbtn").click()  # complete the login
    time.sleep(1)
    return

def login_admin():
    wf.get("http://192.168.17.33:8080/BabyPlan/login.jsp")  # connect the web
    wf.implicitly_wait(2)
    wf.find_element_by_id("userName").send_keys("admin")  # input username
    time.sleep(1)
    wf.find_element_by_id("password").send_keys("admin11")  # type in password
    time.sleep(1)
    wf.find_element_by_id("loginbtn").click()  # complete the login
    time.sleep(1)
    return

def reg():
    pass

def send_report(testreport):
    result_dir = testreport
    lists = os.listdir(result_dir)
    lists.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn))
    print(u'最新测试报告：'+lists[-1])
    #找到最新文件
    file_new = os.path.join(result_dir,lists[-1])
    print(file_new)

def creatsuite():
    testunit = unittest.TestSuite()
    #定义测试文件查找的目录
    test_dir = '.\\test_case'
    #定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py',top_level_dir=None)
    #discover方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print(testunit)
    return testunit


if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    # 定义测试报告路径及文件名
    testreport = "C:\\Users\\ETC\\Desktop\\babyplan\\auto_test\\report\\"
    filename = testreport + now + '_test126_project_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'宝贝计划用例',
        description=u'用例执行情况：'
    )
    #执行测试
    alltestnames = creatsuite()
#    runner = unittest.TextTestRunner()
    runner.run(alltestnames)
    fp.close()

