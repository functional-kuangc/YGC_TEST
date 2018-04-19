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

    @classmethod
    def setUpClass(cls):

        logger.info("测试前准备.")
        cls.__driver = browser(glo.GLO_BROWSER_TYPE)
        PMCloudIndexActions(cls.__driver).login()
        PMCloudLoginActions(cls.__driver).pmcloudLogin()
        ApptenantActions(cls.__driver).apptenantLogin()
        WorkbenchActions(cls.__driver).clickContactType()
        cls.contacttype_page = ContactTypeActions(cls.__driver)

    @classmethod
    def tearDownClass(cls):

        WorkbenchActions(cls.__driver).logout()
        logger.info("测试后退出.")
        cls.__driver.quit()

    def test_contacttype_add_success(self):
        """新增联系类型成功"""

        expected_contacttype = "自动化测试新增联系类型"

        # self.contacttype_page.clickAddContactTypeCancelButton()
        self.contacttype_page.saveAddContactType()

        actual_contacttype = self.contacttype_page.getAddContactTypeText()
        contacttype_list = self.contacttype_page.getContactTypeLists()

        self.contacttype_page.saveDeleteContactType()  # 测试完成后要删除，并且放在断言前面

        self.assertEqual(expected_contacttype, actual_contacttype,
                         msg="测试不通过，期望结果为：{expected}, 实际结果为：{actual}."
                         .format(expected=expected_contacttype, actual=actual_contacttype))
        self.assertIn(expected_contacttype, contacttype_list, msg="测试不通过，联系类型【{expected}】不存在"
                      .format(expected=expected_contacttype))

    def test_contacttype_add_cancel(self):
        """取消新增联系类型"""

        expected_contacttype = "自动化测试新增联系类型"

        self.contacttype_page.clickAddContactTypeCancelButton()
        self.contacttype_page.clickAddContactTypeButton()
        self.contacttype_page.typeContactType()
        self.contacttype_page.clickAddContactTypeCancelButton()

        contacttype_list = self.contacttype_page.getContactTypeLists()

        self.assertNotIn(expected_contacttype, contacttype_list, msg="测试不通过，联系类型【{expected}】不应该存在."
                         .format(expected=expected_contacttype))

    def test_contacttype_add_error_name_repeat(self):
        """新增联系类型名称重复"""

        expected_toast_msg = "名称重复，保存失败！"

        self.contacttype_page.clickAddContactTypeCancelButton()
        self.contacttype_page.saveAddContactType(contact_type="大型吊装作业")

        actual_toast_msg = self.contacttype_page.getToastMsg()

        self.contacttype_page.closeToast()
        self.contacttype_page.clickAddContactTypeCancelButton()

        self.assertEqual(expected_toast_msg, actual_toast_msg,
                         msg="测试不通过，期望结果为：{expected}, 实际结果为：{actual}."
                         .format(expected=expected_toast_msg, actual=actual_toast_msg))

    def test_contacttype_add_error_name_null(self):
        """新增联系类型名称为空"""

        expected_toast_msg = "请输入具体内容！"

        # self.contacttype_page.clickAddContactTypeCancelButton()
        self.contacttype_page.saveAddContactType(contact_type="")

        actual_toast_msg = self.contacttype_page.getToastMsg()

        self.contacttype_page.closeToast()
        self.contacttype_page.clickAddContactTypeCancelButton()

        self.assertEqual(expected_toast_msg, actual_toast_msg,
                         msg="测试不通过，期望结果为：{expected}, 实际结果为：{actual}."
                         .format(expected=expected_toast_msg, actual=actual_toast_msg))

    def test_contacttype_add_error_name_over_length(self):
        """新增联系类型名称长度超过50字符"""

        expected_toast_msg = "请限制在50个字符！"
        expected_contacttype = "一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十"

        # self.contacttype_page.clickAddContactTypeCancelButton()
        self.contacttype_page.clickAddContactTypeButton()
        self.contacttype_page.typeContactType(contact_type="一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十")

        actual_toast_msg = self.contacttype_page.getToastMsg()

        self.contacttype_page.closeToast()
        self.contacttype_page.clickAddContactTypeSaveButton()

        actual_contacttype = self.contacttype_page.getAddContactTypeText()

        self.contacttype_page.saveDeleteContactType()  # 测试完成后要删除，并且放在断言前面

        self.assertEqual(expected_toast_msg, actual_toast_msg,
                         msg="测试不通过，期望结果为：{expected}, 实际结果为：{actual}."
                         .format(expected=expected_toast_msg, actual=actual_toast_msg))
        self.assertEqual(expected_contacttype, actual_contacttype,
                         msg="测试不通过，期望结果为：{expected}, 实际结果为：{actual}."
                         .format(expected=expected_contacttype, actual=actual_contacttype))


if __name__ == '__main__':
    unittest.main()
