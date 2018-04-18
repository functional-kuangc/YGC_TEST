# coding: utf-8
# 导入公共函数Selenium封装类
from libs.pagepubselenium import PagePubSelenium
# 导入联系类型元素定位
from page_objects.pmcloud.contacttype.page_elements.contacttype import ContactType
# 导入页面等待装饰器
from libs.timedecorator import timeDecorator

__author__ = "sunxr"
__version__ = "V1.0"


class ContactTypeActions(PagePubSelenium):
    """联系类型操作类"""

    # 新增相关操作
    @timeDecorator(1)
    def clickAddContactTypeButton(self):
        """
        点击新增按钮.
        """

        self.click(locator=ContactType.ADDCONTACTTYPEBTN)

    @timeDecorator(1)
    def typeContactType(self, contact_type="自动化测试新增联系类型"):
        """
        填写联系类型.
        :param contact_type: 联系类型名称
        """

        self.clear(locator=ContactType.ADDCONTACTTYPEINPUT)
        self.sendText(locator=ContactType.ADDCONTACTTYPEINPUT, text=contact_type)

    @timeDecorator(1)
    def clickAddContactTypeSaveButton(self):
        """
        新增联系类型点击保存按钮.
        """

        self.click(locator=ContactType.ADDCONTACTTYPESAVEBTN)

    @timeDecorator(1)
    def clickAddContactTypeCancelButton(self):
        """
        新增联系类型点击取消按钮.
        """

        self.click(locator=ContactType.ADDCONTACTTYPECANCELBTN)

    @timeDecorator(1)
    def getAddContactTypeText(self):
        """
        获取新增联系类型名称.
        :return: 新增联系类型名称
        """

        return self.getElementAttribute(locator=ContactType.ADDCONTACTTYPETEXT, name="value")

    # 编辑相关
    @timeDecorator(1)
    def clickEditContactTypeButton(self):
        """
        点击编辑按钮.
        """

        self.click(locator=ContactType.EDITCONTACTTYPEBTN)

    @timeDecorator(1)
    def editClearContactType(self):
        """
        使用编辑功能清空联系类型.
        """

        self.clear(locator=ContactType.EDITCONTACTTYPEINPUT)

    @timeDecorator(1)
    def editContactType(self, contact_type="自动化测试编辑联系类型"):
        """
        编辑联系类型.
        :param contact_type: 修改后联系类型名称.
        """

        self.editClearContactType()
        self.sendText(locator=ContactType.EDITCONTACTTYPEINPUT, text=contact_type)

    @timeDecorator(1)
    def clickEditContactTypeSaveButton(self):
        """
        编辑联系类型点击保存按钮.
        """

        self.click(locator=ContactType.EDITCONTACTTYPESAVEBTN)

    @timeDecorator(1)
    def clickEditContactTypeCancelButton(self):
        """
        编辑联系类型点击取消按钮.
        """

        self.click(locator=ContactType.EDITCONTACTTYPECANCELBTN)

    @timeDecorator(1)
    def getEditContactTypeText(self):
        """
        获取编辑后联系类型名称.
        :return: 编辑后联系类型名称
        """

        return self.getElementAttribute(locator=ContactType.EDITCONTACTTYPETEXT, name="value")

    # 删除相关
    @timeDecorator(1)
    def clickDeleteUsedContactTypeButton(self):
        """
        点击被引用的联系类型后面的删除按钮.
        """

        self.click(locator=ContactType.DELETECONTACTTYPEUSEDBTN)

    @timeDecorator(1)
    def clickDeleteNotUsedContactTypeButton(self):
        """
        点击未被引用的联系类型后面的删除按钮.
        """

        self.click(locator=ContactType.DELETECONTACTTYPENOTUSEDBTN)

    @timeDecorator(1)
    def getDeleteMsg(self):
        """
        获取删除操作时弹出的提示内容.
        :return: 提示信息内容
        """

        return self.getElementText(locator=ContactType.DELETECONTACTTYPEMSG)

    @timeDecorator(1)
    def clickDeleteOKButton(self):
        """
        在弹出的删除确认框中点击确定.
        """

        self.click(locator=ContactType.DELETECONTACTTYPEOKBTN)

    @timeDecorator(1)
    def clickDeleteCancelButton(self):
        """
        在弹出的删除确认框中点击取消.
        """

        self.click(locator=ContactType.DELETECONTACTTYPECANCELBTN)

    @timeDecorator(1)
    def clickDeleteCloseButton(self):
        """
        在弹出的删除确认框中点击右上角关闭.
        """

        self.click(locator=ContactType.DELETECONTACTTYPECLOSEBTN)

    @timeDecorator(1)
    def getDeleteContactTypeText(self):
        """
        获取删除后联系类型名称.
        """

        return self.getElementAttribute(locator=ContactType.DELETECONTACTTYPETEXT, name="value")

    # 公共操作
    @timeDecorator(1)
    def getToastMsg(self):
        """
        获取toast提示信息.
        :return: toast提示信息内容
        """

        return self.getElementText(locator=ContactType.TOAST)

    @timeDecorator(1)
    def getContactTypeLists(self):
        """
        获取所有联系类型.
        :return: 所有联系类型组成的列表
        """

        contact_type_list = list()
        elements = self.findElements(locator=ContactType.CONTACTTYPELISTS)

        for element in elements:
            contact_type_list.append(self.getElementAttribute(name="value", element=element))

        return contact_type_list

    # 流程类操作
    def saveAddContactType(self, contact_type="自动化测试新增联系类型"):
        """
        新增联系类型全流程.
        :param contact_type: 新增联系类型名称
        """

        self.clickAddContactTypeButton()
        self.typeContactType(contact_type=contact_type)
        self.clickAddContactTypeSaveButton()

    def saveEditContactType(self, contact_type="自动化测试编辑联系类型"):
        """
        编辑联系类型全流程.
        :param contact_type: 修改后联系类型名称
        """

        self.clickEditContactTypeButton()
        self.editContactType()
        self.clickEditContactTypeSaveButton()
