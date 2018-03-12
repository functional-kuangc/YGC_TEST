# coding: utf-8
# 导入测试框架unittest
import unittest
# 导入生成测试报告模块
from libs.HTMLTestRunner import HTMLTestRunner
# 导入time模块,用于时间处理
import time
# 导入日志模块
from libs.logger import Logger
# 导入Configuration模块,用于操作配置文件
from libs.configuration import Configuration
# 导入setBrowserType方法,用于多线程启动不同浏览器的兼容性测试
from libs.glo_browsertype import setBrowserType
# 导入os模块，获取文件路径
import os

__author__ = "sunxr"
__version__ = "V1.2"

logger = Logger("TestCaseSuite").getLog()


class TestCaseSuite:
    """
    定义测试用例路径,并执行测试用例
    """

    def __init__(self):

        # 创建配置文件实例
        config = Configuration()

        # 获取框架主路径信息
        self.__home_path = os.path.dirname(os.path.dirname(__file__))

        # 读取配置文件中的测试用例路径和测试用例执行规则
        self.__test_path = config.getConfigValue("testCaseSuite", "test_path")
        logger.info("测试用例路径为: %s." % self.__test_path)
        self.__test_rule = config.getConfigValue("testCaseSuite", "test_rule")
        logger.info("测试用例执行规则为: %s." % self.__test_rule)

    def __addCase(self):
        """
        加载所有测试用例.
        :return: 需要执行的测试用例.
        """

        # 加载所有的测试用例
        try:
            logger.info("开始加载测试用例.")
            testcases = unittest.defaultTestLoader.discover(self.__test_path,
                                                            pattern=self.__test_rule,
                                                            top_level_dir=None)
            logger.info("需要执行的测试用例为: %s." % testcases)
            return testcases
        except Exception as msg:
            logger.error("加载测试用例异常: %s." % msg)

    def __runCase(self, testcases):
        """
        执行测试用例,生成测试报告.
        :param testcases: 测试用例
        :return: 测试报告
        """

        # 定义测试报告的路径
        now_time = time.strftime("%Y_%m_%d %H_%M_%S")
        report_path = self.__home_path + "/test_reports/" + now_time + "result.html"

        # 执行所有的用例
        try:
            fp = open(report_path, "wb")
            runner = HTMLTestRunner(stream=fp,
                                    verbosity=1,
                                    title="自动化测试报告,测试结果如下:",
                                    description="测试用例执行情况:",
                                    )
            logger.info("开始执行测试用例.")
            runner.run(testcases)
            fp.close()
            logger.info("测试用例执行完毕,生成测试报告: %s." % report_path)
        except Exception as msg:
            logger.error("执行测试用例异常: %s." % msg)

    def executeTestCases(self):
        """
        加载测试用例,执行测试用例方法集成.
        """

        self.__runCase(self.__addCase())

    def executeCompatibilityTestCases(self, browser_type):
        """
        加载测试用例,设置兼容的浏览器类型,执行测试用例方法集成.
        :param browser_type: 浏览器类型
        """
        testcases = self.__addCase()
        setBrowserType(browser_type)
        self.__runCase(testcases=testcases)
