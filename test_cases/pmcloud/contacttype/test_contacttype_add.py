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
# 导入友工程联系类型操作类
from page_objects import ContactTypeActions

__author__ = "sunxr"
__version__ = "V1.0"

logger = Logger("TestContactTypeAdd").getLog()


class TestContactTypeAdd(unittest.TestCase):
    """联系类型新增相关测试"""

    def setUp(self):

        logger.info("测试前准备.")
        self.__driver = browser(glo.GLO_BROWSER_TYPE)
        PMCloudIndexActions(self.__driver).login()
        PMCloudLoginActions(self.__driver).pmcloudLogin()
        ApptenantActions(self.__driver).apptenantLogin()
        WorkbenchActions(self.__driver).clickContactType()

    def tearDown(self):

        logger.info("测试后退出.")
        WorkbenchActions(self.__driver).logout()
        self.__driver.quit()

    def test_contacttypelist(self):

        contacttype_page = ContactTypeActions(self.__driver)

        contacttype_page.click(ContactType.ADDCONTACTTYPECANCELBTN)
        contacttype_page.pageSleep(2)

        elements = contacttype_page.findElements(("xpath", "/html/body/div[1]/div/div/div/div[2]/div[1]/span//input"))
        # print(elements)
        for element in elements:
            print(element.get_attribute("value"))
        elements = self.__driver.find_elements_by_class_name("widget__input")
        # print(elements)
        for element in elements:
            e = element.find_element_by_tag_name("input")
            print(e.get_attribute("value"))


if __name__ == '__main__':
    unittest.main()
