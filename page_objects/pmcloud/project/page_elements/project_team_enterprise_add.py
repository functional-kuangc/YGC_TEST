# coding: utf-8
# 添加参与企业框架公共部分xpath定位
ENTERPRISECOMMONXPATH3 = "html/body/div[3]/div/div/div/div"
ENTERPRISECOMMONXPATH4 = "html/body/div[4]/div/div/div/div"


def getEnterpriseAddListHeadXpathByIndex(index=1, div=3):
    """
    根据添加参与企业列表列的索引获取表头字段的xpath
    :param div: 添加参与企业框架所属区域
    :param index: 添加参与企业列表列的索引
    :return: 表头字段的xpath
    """

    if div == 3:
        return ENTERPRISECOMMONXPATH3 + "/div[2]/div/div[2]/div/div/span/div[1]/table/thead/tr/th[" + str(index) + "]"
    elif div == 4:
        return ENTERPRISECOMMONXPATH4 + "/div[2]/div/div[2]/div/div/span/div[1]/table/thead/tr/th[" + str(index) + "]"


def getEnterpriseAddTypeXpathByIndex(index=1, div=3):
    """
    根据添加参与企业列表索引获取参与方类型的xpath.
    :param div: 添加参与企业框架所属区域
    :param index: 添加参与企业列表索引
    :return: 参与方类型的xpath
    """

    if div == 3:
        return ENTERPRISECOMMONXPATH3 + "/div[2]/div/div[2]/div/div/span/div[2]/table/tbody/tr[" + str(index) + "]/td[1]"
    elif div == 4:
        return ENTERPRISECOMMONXPATH4 + "/div[2]/div/div[2]/div/div/span/div[2]/table/tbody/tr[" + str(index) + "]/td[1]"


def getEnterpriseAddNameXpathByIndex(index=1, div=3):
    """
    根据添加参与企业列表索引获取参与方企业名称的xpath
    :param div: 添加参与企业框架所属区域
    :param index: 添加参与企业列表索引
    :return: 参与方企业名称的xpath
    """

    if div == 3:
        return ENTERPRISECOMMONXPATH3 + "/div[2]/div/div[2]/div/div/span/div[2]/table/tbody/tr[" + str(index) + "]/td[2]"
    elif div == 4:
        return ENTERPRISECOMMONXPATH4 + "/div[2]/div/div[2]/div/div/span/div[2]/table/tbody/tr[" + str(index) + "]/td[2]"


def getEnterpriseAddOperationXpathByIndex(index=1, div=3):
    """
    根据添加参与企业列表索引获取参与方操作的xpath
    :param div: 添加参与企业框架所属区域
    :param index: 添加参与企业列表索引
    :return: 参与方操作的xpath
    """

    if div == 3:
        return ENTERPRISECOMMONXPATH3 + "/div[2]/div/div[2]/div/div/span/div[2]/table/tbody/tr[" + str(index) + "]/td[3]"
    elif div == 4:
        return ENTERPRISECOMMONXPATH4 + "/div[2]/div/div[2]/div/div/span/div[2]/table/tbody/tr[" + str(index) + "]/td[3]"


class ProjectTeamEnterprise:
    """添加参与企业元素定位"""

    # 添加参与企业列表字段
    ENTERPRISETYPETEXT3 = ("xpath", getEnterpriseAddListHeadXpathByIndex(index=1, div=3))  # 参与方类型字段
    ENTERPRISENAMETEXT3 = ("xpath", getEnterpriseAddListHeadXpathByIndex(index=2, div=3))  # 参与方企业名称字段

    ENTERPRISETYPETEXT4 = ("xpath", getEnterpriseAddListHeadXpathByIndex(index=1, div=4))  # 参与方类型字段
    ENTERPRISENAMETEXT4 = ("xpath", getEnterpriseAddListHeadXpathByIndex(index=2, div=4))  # 参与方企业名称字段

    # 添加参与企业列表提示信息
    ENTERPRISELISTMSG = ("xpath", "html/body/div[4]/div/div/div/div/div[2]/div/div[2]/div/div/div")  # 参与方列表提示信息

    # 单行参与方
    SINGLEENTERPRISENAME3 = ("xpath", ENTERPRISECOMMONXPATH3 + "/div[2]/div/div[2]/div/div/span/div[2]/table/tbody/tr/td[2]")
    SINGLEENTERPRISEOPERATION3 = ("xpath", ENTERPRISECOMMONXPATH3 + "/div[2]/div/div[2]/div/div/span/div[2]/table/tbody/tr/td[3]")

    SINGLEENTERPRISENAME4 = ("xpath", ENTERPRISECOMMONXPATH4 + "/div[2]/div/div[2]/div/div/span/div[2]/table/tbody/tr/td[2]")
    SINGLEENTERPRISEOPERATION4 = ("xpath", ENTERPRISECOMMONXPATH4 + "/div[2]/div/div[2]/div/div/span/div[2]/table/tbody/tr/td[3]")

    # 多行参与方
    # 第一个参与方信息
    FIRSTENTERPRISENAME3 = ("xpath", getEnterpriseAddNameXpathByIndex(index=1, div=3))
    FIRSTENTERPRISEOPERATION3 = ("xpath", getEnterpriseAddOperationXpathByIndex(index=1, div=3) + "/a/span")

    FIRSTENTERPRISENAME4 = ("xpath", getEnterpriseAddNameXpathByIndex(index=1, div=4))
    FIRSTENTERPRISEOPERATION4 = ("xpath", getEnterpriseAddOperationXpathByIndex(index=1, div=4) + "/a/span")

    # 第二个参与方信息
    SECONDENTERPRISENAME3 = ("xpath", getEnterpriseAddNameXpathByIndex(index=2, div=3))
    SECONDENTERPRISEOPERATION3 = ("xpath", getEnterpriseAddOperationXpathByIndex(index=2, div=3) + "/a/span")

    SECONDENTERPRISENAME4 = ("xpath", getEnterpriseAddNameXpathByIndex(index=2, div=4))
    SECONDENTERPRISEOPERATION4 = ("xpath", getEnterpriseAddOperationXpathByIndex(index=2, div=4) + "/a/span")

    # 参与方类型控件组
    # 单行参与方
    SINGLEENTERPRISETYPE3 = ("xpath", ENTERPRISECOMMONXPATH3 + "/div[2]/div/div[2]/div/div/span/div[2]/table/tbody/tr/td[1]/div/div/span")
    SINGLEENTERPRISETYPESELECTYZ4 = ("xpath", "html/body/div[4]/div/div/div/ul/li[1]")  # 选择业主方
    SINGLEENTERPRISETYPESELECTSG4 = ("xpath", "html/body/div[4]/div/div/div/ul/li[2]")  # 选择施工方
    SINGLEENTERPRISETYPESELECTJL4 = ("xpath", "html/body/div[4]/div/div/div/ul/li[3]")  # 选择监理方

    SINGLEENTERPRISETYPE4 = ("xpath", ENTERPRISECOMMONXPATH4 + "/div[2]/div/div[2]/div/div/span/div[2]/table/tbody/tr/td[1]/div/div/span")
    SINGLEENTERPRISETYPESELECTYZ5 = ("xpath", "html/body/div[5]/div/div/div/ul/li[1]")  # 选择业主方
    SINGLEENTERPRISETYPESELECTSG5 = ("xpath", "html/body/div[5]/div/div/div/ul/li[2]")  # 选择施工方
    SINGLEENTERPRISETYPESELECTJL5 = ("xpath", "html/body/div[5]/div/div/div/ul/li[3]")  # 选择监理方

    # 多行参与方
    # 第一个参与方
    FIRSTENTERPRISETYPE3 = ("xpath", getEnterpriseAddTypeXpathByIndex(index=1, div=3) + "/div/div/span")
    FIRSTENTERPRISETYPESELECTYZ4 = ("xpath", "html/body/div[4]/div/div/div/ul/li[1]")  # 选择业主方
    FIRSTENTERPRISETYPESELECTSG4 = ("xpath", "html/body/div[4]/div/div/div/ul/li[2]")  # 选择施工方
    FIRSTENTERPRISETYPESELECTJL4 = ("xpath", "html/body/div[4]/div/div/div/ul/li[3]")  # 选择监理方

    FIRSTENTERPRISETYPE4 = ("xpath", getEnterpriseAddTypeXpathByIndex(index=1, div=4) + "/div/div/span")
    FIRSTENTERPRISETYPESELECTYZ5 = ("xpath", "html/body/div[5]/div/div/div/ul/li[1]")  # 选择业主方
    FIRSTENTERPRISETYPESELECTSG5 = ("xpath", "html/body/div[5]/div/div/div/ul/li[2]")  # 选择施工方
    FIRSTENTERPRISETYPESELECTJL5 = ("xpath", "html/body/div[5]/div/div/div/ul/li[3]")  # 选择监理方

    # 第二个参与方
    SECONDENTERPRISETYPE3 = ("xpath", getEnterpriseAddTypeXpathByIndex(index=2, div=3) + "/div/div/span")
    SECONDENTERPRISETYPESELECTYZ5 = ("xpath", "html/body/div[5]/div/div/div/ul/li[1]")  # 选择业主方
    SECONDENTERPRISETYPESELECTSG5 = ("xpath", "html/body/div[5]/div/div/div/ul/li[2]")  # 选择施工方
    SECONDENTERPRISETYPESELECTJL5 = ("xpath", "html/body/div[5]/div/div/div/ul/li[3]")  # 选择监理方

    SECONDENTERPRISETYPE4 = ("xpath", getEnterpriseAddTypeXpathByIndex(index=2, div=4) + "/div/div/span")
    SECONDENTERPRISETYPESELECTYZ6 = ("xpath", "html/body/div[6]/div/div/div/ul/li[1]")  # 选择业主方
    SECONDENTERPRISETYPESELECTSG6 = ("xpath", "html/body/div[6]/div/div/div/ul/li[2]")  # 选择施工方
    SECONDENTERPRISETYPESELECTJL6 = ("xpath", "html/body/div[6]/div/div/div/ul/li[3]")  # 选择监理方

    # 标题行
    MODULENAME3 = ("xpath", ENTERPRISECOMMONXPATH3 + "/div[1]")  # 模块名称
    CLOSEBTN3 = ("xpath", ENTERPRISECOMMONXPATH3 + "/div[1]/button")  # 右上角关闭按钮


    MODULENAME4 = ("xpath", ENTERPRISECOMMONXPATH4 + "/div[1]")  # 模块名称
    CLOSEBTN4 = ("xpath", ENTERPRISECOMMONXPATH4 + "/div[1]/button")  # 右上角关闭按钮

