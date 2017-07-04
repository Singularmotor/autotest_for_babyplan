#coding=utf8
import HTMLTestRunner
import unittest
import time


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
    filename = testreport + now + '_babyplan_project_result.html'
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