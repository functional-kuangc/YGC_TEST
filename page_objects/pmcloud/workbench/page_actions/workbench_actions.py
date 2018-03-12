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
        """获取当前登录用户名"""

        return self.getElementText(locator=Workbench.USERNAME)

    @timeDecorator(1)
    def clickSelect(self):
        """点击下拉框"""

        self.click(locator=Workbench.SELECT)

    @timeDecorator(1)
    def logout(self):
        """注销"""

        self.clickSelect()
        self.click(locator=Workbench.LOGOUT)

    @timeDecorator(1)
    def clickProject(self):
        """点击项目档案"""

        self.click(locator=Workbench.PROJECT)

    @timeDecorator(1)
    def moveMouseToBasicArchives(self):
        """鼠标悬停在基础档案"""

        self.moveMouseToElement(locator=Workbench.BASICARCHIVES)

    @timeDecorator(1)
    def clickProduce(self):
        """点击工序"""

        self.moveMouseToBasicArchives()
        self.click(locator=Workbench.PRODUCE)

    @timeDecorator(1)
    def clickWorkQuality(self):
        """点击质量标准"""

        self.moveMouseToBasicArchives()
        self.click(locator=Workbench.WORKQUALITY)

    @timeDecorator(1)
    def clickProblemReason(self):
        """点击问题原因"""

        self.moveMouseToBasicArchives()
        self.click(locator=Workbench.PROBLEMREASON)

    @timeDecorator(1)
    def clickContactType(self):
        """点击联系类型"""

        self.moveMouseToBasicArchives()
        self.click(locator=Workbench.CONTACTTYPE)

    @timeDecorator(1)
    def switchToIframe(self):
        """切换到内嵌iframe网页"""

        self.switchToFrame(locator=Workbench.IFRAME)

    @timeDecorator(1)
    def switchBackToFrame(self):
        """切换回外框架"""

        self.switchToDefaultContent()
