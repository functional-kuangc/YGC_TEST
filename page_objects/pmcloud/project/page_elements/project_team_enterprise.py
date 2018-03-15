# coding: utf-8
# 项目参与方框架公共部分xpath定位
ENTERPRISECOMMONXPATH2 = "html/body/div[2]/div/div/div/div/div/div[2]"
ENTERPRISECOMMONXPATH3 = "html/body/div[3]/div/div/div/div/div/div[2]"


def getEnterpriseTypeXpathByIndex(index=1, div=2):
    """
    根据参与方列表索引获取参与方类型的xpath.
    :param div: 项目参与方框架所属区域
    :param index: 参与方列表索引
    :return: 参与方类型的xpath
    """

    if div == 2:
        return ENTERPRISECOMMONXPATH2 + "/div[2]/div/div/span/div/table/tbody/tr[" + str(index) + "]/td[1]/a"
    elif div == 3:
        return ENTERPRISECOMMONXPATH3 + "/div[2]/div/div/span/div/table/tbody/tr[" + str(index) + "]/td[1]/a"


def getEnterpriseNameXpathByIndex(index=1, div=2):
    """
    根据参与方列表索引获取参与方企业名称的xpath
    :param index: 参与方列表索引
    :return: 参与方企业名称的xpath
    """



class ProjectTeamEnterprise:
    """项目参与方元素定位"""

    # 第一个参与方信息