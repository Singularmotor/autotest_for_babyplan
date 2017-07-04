#coding=utf-8
from selenium import webdriver
import pymysql
import unittest,time

print("test28")
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
wf.find_element_by_id("parentLi").click()
wf.find_element_by_xpath(".//*[@id='myTab']/li[3]/a").click()
wf.find_element_by_xpath(".//*[@id='uploadExperienceForm']/div[1]/table/tbody/tr[1]/td[2]/input").send_keys("宝宝06")
wf.find_element_by_xpath(".//*[@id='uploadExperienceForm']/div[1]/table/tbody/tr[3]/td/div/div[2]").send_keys(" ")
wf.find_element_by_xpath(".//*[@id='uploadExperienceForm']/div[2]/button").click()
time.sleep(1)
try:
    wf.find_element_by_xpath(".//*[@id='uploadExperienceForm']/div[2]/button").click()
except:
    n=1
res.execute("SELECT eTitle,eContent FROM experience WHERE eTitle='宝宝06'")
mm=res.fetchone()
if mm==('宝宝06',' ') :
    print("fail")
elif n==0:
    print("pass")
wf.close()
if __name__ == "__main__":
    unittest.main()
