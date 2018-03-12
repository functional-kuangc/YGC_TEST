# coding: utf-8
# 导入公共函数Selenium封装类
from libs.pagepubselenium import PagePubSelenium
# 导入友工程首页元素定位
from page_objects.pmcloud.index.page_elements.pmcloud_index import PMCloudIndex
# 导入页面等待装饰器
from libs.timedecorator import timeDecorator


class PMCloudIndexActions(PagePubSelenium):
    """友工程首页操作类"""

    @timeDecorator(1)
    def openPMCloudIndex(self, expected_title):
        """打开友工程首页"""

        self.openExceptedURL(expected_title=expected_title)

    @timeDecorator(1)
    def clickLoginButton(self):
        """点击登录按钮"""

        self.click(PMCloudIndex.LOGINBTN)
