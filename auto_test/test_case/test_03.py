#coding=utf-8
from selenium import webdriver
import pymysql
import unittest,time

print("test03")
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

logind("test456","test11",0)
wf.close()

if __name__ == "__main__":
    unittest.main()