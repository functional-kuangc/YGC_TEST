# coding: utf-8
# 导入测试用例执行模块
from libs.testcasesuite import TestCaseSuite
# 导入邮件模块
from libs.sendmail import SendMail
# 导入多线程模块
import threading
# 导入Configuration模块,用于操作配置文件
from libs.configuration import Configuration
import time

__author__ = "sunxr"
__version__ = "V1.1"


# 集成测试用例执行和发送邮件功能
def executeCompatibilityTestcasesAndSendMail(thread_browser_type):
    """
    集成测试用例执行和发送邮件功能.
    :param thread_browser_type: 浏览器类型
    """
    TestCaseSuite().executeCompatibilityTestcases(thread_browser_type)
    # SendMail().sendTestReport()

# 实例化配置文件
config = Configuration()

# 获取浏览器类型数量
browser_types = config.getConfigOptions(section="browserType")
browser_counts = len(browser_types)

# 获取浏览器具体类型
browsers = list()

for browser_type in browser_types:
    browser = config.getConfigValue(section="browserType", option=browser_type)
    browsers.append(browser)

# 利用多线程启动所有浏览器执行用例
threads = list()

for thread_browser in browsers:
    thread = threading.Thread(target=executeCompatibilityTestcasesAndSendMail, args=(thread_browser, ))
    threads.append(thread)

for i in range(browser_counts):
    time.sleep(1)
    threads[i].start()

for i in range(browser_counts):
    threads[i].join()
