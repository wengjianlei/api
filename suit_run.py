import unittest
from tools.HTMLTestRunner import HTMLTestRunner
import time

#组装测试套件
suite=unittest.defaultTestLoader.discover("./case",pattern="test_*.py")
#制定报告存放路径及文件名称
file_path="./report/{}.html".format(time.strftime("%Y_%m_%d  %H_%M_%S"))

with open(file_path,"wb") as f:
    HTMLTestRunner(stream=f,title="自动化测试报告",description='api_tester',verbosity=2).run(suite)