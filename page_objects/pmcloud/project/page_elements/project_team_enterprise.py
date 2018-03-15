# coding: utf-8
# 项目参与方框架公共部分xpath定位
ENTERPRISECOMMONXPATH2 = "html/body/div[2]/div/div/div/div/div"
ENTERPRISECOMMONXPATH3 = "html/body/div[3]/div/div/div/div/div"


def getEnterpriseListHeadXpathByIndex(index=1, div=2):
    """
    根据项目参与方列表列的索引获取表头字段的xpath
    :param div: 项目参与方框架所属区域
    :param index: 项目参与方列表列的索引
    :return: 表头字段的xpath
    """

    if div == 2:
        return ENTERPRISECOMMONXPATH2 + "/div[2]/div[2]/div/div/span/div/table/thead/tr/th[" + str(index) + "]"
    elif div == 3:
        return ENTERPRISECOMMONXPATH3 + "/div[2]/div[2]/div/div/span/div/table/thead/tr/th[" + str(index) + "]"


def getEnterpriseTypeXpathByIndex(index=1, div=2):
    """
    根据参与方列表索引获取参与方类型的xpath.
    :param div: 项目参与方框架所属区域
    :param index: 参与方列表索引
    :return: 参与方类型的xpath
    """

    if div == 2:
        return ENTERPRISECOMMONXPATH2 + "/div[2]/div[2]/div/div/span/div/table/tbody/tr[" + str(index) + "]/td[1]/a"
    elif div == 3:
        return ENTERPRISECOMMONXPATH3 + "/div[2]/div[2]/div/div/span/div/table/tbody/tr[" + str(index) + "]/td[1]/a"


def getEnterpriseNameXpathByIndex(index=1, div=2):
    """
    根据参与方列表索引获取参与方企业名称的xpath
    :param div: 项目参与方框架所属区域
    :param index: 参与方列表索引
    :return: 参与方企业名称的xpath
    """

    if div == 2:
        return ENTERPRISECOMMONXPATH2 + "/div[2]/div[2]/div/div/span/div/table/tbody/tr[" + str(index) + "]/td[2]"
    elif div == 3:
        return ENTERPRISECOMMONXPATH3 + "/div[2]/div[2]/div/div/span/div/table/tbody/tr[" + str(index) + "]/td[2]"


class ProjectTeamEnterprise:
    """项目参与方元素定位"""

    # 参与方列表字段
    ENTERPRISETYPETEXT2 = ("xpath", getEnterpriseListHeadXpathByIndex(index=1, div=2))  # 参与方类型字段
    ENTERPRISENAMETEXT2 = ("xpath", getEnterpriseListHeadXpathByIndex(index=2, div=2))  # 参与方企业名称字段

    ENTERPRISETYPETEXT3 = ("xpath", getEnterpriseListHeadXpathByIndex(index=1, div=3))  # 参与方类型字段
    ENTERPRISENAMETEXT3 = ("xpath", getEnterpriseListHeadXpathByIndex(index=2, div=3))  # 参与方企业名称字段

    # 第一个参与方信息
    FIRSTENTERPRISETYPE2 = ("xpath", getEnterpriseTypeXpathByIndex(index=1, div=2))  # 参与方类型
    FIRSTENTERPRISENAME2 = ("xpath", getEnterpriseTypeXpathByIndex(index=1, div=2))  # 参与方企业名称

    FIRSTENTERPRISETYPE3 = ("xpath", getEnterpriseTypeXpathByIndex(index=1, div=3))  # 参与方类型
    FIRSTENTERPRISENAME3 = ("xpath", getEnterpriseTypeXpathByIndex(index=1, div=3))  # 参与方企业名称

    # 标题行
    MODULENAME2 = ("xpath", ENTERPRISECOMMONXPATH2 + "/div[1]/h4")  # 模块名称
    DELETEBTN2 = ("xpath", ENTERPRISECOMMONXPATH2 + "/div[2]/div[1]/button[1]")  # 删除按钮
    ADDBTN2 = ("xpath", ENTERPRISECOMMONXPATH2 + "/div[2]/div[1]/button[2]")  # 添加按钮
    CLOSEBTN2 = ("xpath", ENTERPRISECOMMONXPATH2 + "/div[1]/button")  # 右上角关闭按钮

    MODULENAME3 = ("xpath", ENTERPRISECOMMONXPATH3 + "/div[1]/h4")  # 模块名称
    DELETEBTN3 = ("xpath", ENTERPRISECOMMONXPATH3 + "/div[2]/div[1]/button[1]")  # 删除按钮
    ADDBTN3 = ("xpath", ENTERPRISECOMMONXPATH3 + "/div[2]/div[1]/button[2]")  # 添加按钮
    CLOSEBTN3 = ("xpath", ENTERPRISECOMMONXPATH3 + "/div[1]/button")  # 右上角关闭按钮

    # 项目参与方页面下的Toast提示信息
    ENTERPRISELISTTOAST = ("xpath", "html/body/div[3]/div/span/div/div/div/div/div[2]")
    ENTERPRISELISTTOASTCLOSE = ("xpath", "html/body/div[3]/div/span/div/a/span")
