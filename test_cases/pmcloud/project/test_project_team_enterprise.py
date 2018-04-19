# coding: utf-8
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
# 导入项目参与方操作类
from page_objects import ProjectTeamEnterpriseActions
# 导入添加参与企业操作类
from page_objects import ProjectTeamEnterpriseAddActions

__author__ = "sunxr"
__version__ = "V1.0"

logger = Logger("TestProjectTeamEnterprise").getLog()


@unittest.skip
class TestProjectTeamEnterprise(unittest.TestCase):
    """测试友工程项目参与方"""

    def setUp(self):

        logger.info("测试前准备.")
        self.__driver = browser(glo.GLO_BROWSER_TYPE)

        PMCloudIndexActions(self.__driver).openPMCloudIndex()
        PMCloudIndexActions(self.__driver).clickLoginButton()
        PMCloudLoginActions(self.__driver).pmcloudLogin()
        ApptenantActions(self.__driver).apptenantLogin()
        WorkbenchActions(self.__driver).clickProject()
        WorkbenchActions(self.__driver).switchToIframe()
        ProjectActions(self.__driver).saveCreateProject()
        ProjectActions(self.__driver).closeListToast()
        ProjectActions(self.__driver).selectFirstProject()
        ProjectActions(self.__driver).clickEnterpriseButton()

    def tearDown(self):

        logger.info("测试后退出.")

        ProjectActions(self.__driver).saveDeleteProject()
        WorkbenchActions(self.__driver).switchBackToFrame()
        WorkbenchActions(self.__driver).logout()
        self.__driver.quit()

    def test_add_and_delete_success(self):

        enterprise_page = ProjectTeamEnterpriseActions(self.__driver)
        enterprise_page.clickAddButton()

        enterprise_add_page = ProjectTeamEnterpriseAddActions(self.__driver)
        enterprise_add_page.saveEnterpriseAdd()
        enterprise_page.saveDeleteEnterprise()
        enterprise_page.clickCLoseButton()


if __name__ == '__main__':
    unittest.main()
