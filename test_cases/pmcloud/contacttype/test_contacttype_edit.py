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

logger = Logger("TestContactTypeEdit").getLog()


class TestContactTypeEdit(unittest.TestCase):
    """联系类型编辑相关测试"""

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

        # 测试完成要删除新建的联系类型
        cls.contacttype_page.saveDeleteContactType()

        WorkbenchActions(cls.__driver).logout()
        logger.info("测试后退出.")
        cls.__driver.quit()

    def test_contacttype_edit_success(self):
        """编辑联系类型成功"""

        expected_contacttype = "自动化测试编辑联系类型"

        self.contacttype_page.saveEditContactType()

        actual_contacttype = self.contacttype_page.getEditContactTypeText()
        contacttype_list = self.contacttype_page.getContactTypeLists()

        self.contacttype_page.saveEditContactType(contact_type="自动化测试新增联系类型")  # 测试完成后改回之前的内容

        self.assertEqual(expected_contacttype, actual_contacttype,
                         msg="测试不通过，期望结果为：{expected}, 实际结果为：{actual}."
                         .format(expected=expected_contacttype, actual=actual_contacttype))
        self.assertIn(expected_contacttype, contacttype_list, msg="测试不通过，联系类型【{expected}】不存在"
                      .format(expected=expected_contacttype))

    def test_contacttype_edit_cancel(self):
        """取消编辑联系类型"""

        expected_contacttype = "自动化测试新增联系类型"

        self.contacttype_page.clickEditContactTypeButton()
        self.contacttype_page.editContactType()
        self.contacttype_page.clickEditContactTypeCancelButton()

        contacttype_list = self.contacttype_page.getContactTypeLists()

        self.assertIn(expected_contacttype, contacttype_list, msg="测试不通过，联系类型【{expected}】不应被修改."
                         .format(expected=expected_contacttype))

    def test_contacttype_edit_error_name_repeat(self):
        """编辑联系类型名称重复"""

        expected_toast_msg = "名称重复，保存失败！"
        expected_contacttype = "自动化测试新增联系类型"

        self.contacttype_page.saveEditContactType(contact_type="大型吊装作业")

        actual_toast_msg = self.contacttype_page.getToastMsg()

        self.contacttype_page.closeToast()
        self.contacttype_page.clickEditContactTypeCancelButton()

        actual_contacttype = self.contacttype_page.getEditContactTypeText()

        self.assertEqual(expected_toast_msg, actual_toast_msg,
                         msg="测试不通过，期望结果为：{expected}, 实际结果为：{actual}."
                         .format(expected=expected_toast_msg, actual=actual_toast_msg))
        self.assertEqual(expected_contacttype, actual_contacttype,
                         msg="测试不通过，期望结果为：{expected}, 实际结果为：{actual}."
                         .format(expected=expected_contacttype, actual=actual_contacttype))

    def test_contacttype_edit_error_name_null(self):
        """编辑联系类型名称为空"""

        expected_toast_msg = "请输入具体内容！"
        expected_contacttype = "自动化测试新增联系类型"

        self.contacttype_page.clickEditContactTypeButton()
        self.contacttype_page.editClearContactType()
        self.contacttype_page.clickEditContactTypeSaveButton()

        actual_toast_msg = self.contacttype_page.getToastMsg()

        self.contacttype_page.closeToast()
        self.contacttype_page.clickEditContactTypeCancelButton()

        actual_contacttype = self.contacttype_page.getEditContactTypeText()

        self.assertEqual(expected_toast_msg, actual_toast_msg,
                         msg="测试不通过，期望结果为：{expected}, 实际结果为：{actual}."
                         .format(expected=expected_toast_msg, actual=actual_toast_msg))
        self.assertEqual(expected_contacttype, actual_contacttype,
                         msg="测试不通过，期望结果为：{expected}, 实际结果为：{actual}."
                         .format(expected=expected_contacttype, actual=actual_contacttype))

    def test_contacttype_edit_error_name_over_length(self):
        """编辑联系类型名称长度超过50字符"""

        expected_toast_msg = "请限制在50个字符！"
        expected_contacttype = "一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十"

        self.contacttype_page.clickEditContactTypeButton()
        self.contacttype_page.editContactType(contact_type="一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十")

        actual_toast_msg = self.contacttype_page.getToastMsg()

        self.contacttype_page.closeToast()
        self.contacttype_page.clickEditContactTypeSaveButton()

        actual_contacttype = self.contacttype_page.getEditContactTypeText()

        self.contacttype_page.saveEditContactType(contact_type="自动化测试新增联系类型")  # 测试完成后改回之前的内容

        self.assertEqual(expected_toast_msg, actual_toast_msg,
                         msg="测试不通过，期望结果为：{expected}, 实际结果为：{actual}."
                         .format(expected=expected_toast_msg, actual=actual_toast_msg))
        self.assertEqual(expected_contacttype, actual_contacttype,
                         msg="测试不通过，期望结果为：{expected}, 实际结果为：{actual}."
                         .format(expected=expected_contacttype, actual=actual_contacttype))


if __name__ == '__main__':
    unittest.main()
