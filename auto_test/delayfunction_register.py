import time
from selenium import webdriver
import pymysql
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
    wf.refresh()
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

#BD_06
reg("ouo","456456","456456")
res.execute("SELECT userName,`password` FROM userinfo WHERE userName='ouo'")
#find 'ouo' in table 'userinfo' according to the username
r1=res.fetchone()
if r1[0]=='ouo' and r1[1]=='456456':
    #check the update of new user's information
    print("pass")
else:
    print("fail")
#BD_06

#BD_07
reg("测试01","456456","456456")
res.execute("SELECT * FROM userinfo WHERE userName='测试01'")
#find '测试01' in table 'userinfo' according to the username
r2=res.fetchone()
if r2 is None:
    #check the update of new user's information
        print("fail")
        b7=1
else:
    if r2[2]=="测试01" and r2[3]=="456456":
        print("pass")
    else:
        print("fail")
time.sleep(2)
#BD_07

#BD_08
reg("%o@","456456","456456")
b8=0
try:
    wf.find_element_by_id("regbtn").click()
except:
    res.execute("SELECT userName,`password` FROM userinfo WHERE userName='%o@'")
    #find '%o@' in table 'userinfo' according to the username
    r3=res.fetchone()
    if r3[0]=='%o@' and r3[1]=='456456':
    #check the update of new user's information
        print("fail")
        b8=1
if b8!=1:
    print("pass")
time.sleep(2)
#BD_08

#BD_09
reg("test","456456","456456")
b9=0
try:
    wf.find_element_by_id("regbtn").click()
except:
    res.execute("SELECT userName,`password` FROM userinfo WHERE userName='test'")
    #find 'test' in table 'userinfo' according to the username
    r4=res.fetchone()
    if r4[0]=='test' and r4[1]=='456456':
    #check the update of new user's information
        print("fail")
        b9=1
if b9!=1:
    print("pass")
time.sleep(2)
#BD_09

#BD_10
reg("test001","45645","45645")
b10=0
try:
    wf.find_element_by_id("regbtn").click()
except:
    res.execute("SELECT userName,`password` FROM userinfo WHERE userName='test001'")
    #find 'test001' in table 'userinfo' according to the username
    r5=res.fetchone()
    if r5[0]=='test001' and r5[1]=='45645':
    #check the update of new user's information
        print("fail")
        b10=1
if b10!=1:
    print("pass")
time.sleep(2)
#BD_10

#BD_11
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
time.sleep(2)
#BD_11

#BD_12
reg("test003","456456","123123")
b12=0
try:
    wf.find_element_by_id("regbtn").click()
except:
    res.execute("SELECT userName,`password` FROM userinfo WHERE userName='test003'")
    #find 'test003' in table 'userinfo' according to the username
    r6=res.fetchone()
    if r6[0]=='test003':
    #check the update of new user's information
        print("fail")
        b12=1
if b12!=1:
    print("pass")
time.sleep(2)
#BD_12