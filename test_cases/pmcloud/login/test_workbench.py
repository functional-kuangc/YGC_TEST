# coding: utf-8
# 导入测试框架unittest
import unittest
# 导入浏览器
from libs.browser import browser
# 导入日志模块
from libs.logger import Logger
# 导入全局浏览器变量,用于多线程启动不同浏览器的兼容性测试
import libs.glo_browsertype as glo
# 导入友工程首页操作类
from page_objects import PMCloudIndexActions
# 导入友工程登录页操作类
from page_objects import PMCloudLoginActions
# 导入企业帐号选择页操作类
from page_objects import ApptenantActions
# 导入友工程后台外框架操作类
from page_objects import WorkbenchActions

__author__ = "sunxr"
__version__ = "V1.0"

logger = Logger("TestWorkbench").getLog()


class TestWorkbench(unittest.TestCase):
    """测试友工程的工作台框架"""

    @classmethod
    def setUpClass(cls):

        logger.info("测试前准备.")
        cls.__driver = browser(glo.GLO_BROWSER_TYPE)

        PMCloudIndexActions(cls.__driver).login()
        PMCloudLoginActions(cls.__driver).pmcloudLogin()
        ApptenantActions(cls.__driver).apptenantLogin()
        cls.workbench_page = WorkbenchActions(cls.__driver)

    @classmethod
    def tearDownClass(cls):

        logger.info("测试后退出.")
        WorkbenchActions(cls.__driver).logout()
        cls.__driver.quit()

    def test_1_click_project(self):
        """测试点击项目档案"""

        self.workbench_page.clickProject()

        expected_result = "项目档案"
        result = self.workbench_page.getElementText(locator=("xpath", '//*[@id="app"]/div/div/div/div[1]/h1'))

        self.assertEqual(expected_result, result, msg="测试不通过，期望结果为：{expect}, 实际结果为：{result}."
                         .format(expect=expected_result, result=result))

    def test_2_click_produce(self):
        """测试点击工序"""

        self.workbench_page.clickProduce()

        expected_result = "工序"
        result = self.workbench_page.getElementText(locator=("xpath", '//*[@id="app"]/div/div/div/div[1]/h1'))

        self.assertEqual(expected_result, result, msg="测试不通过，期望结果为：{expect}, 实际结果为：{result}."
                         .format(expect=expected_result, result=result))

    def test_3_click_work_quality(self):
        """测试点击质量标准"""

        self.workbench_page.clickWorkQuality()

        expected_result = "质量标准"
        result = self.workbench_page.getElementText(locator=("xpath", '//*[@id="app"]/div/div/div/div[1]/h4'))

        self.assertEqual(expected_result, result, msg="测试不通过，期望结果为：{expect}, 实际结果为：{result}."
                         .format(expect=expected_result, result=result))

    def test_4_click_problem_reason(self):
        """测试点击问题原因"""

        self.workbench_page.clickProblemReason()

        expected_result = "问题原因"
        result = self.workbench_page.getElementText(locator=("xpath", '//*[@id="app"]/div/div/div/div[1]/h1'))

        self.assertEqual(expected_result, result, msg="测试不通过，期望结果为：{expect}, 实际结果为：{result}."
                         .format(expect=expected_result, result=result))

    def test_5_click_contact_type(self):
        """测试点击联系类型"""

        self.workbench_page.clickContactType()

        expected_result = "联系类型"
        result = self.workbench_page.getElementText(locator=("xpath", '//*[@id="app"]/div/div/div/div[1]'))

        self.assertEqual(expected_result, result, msg="测试不通过，期望结果为：{expect}, 实际结果为：{result}."
                         .format(expect=expected_result, result=result))


if __name__ == '__main__':
    unittest.main()
