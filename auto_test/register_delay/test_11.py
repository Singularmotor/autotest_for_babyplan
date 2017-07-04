#coding=utf-8
from selenium import webdriver
import pymysql
import unittest,time

print("test11")
wf = webdriver.Firefox()
ps=pymysql
bp=ps.connect(host='192.168.17.33',port=3306,user='root',passwd='123123',db='babyplan',charset='utf8')
#connect to the database ,if you want to use chinese in you request on pymysql, please type charset='utf8' at last
res=bp.cursor()

#check the function of register
def reg(ren,rpwd,cpwd):
    #ren==username rpwd==password cpwd==confirm the password
    # dd_2 is a way to identify the reports' types(except pass=1, except fail=0)
    wf.get("http://192.168.17.33:8080/BabyPlan/login.jsp")
    wf.find_element_by_xpath(".//*[@id='loginForm']/a").click()
    time.sleep(1)
    wf.find_element_by_id("regName").clear()
    wf.find_element_by_id("regPwd").clear()
    wf.find_element_by_id("pwdConfirm").clear()
    time.sleep(1)
    wf.find_element_by_id("regName").send_keys(ren) #username
    wf.find_element_by_id("regPwd").send_keys(rpwd) #password
    wf.find_element_by_id("pwdConfirm").send_keys(cpwd) #confirm password
    time.sleep(1)
    wf.find_element_by_xpath(".//*[@id='regbtn']").click() #complete the registering
##complete def

reg("test002","zhongruanguojiceshi05520170630","zhongruanguojiceshi05520170630")
b11=0
try:
    wf.find_element_by_id("regbtn").click()
except:
    res.execute("SELECT userName,`password` FROM userinfo WHERE userName='test002'")
    #find 'test002' in table 'userinfo' according to the username
    r6=res.fetchone()
    if r6[0]=='test002' and r6[1]=='zhongruanguojiceshi05520170630':
    #check the update of new user's information
        print("fail")
        b11=1
if b11!=1:
    print("pass")

wf.close()

if __name__ == "__main__":
    unittest.main()