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
# 导入项目档案操作类
from page_objects import ProjectActions

__author__ = "sunxr"
__version__ = "V1.0"

logger = Logger("TestProject").getLog()


class TestProject(unittest.TestCase):
    """测试友工程项目档案"""

    def setUp(self):

        logger.info("测试前准备.")
        self.__driver = browser(glo.GLO_BROWSER_TYPE)

        PMCloudIndexActions(self.__driver).openPMCloudIndex(expected_title="用友云工程服务")
        PMCloudIndexActions(self.__driver).clickLoginButton()
        PMCloudLoginActions(self.__driver).pmcloudLogin()
        ApptenantActions(self.__driver).apptenantLogin()
        WorkbenchActions(self.__driver).clickProject()
        WorkbenchActions(self.__driver).switchToIframe()

    def tearDown(self):

        logger.info("测试后退出.")
        WorkbenchActions(self.__driver).switchBackToFrame()
        WorkbenchActions(self.__driver).logout()
        self.__driver.quit()

    def test_create_and_delete_success(self):

        project_page = ProjectActions(self.__driver)
        project_page.saveCreateProject()
        print(project_page.getListToastMsg())
        project_page.closeListToast()
        project_page.saveDeleteProject()


if __name__ == '__main__':
    unittest.main()
