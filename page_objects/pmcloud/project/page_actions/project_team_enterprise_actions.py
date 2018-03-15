# coding: utf-8
# 导入公共函数Selenium封装类
from libs.pagepubselenium import PagePubSelenium
# 导入项目参与方元素定位
from page_objects.pmcloud.project.page_elements.project_team_enterprise import ProjectTeamEnterprise
# 导入页面等待装饰器
from libs.timedecorator import timeDecorator

__author__ = "sunxr"
__version__ = "V1.0"


class ProjectTeamEnterpriseActions(PagePubSelenium):
    """项目参与方操作类"""

    @timeDecorator(1)
    def selectFirstEnterprise(self):
        """
        点击选中第一个参与企业.
        """

        if self.getElementText(locator=ProjectTeamEnterprise.MODULENAME3) == "项目参与方":
            self.click(locator=ProjectTeamEnterprise.FIRSTENTERPRISENAME3)
        elif self.getElementText(locator=ProjectTeamEnterprise.MODULENAME5) == "项目参与方":
            self.click(locator=ProjectTeamEnterprise.FIRSTENTERPRISENAME5)
        elif self.getElementText(locator=ProjectTeamEnterprise.MODULENAME2) == "项目参与方":
            self.click(locator=ProjectTeamEnterprise.FIRSTENTERPRISENAME2)
        elif self.getElementText(locator=ProjectTeamEnterprise.MODULENAME4) == "项目参与方":
            self.click(locator=ProjectTeamEnterprise.FIRSTENTERPRISENAME4)

    @timeDecorator(1)
    def clickAddButton(self):
        """
        点击添加按钮.
        """

        if self.getElementText(locator=ProjectTeamEnterprise.MODULENAME3) == "项目参与方":
            self.click(locator=ProjectTeamEnterprise.ADDBTN3)
        elif self.getElementText(locator=ProjectTeamEnterprise.MODULENAME2) == "项目参与方":
            self.click(locator=ProjectTeamEnterprise.ADDBTN2)
        elif self.getElementText(locator=ProjectTeamEnterprise.MODULENAME5) == "项目参与方":
            self.click(locator=ProjectTeamEnterprise.ADDBTN5)
        elif self.getElementText(locator=ProjectTeamEnterprise.MODULENAME4) == "项目参与方":
            self.click(locator=ProjectTeamEnterprise.ADDBTN4)

    @timeDecorator(1)
    def clickDeleteButton(self):
        """
        点击删除按钮.
        """

        if self.getElementText(locator=ProjectTeamEnterprise.MODULENAME3) == "项目参与方":
            self.click(locator=ProjectTeamEnterprise.DELETEBTN3)
        elif self.getElementText(locator=ProjectTeamEnterprise.MODULENAME2) == "项目参与方":
            self.click(locator=ProjectTeamEnterprise.DELETEBTN2)
        elif self.getElementText(locator=ProjectTeamEnterprise.MODULENAME5) == "项目参与方":
            self.click(locator=ProjectTeamEnterprise.DELETEBTN5)
        elif self.getElementText(locator=ProjectTeamEnterprise.MODULENAME4) == "项目参与方":
            self.click(locator=ProjectTeamEnterprise.DELETEBTN4)

    @timeDecorator(1)
    def clickCLoseButton(self):
        """
        点击右上角关闭按钮.
        :return: 关闭项目参与方页面
        """

        if self.getElementText(locator=ProjectTeamEnterprise.MODULENAME3) == "项目参与方":
            self.click(locator=ProjectTeamEnterprise.CLOSEBTN3)
        elif self.getElementText(locator=ProjectTeamEnterprise.MODULENAME2) == "项目参与方":
            self.click(locator=ProjectTeamEnterprise.CLOSEBTN2)
        elif self.getElementText(locator=ProjectTeamEnterprise.MODULENAME5) == "项目参与方":
            self.click(locator=ProjectTeamEnterprise.CLOSEBTN5)
        elif self.getElementText(locator=ProjectTeamEnterprise.MODULENAME4) == "项目参与方":
            self.click(locator=ProjectTeamEnterprise.CLOSEBTN4)

    @timeDecorator(1)
    def getDeleteMsg(self):
        """
        获取删除操作时弹出的提示内容.
        :return: 提示信息内容
        """

        if self.getElementText(locator=ProjectTeamEnterprise.ENTERPRISEDELETECANCELBTN5) == "取消":
            return self.getElementText(locator=ProjectTeamEnterprise.ENTERPRISEDELETEMSG5)
        elif self.getElementText(locator=ProjectTeamEnterprise.ENTERPRISEDELETECANCELBTN6) == "取消":
            return self.getElementText(locator=ProjectTeamEnterprise.ENTERPRISEDELETEMSG6)

    @timeDecorator(1)
    def clickDeleteOKButton(self):
        """
        在弹出的删除确认框中点击确定取消删除.
        :return: 删除参与方
        """

        if self.getElementText(locator=ProjectTeamEnterprise.ENTERPRISEDELETECANCELBTN5) == "取消":
            self.click(locator=ProjectTeamEnterprise.ENTERPRISEDELETEOKBTN5)
        elif self.getElementText(locator=ProjectTeamEnterprise.ENTERPRISEDELETECANCELBTN6) == "取消":
            self.click(locator=ProjectTeamEnterprise.ENTERPRISEDELETEOKBTN6)

    @timeDecorator(1)
    def clickDeleteCancelButton(self):
        """
        在弹出的删除确认框中点击取消.
        :return: 取消删除参与方
        """

        if self.getElementText(locator=ProjectTeamEnterprise.ENTERPRISEDELETECANCELBTN5) == "取消":
            self.click(locator=ProjectTeamEnterprise.ENTERPRISEDELETECANCELBTN5)
        elif self.getElementText(locator=ProjectTeamEnterprise.ENTERPRISEDELETECANCELBTN6) == "取消":
            self.click(locator=ProjectTeamEnterprise.ENTERPRISEDELETECANCELBTN6)

    @timeDecorator(1)
    def clickDeleteCloseButton(self):
        """
        在弹出的删除确认框中点击右上角关闭.
        :return: 取消删除参与方
        """

        if self.getElementText(locator=ProjectTeamEnterprise.ENTERPRISEDELETECANCELBTN5) == "取消":
            self.click(locator=ProjectTeamEnterprise.ENTERPRISEDELETECLOSEBTN5)
        elif self.getElementText(locator=ProjectTeamEnterprise.ENTERPRISEDELETECANCELBTN6) == "取消":
            self.click(locator=ProjectTeamEnterprise.ENTERPRISEDELETECLOSEBTN6)

    @timeDecorator(1)
    def getToastMsg(self):
        """
        获取toast提示信息.
        :return: toast提示信息
        """

        return self.getElementText(locator=ProjectTeamEnterprise.ENTERPRISELISTTOAST)

    @timeDecorator(1)
    def closeToast(self):
        """
        关闭toast提示信息.
        """

        self.click(locator=ProjectTeamEnterprise.ENTERPRISELISTTOASTCLOSE)

    # 流程类操作
    # 删除参与方
    def saveDeleteEnterprise(self):
        """
        删除第一个参与方全流程.
        """

        self.selectFirstEnterprise()
        self.clickDeleteButton()
        self.clickDeleteOKButton()

    def cancelDeleteEnterpriseByCancelButton(self):
        """
        通过取消按钮取消删除参与方全流程.
        """

        self.selectFirstEnterprise()
        self.clickDeleteButton()
        self.clickDeleteCancelButton()

    def cancelDeleteEnterpriseByCloseButton(self):
        """
        通过右上角关闭按钮取消删除参与方全流程.
        :return:
        """

        self.selectFirstEnterprise()
        self.clickDeleteButton()
        self.clickDeleteCloseButton()
