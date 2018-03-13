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


def getProjectOperationXpathByIndex(index=1):
    """
    根据按钮位置索引获取项目各操作按钮xpath.
    :param index: 按钮位置索引
    :return: 操作按钮xpath
    """

    return ".//*[@id='app']/div/div/div/div[1]/div[3]/button[" + str(index) + "]"


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
    CREATEBTN = ("xpath", getProjectOperationXpathByIndex(1))  # 创建按钮
    ENTERPRISEBTN = ("xpath", getProjectOperationXpathByIndex(2))  # 项目参与方按钮
    MEMBERBTN = ("xpath", getProjectOperationXpathByIndex(3))  # 项目团队按钮
    EDITBTN = ("xpath", getProjectOperationXpathByIndex(4))  # 编辑按钮
    ENDBTN = ("xpath", getProjectOperationXpathByIndex(5))  # 结束按钮
    DELETEBTN = ("xpath", getProjectOperationXpathByIndex(6))  # 删除按钮

    # 项目信息框公共部分xpath定位
    INFOCOMMONXPATH = "html/body/div[3]/div/div/div/div/div/"

    # 项目创建
    NEWCODETEXT = ("xpath", INFOCOMMONXPATH + "div[2]/div[1]/div[1]/span")  # 项目编码字段
    NEWNAMETEXT = ("xpath", INFOCOMMONXPATH + "/div[2]/div[1]/div[2]/span")  # 项目名称字段
    NEWAPPROVALDATETEXT = ("xpath", INFOCOMMONXPATH + "/div[2]/div[2]/div[1]/span")  # 立项日期字段
    NEWMANAGERTEXT = ("xpath", INFOCOMMONXPATH + "/div[2]/div[2]/div[2]/span")  # 项目经理字段
    NEWDESCRIPTIONTEXT = ("xpath", INFOCOMMONXPATH + "/div[2]/div[3]/div[1]")  # 项目描述字段

    NEWCODEINPUT = ("xpath", INFOCOMMONXPATH + "/div[2]/div[1]/div[1]/input")  # 项目编码输入框
    NEWNAMEINPUT = ("xpath", INFOCOMMONXPATH + "/div[2]/div[1]/div[2]/input")  # 项目名称输入框
    NEWMANAGERINPUT = ("xpath", INFOCOMMONXPATH + "/div[2]/div[3]/div[2]/textarea")  # 项目经理输入框
    NEWDESCRIPTIONINPUT = ("xpath", INFOCOMMONXPATH + "/div[2]/div[3]/div[2]/textarea")  # 项目描述输入框

    # 立项日期控件组
    NEWAPPROVALDATEINPUT = ("xpath", INFOCOMMONXPATH + "/div[2]/div[2]/div[1]/div/div/input")  # 日期参照
    NEWTODAYDATE = ("xpath", "html/body/div[4]/div/div/div/div/div[2]/div[3]/span/a")  # 今天

    # 取消创建
    CANCELMSGDIV3 = ("xpath", "html/body/div[3]/div/div/div/div/div[2]")  # 取消提示信息
    CANCELMSGDIV4 = ("xpath", "html/body/div[4]/div/div/div/div/div[2]")  # 取消提示信息
    CANCELMSGDIV5 = ("xpath", "html/body/div[5]/div/div/div/div/div[2]")  # 取消提示信息

    CANCELCANCELBTN3 = ("xpath", "html/body/div[3]/div/div/div/div/div[3]/button[1]")  # 取消取消
    CANCELCANCELBTN4 = ("xpath", "html/body/div[4]/div/div/div/div/div[3]/button[1]")  # 取消取消
    CANCELCANCELBTN5 = ("xpath", "html/body/div[5]/div/div/div/div/div[3]/button[1]")  # 取消取消

    CANCELOKBTN3 = ("xpath", "html/body/div[3]/div/div/div/div/div[3]/button[2]")  # 确定取消
    CANCELOKBTN4 = ("xpath", "html/body/div[4]/div/div/div/div/div[3]/button[2]")  # 确定取消
    CANCELOKBTN5 = ("xpath", "html/body/div[5]/div/div/div/div/div[3]/button[2]")  # 确定取消

    CANCELCLOSEBTN3 = ("xpath", "html/body/div[3]/div/div/div/div/div[1]/button")  # 关闭取消
    CANCELCLOSEBTN4 = ("xpath", "html/body/div[4]/div/div/div/div/div[1]/button")  # 关闭取消
    CANCELCLOSEBTN5 = ("xpath", "html/body/div[5]/div/div/div/div/div[1]/button")  # 关闭取消

    # 项目编辑
    EDITNAMETEXT = ("xpath", INFOCOMMONXPATH + "/div[2]/div[1]/div[1]")  # 项目名称字段
    EDITCODETEXT = ("xpath", INFOCOMMONXPATH + "/div[2]/div[2]/div[1]")  # 项目编码字段
    EDITMANAGERTEXT = ("xpath", INFOCOMMONXPATH + "/div[2]/div[2]/div[2]")  # 项目经理字段
    EDITAPPROVALDATETEXT = ("xpath", INFOCOMMONXPATH + "/div[2]/div[3]/div")  # 立项日期字段
    EDITDESCRIPTIONTEXT = ("xpath", INFOCOMMONXPATH + "/div[2]/div[4]/div[1]")  # 项目描述字段

    EDITNAMEINPUTTEXT = ("xpath", INFOCOMMONXPATH + "/div[2]/div[1]/div[2]")  # 项目名称内容
    EDITCODEINPUTTEXT = ("xpath", INFOCOMMONXPATH + "/div[2]/div[2]/div[1]/span")  # 项目编码内容
    EDITMANAGERINPUTTEXT = ("xpath", INFOCOMMONXPATH + "/div[2]/div[2]/div[2]/span")  # 项目经理内容
    EDITAPPROVALDATEINPUTTEXT = ("xpath", INFOCOMMONXPATH + "/div[2]/div[3]/div/span")  # 立项日期内容
    EDITDESCRIPTIONINPUT = ("xpath", INFOCOMMONXPATH + "/div[2]/div[4]/div[2]/textarea")  # 项目描述内容

    # 项目结束
    ENDNAMETEXT = ("xpath", INFOCOMMONXPATH + "/div[2]/div[1]/div[1]")  # 项目名称字段
    ENDCODETEXT = ("xpath", INFOCOMMONXPATH + "/div[2]/div[2]/div[1]")  # 项目编码字段
    ENDMANAGERTEXT = ("xpath", INFOCOMMONXPATH + "/div[2]/div[2]/div[2]")  # 项目经理字段
    ENDAPPROVALDATETEXT = ("xpath", INFOCOMMONXPATH + "/div[2]/div[3]/div")  # 立项日期字段
    ENDENDDATETEXT = ("xpath", INFOCOMMONXPATH + "/div[2]/div[4]/div/span")  # 结束日期字段
    ENDDESCRIPTIONTEXT = ("xpath", INFOCOMMONXPATH + "/div[2]/div[5]/div[1]")  # 项目描述字段

    ENDNAMEINPUTTEXT = ("xpath", INFOCOMMONXPATH + "/div[2]/div[1]/div[2]")  # 项目名称内容
    ENDCODEINPUTTEXT = ("xpath", INFOCOMMONXPATH + "/div[2]/div[2]/div[1]/span")  # 项目编码内容
    ENDMANAGERINPUTTEXT = ("xpath", INFOCOMMONXPATH + "/div[2]/div[2]/div[2]/span")  # 项目经理内容
    ENDAPPROVALDATEINPUTTEXT = ("xpath", INFOCOMMONXPATH + "/div[2]/div[3]/div/span")  # 立项日期内容
    ENDDESCRIPTIONINPUT = ("xpath", INFOCOMMONXPATH + "/div[2]/div[5]/div[2]/textarea")  # 项目描述内容

    # 结束日期控件组
    ENDENDDATEINPUT = ("xpath", INFOCOMMONXPATH + "/div[2]/div[4]/div/div/div/input")  # 日期参照
    ENDTODAYDATE = ("xpath", "html/body/div[4]/div/div/div/div/div[2]/div[3]/span/a")  # 今天

    # 项目删除
    DELETEMSG = ("xpath", "html/body/div[2]/div/div/div/div/div/div[2]")  # 删除提示信息
    DELETECANCELBTN = ("xpath", "html/body/div[2]/div/div/div/div/div/div[3]/button[1]")  # 取消删除
    DELETEOKBTN = ("xpath", "html/body/div[2]/div/div/div/div/div/div[3]/button[2]")  # 确定删除
    DELETECLOSEBTN = ("xpath", "html/body/div[2]/div/div/div/div/div/div[1]/button")  # 关闭删除

    # 项目详情
    INFONAMETEXT = ("xpath", INFOCOMMONXPATH + "")  # 项目名称字段
    INFOCODETEXT = ("xpath", INFOCOMMONXPATH + "")  # 项目编码字段
    INFOMANAGERTEXT = ("xpath", INFOCOMMONXPATH + "")  # 项目经理字段
    INFOAPPROVALDATETEXT = ("xpath", INFOCOMMONXPATH + "")  # 立项日期字段
    INFOENDDATETEXT = ("xpath", INFOCOMMONXPATH + "")  # 结束日期字段
    INFODESCRIPTIONTEXT = ("xpath", INFOCOMMONXPATH + "")  # 项目描述字段

    INFONAMEINPUTTEXT = ("xpath", INFOCOMMONXPATH + "")  # 项目名称内容
    INFOCODEINPUTTEXT = ("xpath", INFOCOMMONXPATH + "")  # 项目编码内容
    INFOMANAGERINPUTTEXT = ("xpath", INFOCOMMONXPATH + "")  # 项目经理内容
    INFOAPPROVALDATEINPUTTEXT = ("xpath", INFOCOMMONXPATH + "")  # 立项日期内容
    INFOENDDATEINPUTTEXT = ("xpath", INFOCOMMONXPATH + "")  # 结束日期内容
    INFODESCRIPTIONINPUTTEXT = ("xpath", INFOCOMMONXPATH + "")  # 项目描述内容

    # 通用保存、取消、关闭
    CANCELBTN = ("xpath", INFOCOMMONXPATH + "/div[3]/button[1]")  # 取消按钮
    SAVEBTN = ("xpath", INFOCOMMONXPATH + "/div[3]/button[2]")  # 保存按钮
    CLOSEBTN = ("xpath", INFOCOMMONXPATH + "/div[1]/button")  # 右上角关闭按钮

    # 项目列表页面下的提示信息
    LISTMSG = ("xpath", "html/body/div[2]/div/span/div/div/div/div/div[2]")  # 列表页面下弹出的提示
    LISTCLOSE = ("xpath", "html/body/div[2]/div/span/div/a/span")  # 关闭提示

    # 项目详情页面下的提示信息
    CARDMSG = ("xpath", "html/body/div[3]/div/span/div/div/div/div/div[2]")  # 项目详情页面下弹出的提示
    CARDCLOSE = ("xpath", "html/body/div[3]/div/span/div/a/span")  # 关闭提示

    # 字段重复校验的提示信息
    REPEATMSG = ("xpath", "html/body/div[4]/div/span/div/div/div/div/div[2]")  # 校验编码重复弹出的提示
    REPEATCLOSE = ("xpath", "html/body/div[4]/div/span/div/a/span")  # 关闭提示
