#coding=utf-8
from selenium import webdriver
import time
import pymysql

wf = webdriver.Firefox()
#check the function of login
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

def login():
    wf.get("http://192.168.17.33:8080/BabyPlan/login.jsp")  # connect the web
    wf.implicitly_wait(2)
    wf.find_element_by_id("userName").send_keys("test")  # input username
    time.sleep(1)
    wf.find_element_by_id("password").send_keys("test11")  # type in password
    time.sleep(1)
    wf.find_element_by_id("loginbtn").click()  # complete the login
    time.sleep(1)
    return

logind("test","test11",1) #BD_01
logind("test","test",0) #BD_02
logind("test456","test11",0) #BD_03
logind("testqqq","tesssss",0) #BD_04

#BD_05
ps=pymysql
bp=ps.connect(host='192.168.17.33',port=3306,user='root',passwd='123123',db='babyplan',charset='utf8')
#connect to the database ,if you want to use chinese in you request on pymysql, please type charset='utf8' at last
res=bp.cursor()
res.execute("UPDATE userinfo SET password = '123123' WHERE userName = 'test'")
#mission for the database
bp.commit()
time.sleep(1)
#res.execute("")
#print(r1)
logind("test","123123",1)
res.execute("UPDATE userinfo SET password = 'test11' WHERE userName = 'test'")
#reset the password
bp.commit()
time.sleep(1)
#BD_05

#register function tests are delayed in delayfunction_register.py

login()
#BD_13
wf.find_element_by_id("playLi").click()
wf.find_element_by_xpath(".//*[@id='div0']/a/p").click()
wf.find_element_by_xpath("html/body/div[1]/div[1]/a").click()
#BD_14
wf.find_element_by_xpath(".//*[@id='musicCarousel']/div/div[1]/div/div[1]/a/img").click()




