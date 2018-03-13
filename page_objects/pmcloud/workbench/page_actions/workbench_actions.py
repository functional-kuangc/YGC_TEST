# coding: utf-8
# 导入公共函数Selenium封装类
from libs.pagepubselenium import PagePubSelenium
# 导入友工程后台外框架元素定位
from page_objects.pmcloud.workbench.page_elements.workbench import Workbench
# 导入页面等待装饰器
from libs.timedecorator import timeDecorator


class WorkbenchActions(PagePubSelenium):
    """友工程后台外框架操作类"""

    def getCurrentUser(self):
        """
        获取当前登录用户名.
        :return: 用户名昵称
        """

        return self.getElementText(locator=Workbench.USERNAME)

    @timeDecorator(1)
    def clickSelect(self):
        """
        点击下拉框.
        :return: 下拉框展开
        """

        self.click(locator=Workbench.SELECT)

    @timeDecorator(1)
    def logout(self):
        """
        注销.
        :return: 退出登录
        """

        self.clickSelect()
        self.click(locator=Workbench.LOGOUT)

    @timeDecorator(1)
    def clickProject(self):
        """
        点击项目档案.
        :return: 跳转到项目档案页面.
        """

        self.click(locator=Workbench.PROJECT)

    @timeDecorator(1)
    def moveMouseToBasicArchives(self):
        """
        鼠标悬停在基础档案.
        :return: 展开基础档案后面的菜单
        """

        self.moveMouseToElement(locator=Workbench.BASICARCHIVES)

    @timeDecorator(1)
    def clickProduce(self):
        """
        点击工序.
        :return: 跳转到工序页面
        """

        self.moveMouseToBasicArchives()
        self.click(locator=Workbench.PRODUCE)

    @timeDecorator(1)
    def clickWorkQuality(self):
        """
        点击质量标准.
        :return: 跳转到质量标准页面
        """

        self.moveMouseToBasicArchives()
        self.click(locator=Workbench.WORKQUALITY)

    @timeDecorator(1)
    def clickProblemReason(self):
        """
        点击问题原因.
        :return: 跳转到问题原因页面
        """

        self.moveMouseToBasicArchives()
        self.click(locator=Workbench.PROBLEMREASON)

    @timeDecorator(1)
    def clickContactType(self):
        """
        点击联系类型.
        :return: 跳转到联系类型页面
        """

        self.moveMouseToBasicArchives()
        self.click(locator=Workbench.CONTACTTYPE)

    @timeDecorator(1)
    def switchToIframe(self):
        """
        切换到内嵌iframe网页.
        """

        self.switchToFrame(locator=Workbench.IFRAME)

    @timeDecorator(1)
    def switchBackToFrame(self):
        """
        切换回外框架.
        """

        self.switchToDefaultContent()
