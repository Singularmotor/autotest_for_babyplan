#coding=utf-8
from selenium import webdriver
import pymysql
import unittest,time

print("test13")
wf = webdriver.Firefox()

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
#BD_13
wf.find_element_by_id("playLi").click()
wf.find_element_by_xpath(".//*[@id='div0']/a/p").click()
try:
    n=wf.find_element_by_class_name("firstP").text
except:
    print("fail")
if n=="愿望":
    print("pass")
else:
    print("fail")
wf.close()

if __name__ == "__main__":
    unittest.main()
