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
    SINGLEENTERPRISETYPE2 = ("xpath", )
    SINGLEENTERPRISENAME2 = ("xpath", )
    SINGLEENTERPRISEOPERATION2 = ("xpath", )

    SINGLEENTERPRISETYPE3 = ("xpath", )
    SINGLEENTERPRISENAME3 = ("xpath", )
    SINGLEENTERPRISEOPERATION3 = ("xpath", )

    # 多行参与方
    # 第一个参与方信息
    # 参与方类型控件组
    FIRSTENTERPRISETYPE2 = ("xpath", getEnterpriseTypeXpathByIndex(index=1, div=2))  # 参与方类型

    FIRSTENTERPRISENAME2 = ("xpath", getEnterpriseTypeXpathByIndex(index=1, div=2))  # 参与方企业名称

    FIRSTENTERPRISETYPE3 = ("xpath", getEnterpriseTypeXpathByIndex(index=1, div=3))  # 参与方类型
    FIRSTENTERPRISENAME3 = ("xpath", getEnterpriseTypeXpathByIndex(index=1, div=3))  # 参与方企业名称

    # 第二个参与方信息

    # 标题行
    MODULENAME2 = ("xpath", ENTERPRISECOMMONXPATH2 + "/div[1]/h4")  # 模块名称
    DELETEBTN2 = ("xpath", ENTERPRISECOMMONXPATH2 + "/div[2]/div[1]/button[1]")  # 删除按钮
    ADDBTN2 = ("xpath", ENTERPRISECOMMONXPATH2 + "/div[2]/div[1]/button[2]")  # 添加按钮
    CLOSEBTN2 = ("xpath", ENTERPRISECOMMONXPATH2 + "/div[1]/button")  # 右上角关闭按钮

    MODULENAME3 = ("xpath", ENTERPRISECOMMONXPATH3 + "/div[1]/h4")  # 模块名称
    DELETEBTN3 = ("xpath", ENTERPRISECOMMONXPATH3 + "/div[2]/div[1]/button[1]")  # 删除按钮
    ADDBTN3 = ("xpath", ENTERPRISECOMMONXPATH3 + "/div[2]/div[1]/button[2]")  # 添加按钮
    CLOSEBTN3 = ("xpath", ENTERPRISECOMMONXPATH3 + "/div[1]/button")  # 右上角关闭按钮




    # 参与方选项