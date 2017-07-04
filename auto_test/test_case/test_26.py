#coding=utf-8
from selenium import webdriver
import pymysql
import unittest,time

print("test26")
wf = webdriver.Firefox()
ps=pymysql
bp=ps.connect(host='192.168.17.33',port=3306,user='root',passwd='123123',db='babyplan',charset='utf8')
#connect to the database ,if you want to use chinese in you request on pymysql, please type charset='utf8' at last
res=bp.cursor()

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

login_guest01()
n=0
mm=0
try:
    wf.find_element_by_id("parentLi").click()
    wf.find_element_by_xpath(".//*[@id='myTab']/li[3]/a").click()
    wf.find_element_by_xpath(".//*[@id='uploadExperienceForm']/div[1]/table/tbody/tr[1]/td[2]/input").send_keys("宝宝")
    wf.find_element_by_xpath(".//*[@id='uploadExperienceForm']/div[1]/table/tbody/tr[3]/td/div/div[2]").send_keys("你好")
    wf.find_element_by_xpath(".//*[@id='uploadExperienceForm']/div[2]/button").click()
except:
    print("fail")
    n=1
try:
    res.execute("SELECT eTitle,eContent FROM experience WHERE eTitle='宝宝' AND eContent='你好'")
    mm=res.fetchone()
except:
    print("fail")
    n=1
if n==0 and mm==('宝宝','你好'):
    print("pass")
elif n!=1:
    print("fail")
wf.close()

if __name__ == "__main__":
    unittest.main()
