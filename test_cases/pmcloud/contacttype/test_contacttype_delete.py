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

logger = Logger("TestContactTypeDelete").getLog()


class TestContactTypeDelete(unittest.TestCase):
    """联系类型删除相关测试"""

    @classmethod
    def setUpClass(cls):
        logger.info("测试前准备.")
        cls.__driver = browser(glo.GLO_BROWSER_TYPE)
        PMCloudIndexActions(cls.__driver).login()
        PMCloudLoginActions(cls.__driver).pmcloudLogin()
        ApptenantActions(cls.__driver).apptenantLogin()
        WorkbenchActions(cls.__driver).clickContactType()

        # 提前新建好联系类型
        cls.contacttype_page = ContactTypeActions(cls.__driver)
        cls.contacttype_page.clickAddContactTypeCancelButton()
        cls.contacttype_page.saveAddContactType()
        cls.contacttype_page.clickAddContactTypeCancelButton()

    @classmethod
    def tearDownClass(cls):

        WorkbenchActions(cls.__driver).logout()
        logger.info("测试后退出.")
        cls.__driver.quit()

    def test_contacttype_delete_success(self):
        """删除编辑类型成功"""

        expected_toast_msg = "成功删除！"
        expected_contacttype = "自动化测试新增联系类型"

        self.contacttype_page.saveDeleteContactType()

        actual_toast_msg = self.contacttype_page.getToastMsg()
        contacttype_list = self.contacttype_page.getContactTypeLists()

        self.assertEqual(expected_toast_msg, actual_toast_msg,
                         msg="测试不通过，期望结果为：{expected}, 实际结果为：{actual}."
                         .format(expected=expected_toast_msg, actual=actual_toast_msg))
        self.assertNotIn(expected_contacttype, contacttype_list, msg="测试不通过，联系类型【{expected}】不应该存在."
                         .format(expected=expected_contacttype))

    def test_contacttype_delete_cancel(self):
        """通过取消按钮取消删除"""

        expected_contacttype = "自动化测试新增联系类型"

        self.contacttype_page.clickDeleteNotUsedContactTypeButton()
        self.contacttype_page.clickDeleteCancelButton()

        contacttype_list = self.contacttype_page.getContactTypeLists()

        self.assertIn(expected_contacttype, contacttype_list, msg="测试不通过，联系类型【{expected}】不存在"
                      .format(expected=expected_contacttype))

    def test_contacttype_delete_close(self):
        """通过右上角关闭按钮取消删除"""

        expected_contacttype = "自动化测试新增联系类型"

        self.contacttype_page.clickDeleteNotUsedContactTypeButton()
        self.contacttype_page.clickDeleteCloseButton()

        contacttype_list = self.contacttype_page.getContactTypeLists()

        self.assertIn(expected_contacttype, contacttype_list, msg="测试不通过，联系类型【{expected}】不存在"
                      .format(expected=expected_contacttype))

    def test_contacttype_delete_msg(self):
        """删除提示信息验证"""

        expected_delete_msg = "是否删除该信息？"

        self.contacttype_page.clickDeleteNotUsedContactTypeButton()

        actual_delete_msg = self.contacttype_page.getDeleteMsg()

        self.contacttype_page.clickDeleteCancelButton()

        self.assertEqual(expected_delete_msg, actual_delete_msg,
                         msg="测试不通过，期望结果为：{expected}, 实际结果为：{actual}."
                         .format(expected=expected_delete_msg, actual=actual_delete_msg))

    def test_contacttype_delete_error_used(self):
        """被引用的联系类型删除验证"""

        expected_toast_msg = "数据已经被引用，不可进行该操作！"
        expected_contacttype = "自动化测试新增联系类型"

        self.contacttype_page.clickDeleteUsedContactTypeButton()
        self.contacttype_page.clickDeleteOKButton()

        actual_toast_msg = self.contacttype_page.getToastMsg()

        self.contacttype_page.closeToast()

        contacttype_list = self.contacttype_page.getContactTypeLists()

        self.assertEqual(expected_toast_msg, actual_toast_msg,
                         msg="测试不通过，期望结果为：{expected}, 实际结果为：{actual}."
                         .format(expected=expected_toast_msg, actual=actual_toast_msg))

        self.assertIn(expected_contacttype, contacttype_list, msg="测试不通过，联系类型【{expected}】不存在"
                      .format(expected=expected_contacttype))


if __name__ == '__main__':
    unittest.main()
