# coding: utf-8
# 导入公共函数Selenium封装类
from libs.pagepubselenium import PagePubSelenium
# 导入添加参与企业元素定位
from page_objects.pmcloud.project.page_elements.project_team_enterprise_add import ProjectTeamEnterpriseAdd
# 导入页面等待装饰器
from libs.timedecorator import timeDecorator

__author__ = "sunxr"
__version__ = "V1.0"


class ProjectTeamEnterpriseAddActions(PagePubSelenium):
    """添加参与企业操作类"""

    @timeDecorator(1)
    def clearSearchKeyword(self):
        """
        清空搜索框中关键字.
        """

        if self.getElementText(locator=ProjectTeamEnterpriseAdd.MODULENAME4) == "添加参与企业":
            self.clear(locator=ProjectTeamEnterpriseAdd.SEARCHINPUT4)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.MODULENAME6) == "添加参与企业":
            self.clear(locator=ProjectTeamEnterpriseAdd.SEARCHINPUT6)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.MODULENAME3) == "添加参与企业":
            self.clear(locator=ProjectTeamEnterpriseAdd.SEARCHINPUT3)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.MODULENAME5) == "添加参与企业":
            self.clear(locator=ProjectTeamEnterpriseAdd.SEARCHINPUT5)

    @timeDecorator(1)
    def typeSearchKeyword(self, keyword="sxr"):
        """
        在搜索框中输入搜索关键字.
        :param keyword: 搜索关键字
        """

        if self.getElementText(locator=ProjectTeamEnterpriseAdd.MODULENAME4) == "添加参与企业":
            self.sendText(locator=ProjectTeamEnterpriseAdd.SEARCHINPUT4, text=keyword)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.MODULENAME6) == "添加参与企业":
            self.sendText(locator=ProjectTeamEnterpriseAdd.SEARCHINPUT6, text=keyword)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.MODULENAME3) == "添加参与企业":
            self.sendText(locator=ProjectTeamEnterpriseAdd.SEARCHINPUT3, text=keyword)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.MODULENAME5) == "添加参与企业":
            self.sendText(locator=ProjectTeamEnterpriseAdd.SEARCHINPUT5, text=keyword)

    @timeDecorator(3)
    def clickSearchButton(self):
        """
        点击搜索按钮.
        :return: 搜索结果
        """

        if self.getElementText(locator=ProjectTeamEnterpriseAdd.MODULENAME4) == "添加参与企业":
            self.click(locator=ProjectTeamEnterpriseAdd.SEARCHBUTTON4)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.MODULENAME6) == "添加参与企业":
            self.click(locator=ProjectTeamEnterpriseAdd.SEARCHBUTTON6)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.MODULENAME3) == "添加参与企业":
            self.click(locator=ProjectTeamEnterpriseAdd.SEARCHBUTTON3)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.MODULENAME5) == "添加参与企业":
            self.click(locator=ProjectTeamEnterpriseAdd.SEARCHBUTTON5)

    @timeDecorator(1)
    def selectFirstEnterprise(self):
        """
        从搜索结果中选择第一个企业.
        """

        if self.getElementText(locator=ProjectTeamEnterpriseAdd.MODULENAME4) == "添加参与企业":
            self.click(locator=ProjectTeamEnterpriseAdd.SELECTSEARCHLIST41)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.MODULENAME6) == "添加参与企业":
            self.click(locator=ProjectTeamEnterpriseAdd.SELECTSEARCHLIST61)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.MODULENAME3) == "添加参与企业":
            self.click(locator=ProjectTeamEnterpriseAdd.SELECTSEARCHLIST31)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.MODULENAME5) == "添加参与企业":
            self.click(locator=ProjectTeamEnterpriseAdd.SELECTSEARCHLIST51)

    def selectSecondEnterprise(self):
        """
        从搜索结果中选择第二个企业.
        """

        if self.getElementText(locator=ProjectTeamEnterpriseAdd.MODULENAME4) == "添加参与企业":
            self.click(locator=ProjectTeamEnterpriseAdd.SELECTSEARCHLIST42)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.MODULENAME6) == "添加参与企业":
            self.click(locator=ProjectTeamEnterpriseAdd.SELECTSEARCHLIST62)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.MODULENAME3) == "添加参与企业":
            self.click(locator=ProjectTeamEnterpriseAdd.SELECTSEARCHLIST32)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.MODULENAME5) == "添加参与企业":
            self.click(locator=ProjectTeamEnterpriseAdd.SELECTSEARCHLIST52)

    def clickOKButton(self):
        """
        点击确定按钮.
        """

        if self.getElementText(locator=ProjectTeamEnterpriseAdd.MODULENAME4) == "添加参与企业":
            self.click(locator=ProjectTeamEnterpriseAdd.OKBTN4)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.MODULENAME6) == "添加参与企业":
            self.click(locator=ProjectTeamEnterpriseAdd.OKBTN6)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.MODULENAME3) == "添加参与企业":
            self.click(locator=ProjectTeamEnterpriseAdd.OKBTN3)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.MODULENAME5) == "添加参与企业":
            self.click(locator=ProjectTeamEnterpriseAdd.OKBTN5)

    def clickCancelButton(self):
        """
        点击取消按钮.
        """

        if self.getElementText(locator=ProjectTeamEnterpriseAdd.MODULENAME4) == "添加参与企业":
            self.click(locator=ProjectTeamEnterpriseAdd.CANCELBTN4)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.MODULENAME6) == "添加参与企业":
            self.click(locator=ProjectTeamEnterpriseAdd.CANCELBTN6)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.MODULENAME3) == "添加参与企业":
            self.click(locator=ProjectTeamEnterpriseAdd.CANCELBTN3)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.MODULENAME5) == "添加参与企业":
            self.click(locator=ProjectTeamEnterpriseAdd.CANCELBTN5)

    def clickCloseButton(self):
        """
        点击右上角关闭按钮.
        """

        if self.getElementText(locator=ProjectTeamEnterpriseAdd.MODULENAME4) == "添加参与企业":
            self.click(locator=ProjectTeamEnterpriseAdd.CLOSEBTN4)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.MODULENAME6) == "添加参与企业":
            self.click(locator=ProjectTeamEnterpriseAdd.CLOSEBTN6)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.MODULENAME3) == "添加参与企业":
            self.click(locator=ProjectTeamEnterpriseAdd.CLOSEBTN3)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.MODULENAME5) == "添加参与企业":
            self.click(locator=ProjectTeamEnterpriseAdd.CLOSEBTN5)

    def getToastMsg(self):
        """
        获取toast提示信息.
        :return: toast提示信息
        """

        if self.getElementText(locator=ProjectTeamEnterpriseAdd.MODULENAME4) == "添加参与企业":
            return self.getElementText(locator=ProjectTeamEnterpriseAdd.ENTERPRISEADDTOAST5)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.MODULENAME6) == "添加参与企业":
            return self.getElementText(locator=ProjectTeamEnterpriseAdd.ENTERPRISEADDTOAST7)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.MODULENAME3) == "添加参与企业":
            return self.getElementText(locator=ProjectTeamEnterpriseAdd.ENTERPRISEADDTOAST4)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.MODULENAME5) == "添加参与企业":
            return self.getElementText(locator=ProjectTeamEnterpriseAdd.ENTERPRISEADDTOAST6)

    def closeToast(self):
        """
        关闭toast提示.
        """

        if self.getElementText(locator=ProjectTeamEnterpriseAdd.MODULENAME4) == "添加参与企业":
            return self.click(locator=ProjectTeamEnterpriseAdd.ENTERPRISEADDTOASTCLOSE5)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.MODULENAME6) == "添加参与企业":
            return self.getElementText(locator=ProjectTeamEnterpriseAdd.ENTERPRISEADDTOASTCLOSE7)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.MODULENAME3) == "添加参与企业":
            return self.getElementText(locator=ProjectTeamEnterpriseAdd.ENTERPRISEADDTOASTCLOSE4)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.MODULENAME5) == "添加参与企业":
            return self.getElementText(locator=ProjectTeamEnterpriseAdd.ENTERPRISEADDTOASTCLOSE6)

    pass

# 搜索流程

# 设置流程

# 添加流程

# 退出流程


