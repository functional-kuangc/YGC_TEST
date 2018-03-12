# coding: utf-8
def getProjectXpathByIndex(index=1):
    """
    根据项目列表索引获取项目的xpath.
    :param index: 项目列表索引
    :return: 项目单选xpath
    """

    return ".//*[@id='app']/div/div/div/div[2]/div/div/div/span/div/table/tbody/tr[" + str(index) + "]/td[1]"


def getProjectCodeXpathByIndex(index=1):
    """
    根据项目列表索引获取项目的项目编码xpath.
    :param index: 项目列表索引
    :return: 项目编码xpath
    """

    return ".//*[@id='app']/div/div/div/div[2]/div/div/div/span/div/table/tbody/tr[" + str(index) + "]/td[2]"


def getProjectNameXpathByIndex(index=1):
    """
    根据项目列表索引获取项目的项目名称xpath.
    :param index: 项目列表索引
    :return: 项目名称xpath
    """

    return ".//*[@id='app']/div/div/div/div[2]/div/div/div/span/div/table/tbody/tr[" + str(index) + "]/td[3]"


def getProjectManagerXpathByIndex(index=1):
    """
    根据项目列表索引获取项目的项目经理xpath.
    :param index: 项目列表索引
    :return: 项目经理xpath
    """

    return ".//*[@id='app']/div/div/div/div[2]/div/div/div/span/div/table/tbody/tr[" + str(index) + "]/td[4]"


def getProjectApprovalDateXpathByIndex(index=1):
    """
    根据项目列表索引获取项目的立项日期xpath.
    :param index: 项目列表索引
    :return: 立项日期xpath
    """

    return ".//*[@id='app']/div/div/div/div[2]/div/div/div/span/div/table/tbody/tr[" + str(index) + "]/td[5]"


def getProjectEndDateXpathByIndex(index=1):
    """
    根据项目列表索引获取项目的结束日期xpath.
    :param index: 项目列表索引
    :return: 结束日期xpath
    """

    return ".//*[@id='app']/div/div/div/div[2]/div/div/div/span/div/table/tbody/tr[" + str(index) + "]/td[6]"


def getProjectDescriptionXpathByIndex(index=1):
    """
    根据项目列表索引获取项目的项目描述xpath.
    :param index: 项目列表索引
    :return: 项目描述xpath
    """

    return ".//*[@id='app']/div/div/div/div[2]/div/div/div/span/div/table/tbody/tr[" + str(index) + "]/td[7]"


class Project:
    """项目档案元素定位"""

    # 第一个项目档案信息
    FIRSTPROJECTRADIOBTN = ("xpath", getProjectXpathByIndex(1))  # 单选框
    FIRSTPROJECTCODE = ("xpath", getProjectCodeXpathByIndex(1))  # 项目编码
    FIRSTPROJECTNAME = ("xpath", getProjectNameXpathByIndex(1))  # 项目名称
    FIRSTPROJECTMANAGER = ("xpath", getProjectManagerXpathByIndex(1))  # 项目经理
    FIRSTPROJECTAPPROVALDATE = ("xpath", getProjectApprovalDateXpathByIndex(1))  # 立项日期
    FIRSTPROJECTENDDATE = ("xpath", getProjectEndDateXpathByIndex(1))  # 结束日期
    FIRSTPROJECTDESCRIPTION = ("xpath", getProjectDescriptionXpathByIndex(1))  # 项目描述

    # 标题行
    MODULENAME = ("xpath", ".//*[@id='app']/div/div/div/div[1]/div[1]/h4")  # 模块名称
    SEARCHINPUT = ("xpath", ".//*[@id='app']/div/div/div/div[1]/div[2]/input")  # 搜索框
    SEARCHBTN = ("xpath", ".//*[@id='app']/div/div/div/div[1]/div[2]/button")  # 搜索按钮
    CREATEBTN = ("xpath", ".//*[@id='app']/div/div/div/div[1]/div[3]/button[1]")  # 创建按钮
    ENTERPRISEBTN = ("xpath", ".//*[@id='app']/div/div/div/div[1]/div[3]/button[2]")  # 项目参与方按钮
    MEMBERBTN = ("xpath", ".//*[@id='app']/div/div/div/div[1]/div[3]/button[3]")  # 项目团队按钮
    EDITBTN = ("xpath", ".//*[@id='app']/div/div/div/div[1]/div[3]/button[4]")  # 编辑按钮
    ENDBTN = ("xpath", ".//*[@id='app']/div/div/div/div[1]/div[3]/button[5]")  # 结束按钮
    DELETEBTN = ("xpath", ".//*[@id='app']/div/div/div/div[1]/div[3]/button[6]")  # 删除按钮
