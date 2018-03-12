# coding: utf-8
class Workbench:
    """友工程后台外框架元素定位"""

    SELECT = ("xpath", ".//*[@id='username']/span[3]")  # 下拉按钮
    USERNAME = ("xpath", ".//*[@id='username']/span[2]")  # 当前登录用户名
    LOGOUT = ("xpath", ".//*[@id='moreMenu']/li[5]/a")  # 注销

    APPCENTER = ("xpath", "html/body/div[1]/div/ul/li[1]/a")  # 应用中心
    PROJECT = ("xpath", "html/body/div[1]/div/ul/li[2]/a")  # 项目档案
    BASICARCHIVES = ("xpath", "html/body/div[1]/div/ul/li[3]/a")  # 基础档案
    PRODUCE = ("xpath", "html/body/div[1]/div/ul/li[3]/div/ul/li[1]/a")  # 工序
    WORKQUALITY = ("xpath", "html/body/div[1]/div/ul/li[3]/div/ul/li[2]/a")  # 质量标准
    PROBLEMREASON = ("xpath", "html/body/div[1]/div/ul/li[3]/div/ul/li[3]/a")  # 问题原因
    CONTACTTYPE = ("xpath", "html/body/div[1]/div/ul/li[3]/div/ul/li[4]/a")  # 联系类型

    IFRAME = ("xpath", "/html/body/div[2]/div[1]/div/div/iframe")  # 内嵌网页
