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

logger = Logger("TestLogin").getLog()


class TestLogin(unittest.TestCase):
    """测试友工程登录"""

    def setUp(self):

        logger.info("测试前准备.")
        self.__driver = browser(glo.GLO_BROWSER_TYPE)

    def tearDown(self):

        logger.info("测试后退出.")
        self.__driver.quit()

    def test_login_success(self):
        """登录成功"""

        logger.info("执行TestLogin_test_login_success测试用例.")
        expected_result = "测试孙旭冉"

        index_page = PMCloudIndexActions(self.__driver)
        index_page.openPMCloudIndex(expected_title="工程云")
        index_page.clickLoginButton()

        login_page = PMCloudLoginActions(self.__driver)
        login_page.pmcloudLogin(remember_selected=True)

        apptenant_page = ApptenantActions(self.__driver)
        apptenant_page.apptenantLogin()

        result = self.__driver.find_element_by_xpath(".//*[@id='username']/span[2]").text

        self.assertEqual(expected_result, result, msg="测试不通过，期望结果为：{expect}, 实际结果为：{result}."
                         .format(expect=expected_result, result=result))


if __name__ == '__main__':
    unittest.main()
