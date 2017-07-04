#coding=utf-8
#manhand testing
pass


'''from selenium import webdriver
import pymysql
import unittest,time

print("test20")
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
n=0
wf.find_element_by_id("parentLi").click()
wf.find_element_by_xpath(".//*[@id='myTab']/li[2]/a").click()
wf.find_element_by_xpath(".//*[@id='photobtn']").click()
time.sleep(1)
try:
    wf.find_element_by_xpath(".//*[@id='uploadPhoto']/div/div/table/tbody/tr[1]/td[2]/input").send_keys("666")
    wf.find_element_by_xpath(".//*[@id='txtPhotoImg']").send_keys("C:\Users\ETC\Desktop\babyplan\49727a2a8795ac0a97c2ce7c842f9c4b.jpg")
    wf.find_element_by_xpath(".//*[@id='uploadPhoto']/div/div/div[2]/button[1]").click()
except:
    print("fail")
    n=1
if n==0:
    print("pass")
wf.close()

if __name__ == "__main__":
    unittest.main()'''