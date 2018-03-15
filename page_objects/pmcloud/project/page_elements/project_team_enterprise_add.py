# coding: utf-8

__author__ = "sunxr"
__version__ = "V1.0"


# 添加参与企业框架公共部分xpath定位
ENTERPRISEADDCOMMONXPATH3 = "html/body/div[3]/div/div/div/div"
ENTERPRISEADDCOMMONXPATH4 = "html/body/div[4]/div/div/div/div"
ENTERPRISEADDCOMMONXPATH5 = "html/body/div[5]/div/div/div/div"
ENTERPRISEADDCOMMONXPATH6 = "html/body/div[6]/div/div/div/div"


def getEnterpriseAddListHeadXpathByIndex(index=1, div=3):
    """
    根据添加参与企业列表列的索引获取表头字段的xpath.
    :param div: 添加参与企业框架所属区域
    :param index: 添加参与企业列表列的索引
    :return: 表头字段的xpath
    """

    if div == 3:
        return ENTERPRISEADDCOMMONXPATH3 + "/div[2]/div/div[2]/div/div/span/div[1]/table/thead/tr/th[" + str(index) + "]"
    elif div == 4:
        return ENTERPRISEADDCOMMONXPATH4 + "/div[2]/div/div[2]/div/div/span/div[1]/table/thead/tr/th[" + str(index) + "]"
    elif div == 5:
        return ENTERPRISEADDCOMMONXPATH5 + "/div[2]/div/div[2]/div/div/span/div[1]/table/thead/tr/th[" + str(index) + "]"
    elif div == 6:
        return ENTERPRISEADDCOMMONXPATH6 + "/div[2]/div/div[2]/div/div/span/div[1]/table/thead/tr/th[" + str(index) + "]"


def getEnterpriseAddTypeXpathByIndex(index=1, div=3):
    """
    根据添加参与企业列表索引获取参与方类型的xpath.
    :param div: 添加参与企业框架所属区域
    :param index: 添加参与企业列表索引
    :return: 参与方类型的xpath
    """

    if div == 3:
        return ENTERPRISEADDCOMMONXPATH3 + "/div[2]/div/div[2]/div/div/span/div[2]/table/tbody/tr[" + str(index) + "]/td[1]"
    elif div == 4:
        return ENTERPRISEADDCOMMONXPATH4 + "/div[2]/div/div[2]/div/div/span/div[2]/table/tbody/tr[" + str(index) + "]/td[1]"
    elif div == 5:
        return ENTERPRISEADDCOMMONXPATH5 + "/div[2]/div/div[2]/div/div/span/div[2]/table/tbody/tr[" + str(index) + "]/td[1]"
    elif div == 6:
        return ENTERPRISEADDCOMMONXPATH6 + "/div[2]/div/div[2]/div/div/span/div[2]/table/tbody/tr[" + str(index) + "]/td[1]"


def getEnterpriseAddNameXpathByIndex(index=1, div=3):
    """
    根据添加参与企业列表索引获取参与方企业名称的xpath.
    :param div: 添加参与企业框架所属区域
    :param index: 添加参与企业列表索引
    :return: 参与方企业名称的xpath
    """

    if div == 3:
        return ENTERPRISEADDCOMMONXPATH3 + "/div[2]/div/div[2]/div/div/span/div[2]/table/tbody/tr[" + str(index) + "]/td[2]"
    elif div == 4:
        return ENTERPRISEADDCOMMONXPATH4 + "/div[2]/div/div[2]/div/div/span/div[2]/table/tbody/tr[" + str(index) + "]/td[2]"
    elif div == 5:
        return ENTERPRISEADDCOMMONXPATH5 + "/div[2]/div/div[2]/div/div/span/div[2]/table/tbody/tr[" + str(index) + "]/td[2]"
    elif div == 6:
        return ENTERPRISEADDCOMMONXPATH6 + "/div[2]/div/div[2]/div/div/span/div[2]/table/tbody/tr[" + str(index) + "]/td[2]"


def getEnterpriseAddOperationXpathByIndex(index=1, div=3):
    """
    根据添加参与企业列表索引获取参与方操作的xpath.
    :param div: 添加参与企业框架所属区域
    :param index: 添加参与企业列表索引
    :return: 参与方操作的xpath
    """

    if div == 3:
        return ENTERPRISEADDCOMMONXPATH3 + "/div[2]/div/div[2]/div/div/span/div[2]/table/tbody/tr[" + str(index) + "]/td[3]"
    elif div == 4:
        return ENTERPRISEADDCOMMONXPATH4 + "/div[2]/div/div[2]/div/div/span/div[2]/table/tbody/tr[" + str(index) + "]/td[3]"
    elif div == 5:
        return ENTERPRISEADDCOMMONXPATH5 + "/div[2]/div/div[2]/div/div/span/div[2]/table/tbody/tr[" + str(index) + "]/td[3]"
    elif div == 6:
        return ENTERPRISEADDCOMMONXPATH6 + "/div[2]/div/div[2]/div/div/span/div[2]/table/tbody/tr[" + str(index) + "]/td[3]"


def getEnterpriseAddToastXpath(div=4):
    """
    获取参与企业页面下的Toast提示信息的xpath.
    :param div: Toast提示所属区域
    :return: Toast提示信息的xpath
    """

    return "html/body/div[" + str(div) + "]/div/span/div/div/div/div/div[2]"


def getEnterpriseAddToastCloseXpath(div=4):
    """
    获取参与企业页面下的Toast提示关闭按钮的xpath.
    :param div: Toast提示所属区域
    :return: Toast提示关闭按钮的xpath
    """

    return "html/body/div[" + str(div) + "]/div/span/div/a/span"


class ProjectTeamEnterpriseAdd:
    """添加参与企业元素定位"""

    # 添加参与企业列表字段
    ENTERPRISETYPETEXT3 = ("xpath", getEnterpriseAddListHeadXpathByIndex(index=1, div=3))  # 参与方类型字段
    ENTERPRISENAMETEXT3 = ("xpath", getEnterpriseAddListHeadXpathByIndex(index=2, div=3))  # 参与方企业名称字段

    ENTERPRISETYPETEXT4 = ("xpath", getEnterpriseAddListHeadXpathByIndex(index=1, div=4))  # 参与方类型字段
    ENTERPRISENAMETEXT4 = ("xpath", getEnterpriseAddListHeadXpathByIndex(index=2, div=4))  # 参与方企业名称字段

    ENTERPRISETYPETEXT5 = ("xpath", getEnterpriseAddListHeadXpathByIndex(index=1, div=5))  # 参与方类型字段
    ENTERPRISENAMETEXT5 = ("xpath", getEnterpriseAddListHeadXpathByIndex(index=2, div=5))  # 参与方企业名称字段

    ENTERPRISETYPETEXT6 = ("xpath", getEnterpriseAddListHeadXpathByIndex(index=1, div=6))  # 参与方类型字段
    ENTERPRISENAMETEXT6 = ("xpath", getEnterpriseAddListHeadXpathByIndex(index=2, div=6))  # 参与方企业名称字段

    # 添加参与企业列表提示信息
    ENTERPRISELISTMSG3 = ("xpath", ENTERPRISEADDCOMMONXPATH3 + "/div[2]/div/div[2]/div/div/div")  # 参与方列表提示信息
    ENTERPRISELISTMSG4 = ("xpath", ENTERPRISEADDCOMMONXPATH4 + "/div[2]/div/div[2]/div/div/div")  # 参与方列表提示信息
    ENTERPRISELISTMSG5 = ("xpath", ENTERPRISEADDCOMMONXPATH5 + "/div[2]/div/div[2]/div/div/div")  # 参与方列表提示信息
    ENTERPRISELISTMSG6 = ("xpath", ENTERPRISEADDCOMMONXPATH6 + "/div[2]/div/div[2]/div/div/div")  # 参与方列表提示信息

    # 单行参与方
    SINGLEENTERPRISENAME3 = ("xpath", ENTERPRISEADDCOMMONXPATH3 + "/div[2]/div/div[2]/div/div/span/div[2]/table/tbody/tr/td[2]")
    SINGLEENTERPRISEOPERATION3 = ("xpath", ENTERPRISEADDCOMMONXPATH3 + "/div[2]/div/div[2]/div/div/span/div[2]/table/tbody/tr/td[3]")

    SINGLEENTERPRISENAME4 = ("xpath", ENTERPRISEADDCOMMONXPATH4 + "/div[2]/div/div[2]/div/div/span/div[2]/table/tbody/tr/td[2]")
    SINGLEENTERPRISEOPERATION4 = ("xpath", ENTERPRISEADDCOMMONXPATH4 + "/div[2]/div/div[2]/div/div/span/div[2]/table/tbody/tr/td[3]")

    SINGLEENTERPRISENAME5 = ("xpath", ENTERPRISEADDCOMMONXPATH5 + "/div[2]/div/div[2]/div/div/span/div[2]/table/tbody/tr/td[2]")
    SINGLEENTERPRISEOPERATION5 = ("xpath", ENTERPRISEADDCOMMONXPATH5 + "/div[2]/div/div[2]/div/div/span/div[2]/table/tbody/tr/td[3]")

    SINGLEENTERPRISENAME6 = ("xpath", ENTERPRISEADDCOMMONXPATH6 + "/div[2]/div/div[2]/div/div/span/div[2]/table/tbody/tr/td[2]")
    SINGLEENTERPRISEOPERATION6 = ("xpath", ENTERPRISEADDCOMMONXPATH6 + "/div[2]/div/div[2]/div/div/span/div[2]/table/tbody/tr/td[3]")

    # 多行参与方
    # 第一个参与方信息
    FIRSTENTERPRISENAME3 = ("xpath", getEnterpriseAddNameXpathByIndex(index=1, div=3))
    FIRSTENTERPRISEOPERATION3 = ("xpath", getEnterpriseAddOperationXpathByIndex(index=1, div=3))

    FIRSTENTERPRISENAME4 = ("xpath", getEnterpriseAddNameXpathByIndex(index=1, div=4))
    FIRSTENTERPRISEOPERATION4 = ("xpath", getEnterpriseAddOperationXpathByIndex(index=1, div=4))

    FIRSTENTERPRISENAME5 = ("xpath", getEnterpriseAddNameXpathByIndex(index=1, div=5))
    FIRSTENTERPRISEOPERATION5 = ("xpath", getEnterpriseAddOperationXpathByIndex(index=1, div=5))

    FIRSTENTERPRISENAME6 = ("xpath", getEnterpriseAddNameXpathByIndex(index=1, div=6))
    FIRSTENTERPRISEOPERATION6 = ("xpath", getEnterpriseAddOperationXpathByIndex(index=1, div=6))

    # 第二个参与方信息
    SECONDENTERPRISENAME3 = ("xpath", getEnterpriseAddNameXpathByIndex(index=2, div=3))
    SECONDENTERPRISEOPERATION3 = ("xpath", getEnterpriseAddOperationXpathByIndex(index=2, div=3))

    SECONDENTERPRISENAME4 = ("xpath", getEnterpriseAddNameXpathByIndex(index=2, div=4))
    SECONDENTERPRISEOPERATION4 = ("xpath", getEnterpriseAddOperationXpathByIndex(index=2, div=4))

    SECONDENTERPRISENAME5 = ("xpath", getEnterpriseAddNameXpathByIndex(index=2, div=5))
    SECONDENTERPRISEOPERATION5 = ("xpath", getEnterpriseAddOperationXpathByIndex(index=2, div=5))

    SECONDENTERPRISENAME6 = ("xpath", getEnterpriseAddNameXpathByIndex(index=2, div=6))
    SECONDENTERPRISEOPERATION6 = ("xpath", getEnterpriseAddOperationXpathByIndex(index=2, div=6))

    # 参与方类型控件组
    # 单行参与方
    SINGLEENTERPRISETYPE3 = ("xpath", ENTERPRISEADDCOMMONXPATH3 + "/div[2]/div/div[2]/div/div/span/div[2]/table/tbody/tr/td[1]/div/div/span")
    SINGLEENTERPRISETYPESELECTYZ4 = ("xpath", "html/body/div[4]/div/div/div/ul/li[1]")  # 选择业主方
    SINGLEENTERPRISETYPESELECTSG4 = ("xpath", "html/body/div[4]/div/div/div/ul/li[2]")  # 选择施工方
    SINGLEENTERPRISETYPESELECTJL4 = ("xpath", "html/body/div[4]/div/div/div/ul/li[3]")  # 选择监理方

    SINGLEENTERPRISETYPE4 = ("xpath", ENTERPRISEADDCOMMONXPATH4 + "/div[2]/div/div[2]/div/div/span/div[2]/table/tbody/tr/td[1]/div/div/span")
    SINGLEENTERPRISETYPESELECTYZ5 = ("xpath", "html/body/div[5]/div/div/div/ul/li[1]")  # 选择业主方
    SINGLEENTERPRISETYPESELECTSG5 = ("xpath", "html/body/div[5]/div/div/div/ul/li[2]")  # 选择施工方
    SINGLEENTERPRISETYPESELECTJL5 = ("xpath", "html/body/div[5]/div/div/div/ul/li[3]")  # 选择监理方

    SINGLEENTERPRISETYPE5 = ("xpath", ENTERPRISEADDCOMMONXPATH5 + "/div[2]/div/div[2]/div/div/span/div[2]/table/tbody/tr/td[1]/div/div/span")
    SINGLEENTERPRISETYPESELECTYZ6 = ("xpath", "html/body/div[6]/div/div/div/ul/li[1]")  # 选择业主方
    SINGLEENTERPRISETYPESELECTSG6 = ("xpath", "html/body/div[6]/div/div/div/ul/li[2]")  # 选择施工方
    SINGLEENTERPRISETYPESELECTJL6 = ("xpath", "html/body/div[6]/div/div/div/ul/li[3]")  # 选择监理方

    SINGLEENTERPRISETYPE6 = ("xpath", ENTERPRISEADDCOMMONXPATH6 + "/div[2]/div/div[2]/div/div/span/div[2]/table/tbody/tr/td[1]/div/div/span")
    SINGLEENTERPRISETYPESELECTYZ7 = ("xpath", "html/body/div[7]/div/div/div/ul/li[1]")  # 选择业主方
    SINGLEENTERPRISETYPESELECTSG7 = ("xpath", "html/body/div[7]/div/div/div/ul/li[2]")  # 选择施工方
    SINGLEENTERPRISETYPESELECTJL7 = ("xpath", "html/body/div[7]/div/div/div/ul/li[3]")  # 选择监理方

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

    FIRSTENTERPRISETYPE5 = ("xpath", getEnterpriseAddTypeXpathByIndex(index=1, div=5) + "/div/div/span")
    FIRSTENTERPRISETYPESELECTYZ6 = ("xpath", "html/body/div[6]/div/div/div/ul/li[1]")  # 选择业主方
    FIRSTENTERPRISETYPESELECTSG6 = ("xpath", "html/body/div[6]/div/div/div/ul/li[2]")  # 选择施工方
    FIRSTENTERPRISETYPESELECTJL6 = ("xpath", "html/body/div[6]/div/div/div/ul/li[3]")  # 选择监理方

    FIRSTENTERPRISETYPE6 = ("xpath", getEnterpriseAddTypeXpathByIndex(index=1, div=6) + "/div/div/span")
    FIRSTENTERPRISETYPESELECTYZ7 = ("xpath", "html/body/div[7]/div/div/div/ul/li[1]")  # 选择业主方
    FIRSTENTERPRISETYPESELECTSG7 = ("xpath", "html/body/div[7]/div/div/div/ul/li[2]")  # 选择施工方
    FIRSTENTERPRISETYPESELECTJL7 = ("xpath", "html/body/div[7]/div/div/div/ul/li[3]")  # 选择监理方

    # 第二个参与方
    SECONDENTERPRISETYPE3 = ("xpath", getEnterpriseAddTypeXpathByIndex(index=2, div=3) + "/div/div/span")
    SECONDENTERPRISETYPESELECTYZ5 = ("xpath", "html/body/div[5]/div/div/div/ul/li[1]")  # 选择业主方
    SECONDENTERPRISETYPESELECTSG5 = ("xpath", "html/body/div[5]/div/div/div/ul/li[2]")  # 选择施工方
    SECONDENTERPRISETYPESELECTJL5 = ("xpath", "html/body/div[5]/div/div/div/ul/li[3]")  # 选择监理方

    SECONDENTERPRISETYPE4 = ("xpath", getEnterpriseAddTypeXpathByIndex(index=2, div=4) + "/div/div/span")
    SECONDENTERPRISETYPESELECTYZ6 = ("xpath", "html/body/div[6]/div/div/div/ul/li[1]")  # 选择业主方
    SECONDENTERPRISETYPESELECTSG6 = ("xpath", "html/body/div[6]/div/div/div/ul/li[2]")  # 选择施工方
    SECONDENTERPRISETYPESELECTJL6 = ("xpath", "html/body/div[6]/div/div/div/ul/li[3]")  # 选择监理方

    SECONDENTERPRISETYPE5 = ("xpath", getEnterpriseAddTypeXpathByIndex(index=2, div=5) + "/div/div/span")
    SECONDENTERPRISETYPESELECTYZ7 = ("xpath", "html/body/div[7]/div/div/div/ul/li[1]")  # 选择业主方
    SECONDENTERPRISETYPESELECTSG7 = ("xpath", "html/body/div[7]/div/div/div/ul/li[2]")  # 选择施工方
    SECONDENTERPRISETYPESELECTJL7 = ("xpath", "html/body/div[7]/div/div/div/ul/li[3]")  # 选择监理方

    SECONDENTERPRISETYPE6 = ("xpath", getEnterpriseAddTypeXpathByIndex(index=2, div=6) + "/div/div/span")
    SECONDENTERPRISETYPESELECTYZ8 = ("xpath", "html/body/div[8]/div/div/div/ul/li[1]")  # 选择业主方
    SECONDENTERPRISETYPESELECTSG8 = ("xpath", "html/body/div[8]/div/div/div/ul/li[2]")  # 选择施工方
    SECONDENTERPRISETYPESELECTJL8 = ("xpath", "html/body/div[8]/div/div/div/ul/li[3]")  # 选择监理方

    # 标题行
    MODULENAME3 = ("xpath", ENTERPRISEADDCOMMONXPATH3 + "/div[1]")  # 模块名称
    OKBTN3 = ("xpath", ENTERPRISEADDCOMMONXPATH3 + "/div[3]/button[2]")  # 确定按钮
    CANCELBTN3 = ("xpath", ENTERPRISEADDCOMMONXPATH3 + "/div[3]/button[1]")  # 取消按钮
    CLOSEBTN3 = ("xpath", ENTERPRISEADDCOMMONXPATH3 + "/div[1]/button")  # 右上角关闭按钮
    SEARCHINPUT3 = ("xpath", ENTERPRISEADDCOMMONXPATH3 + "/div[2]/div/div[1]/div/input")  # 搜索文本框
    SEARCHBUTTON3 = ("xpath", ENTERPRISEADDCOMMONXPATH3 + "/div[2]/div/div[1]/button")  # 搜索按钮
    SELECTSEARCHLIST31 = ("xpath", ENTERPRISEADDCOMMONXPATH3 + "/div[2]/div/div[1]/div/ul/li[1]")  # 选择第一个企业
    SELECTSEARCHLIST32 = ("xpath", ENTERPRISEADDCOMMONXPATH3 + "/div[2]/div/div[1]/div/ul/li[2]")  # 选择第二个企业

    MODULENAME4 = ("xpath", ENTERPRISEADDCOMMONXPATH4 + "/div[1]")  # 模块名称
    OKBTN4 = ("xpath", ENTERPRISEADDCOMMONXPATH4 + "/div[3]/button[2]")  # 确定按钮
    CANCELBTN4 = ("xpath", ENTERPRISEADDCOMMONXPATH4 + "/div[3]/button[1]")  # 取消按钮
    CLOSEBTN4 = ("xpath", ENTERPRISEADDCOMMONXPATH4 + "/div[1]/button")  # 右上角关闭按钮
    SEARCHINPUT4 = ("xpath", ENTERPRISEADDCOMMONXPATH4 + "/div[2]/div/div[1]/div/input")  # 搜索文本框
    SEARCHBUTTON4 = ("xpath", ENTERPRISEADDCOMMONXPATH4 + "/div[2]/div/div[1]/button")  # 搜索按钮
    SELECTSEARCHLIST41 = ("xpath", ENTERPRISEADDCOMMONXPATH4 + "/div[2]/div/div[1]/div/ul/li[1]")  # 选择第一个企业
    SELECTSEARCHLIST42 = ("xpath", ENTERPRISEADDCOMMONXPATH4 + "/div[2]/div/div[1]/div/ul/li[2]")  # 选择第二个企业

    MODULENAME5 = ("xpath", ENTERPRISEADDCOMMONXPATH5 + "/div[1]")  # 模块名称
    OKBTN5 = ("xpath", ENTERPRISEADDCOMMONXPATH5 + "/div[3]/button[2]")  # 确定按钮
    CANCELBTN5 = ("xpath", ENTERPRISEADDCOMMONXPATH5 + "/div[3]/button[1]")  # 取消按钮
    CLOSEBTN5 = ("xpath", ENTERPRISEADDCOMMONXPATH5 + "/div[1]/button")  # 右上角关闭按钮
    SEARCHINPUT5 = ("xpath", ENTERPRISEADDCOMMONXPATH5 + "/div[2]/div/div[1]/div/input")  # 搜索文本框
    SEARCHBUTTON5 = ("xpath", ENTERPRISEADDCOMMONXPATH5 + "/div[2]/div/div[1]/button")  # 搜索按钮
    SELECTSEARCHLIST51 = ("xpath", ENTERPRISEADDCOMMONXPATH5 + "/div[2]/div/div[1]/div/ul/li[1]")  # 选择第一个企业
    SELECTSEARCHLIST52 = ("xpath", ENTERPRISEADDCOMMONXPATH5 + "/div[2]/div/div[1]/div/ul/li[2]")  # 选择第二个企业

    MODULENAME6 = ("xpath", ENTERPRISEADDCOMMONXPATH6 + "/div[1]")  # 模块名称
    OKBTN6 = ("xpath", ENTERPRISEADDCOMMONXPATH6 + "/div[3]/button[2]")  # 确定按钮
    CANCELBTN6 = ("xpath", ENTERPRISEADDCOMMONXPATH6 + "/div[3]/button[1]")  # 取消按钮
    CLOSEBTN6 = ("xpath", ENTERPRISEADDCOMMONXPATH6 + "/div[1]/button")  # 右上角关闭按钮
    SEARCHINPUT6 = ("xpath", ENTERPRISEADDCOMMONXPATH6 + "/div[2]/div/div[1]/div/input")  # 搜索文本框
    SEARCHBUTTON6 = ("xpath", ENTERPRISEADDCOMMONXPATH6 + "/div[2]/div/div[1]/button")  # 搜索按钮
    SELECTSEARCHLIST61 = ("xpath", ENTERPRISEADDCOMMONXPATH6 + "/div[2]/div/div[1]/div/ul/li[1]")  # 选择第一个企业
    SELECTSEARCHLIST62 = ("xpath", ENTERPRISEADDCOMMONXPATH6 + "/div[2]/div/div[1]/div/ul/li[2]")  # 选择第二个企业

    # 添加参与企业页面下参与方的删除
    # 单行参与方
    SINGLEENTERPRISEDELETEBTN3 = ("xpath", SINGLEENTERPRISEOPERATION3[1] + "/a/span")
    SINGLEENTERPRISEDELETEBTN4 = ("xpath", SINGLEENTERPRISEOPERATION4[1] + "/a/span")
    SINGLEENTERPRISEDELETEBTN5 = ("xpath", SINGLEENTERPRISEOPERATION5[1] + "/a/span")
    SINGLEENTERPRISEDELETEBTN6 = ("xpath", SINGLEENTERPRISEOPERATION6[1] + "/a/span")

    # 多行参与方
    # 第一个参与方
    FIRSTENTERPRISEDELETEBTN3 = ("xpath", FIRSTENTERPRISEOPERATION3[1] + "/a/span")
    FIRSTENTERPRISEDELETEBTN4 = ("xpath", FIRSTENTERPRISEOPERATION4[1] + "/a/span")
    FIRSTENTERPRISEDELETEBTN5 = ("xpath", FIRSTENTERPRISEOPERATION5[1] + "/a/span")
    FIRSTENTERPRISEDELETEBTN6 = ("xpath", FIRSTENTERPRISEOPERATION6[1] + "/a/span")

    # 第二个参与方
    SECONDENTERPRISEDELETEBTN3 = ("xpath", SECONDENTERPRISEOPERATION3[1] + "/a/span")
    SECONDENTERPRISEDELETEBTN4 = ("xpath", SECONDENTERPRISEOPERATION4[1] + "/a/span")
    SECONDENTERPRISEDELETEBTN5 = ("xpath", SECONDENTERPRISEOPERATION5[1] + "/a/span")
    SECONDENTERPRISEDELETEBTN6 = ("xpath", SECONDENTERPRISEOPERATION6[1] + "/a/span")

    # 添加参与企业页面下的Toast提示信息
    ENTERPRISEADDTOAST4 = ("xpath", getEnterpriseAddToastXpath(div=4))
    ENTERPRISEADDTOASTCLOSE4 = ("xpath", getEnterpriseAddToastCloseXpath(div=4))

    ENTERPRISEADDTOAST5 = ("xpath", getEnterpriseAddToastXpath(div=5))
    ENTERPRISEADDTOASTCLOSE5 = ("xpath", getEnterpriseAddToastCloseXpath(div=5))

    ENTERPRISEADDTOAST6 = ("xpath", getEnterpriseAddToastXpath(div=6))
    ENTERPRISEADDTOASTCLOSE6 = ("xpath", getEnterpriseAddToastCloseXpath(div=6))

    ENTERPRISEADDTOAST7 = ("xpath", getEnterpriseAddToastXpath(div=7))
    ENTERPRISEADDTOASTCLOSE7 = ("xpath", getEnterpriseAddToastCloseXpath(div=7))
