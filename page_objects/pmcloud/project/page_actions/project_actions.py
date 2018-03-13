# coding: utf-8
# 导入公共函数Selenium封装类
from libs.pagepubselenium import PagePubSelenium
# 导入项目档案元素定位
from page_objects.pmcloud.project.page_elements.project import Project
# 导入页面等待装饰器
from libs.timedecorator import timeDecorator


class ProjectActions(PagePubSelenium):
    """项目档案操作类"""

    @timeDecorator(1)
    def clickProject(self):
        """点击项目，打开项目"""
