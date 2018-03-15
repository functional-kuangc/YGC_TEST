# coding: utf-8
# 项目编辑框公共部分xpath定位
INFOCOMMONXPATH3 = "html/body/div[3]/div/div/div/div/div"
INFOCOMMONXPATH2 = "html/body/div[2]/div/div/div/div/div"


def getProjectListHeadXpathByIndex(index=2):
    """
    根据项目列表列的索引获取表头字段的xpath
    :param index: 项目列表列的索引
    :return: 表头字段的xpath
    """

    return ".//*[@id='app']/div/div/div/div[2]/div/div/div/span/div/table/thead/tr/th[" + str(index) + "]"


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

    # 项目档案列表字段名称
    PROJECTCODETEXT = ("xpath", getProjectListHeadXpathByIndex(index=2))  # 项目编码字段
    PROJECTNAMETEXT = ("xpath", getProjectListHeadXpathByIndex(index=3))  # 项目名称字段
    PROJECTMANAGERTEXT = ("xpath", getProjectListHeadXpathByIndex(index=4))  # 项目经理字段
    PROJECTAPPROVALDATETEXT = ("xpath", getProjectListHeadXpathByIndex(index=5))  # 立项日期字段
    PROJECTENDDATETEXT = ("xpath", getProjectListHeadXpathByIndex(index=6))  # 结束日期字段
    PROJECTDESCRIPTIONTEXT = ("xpath", getProjectListHeadXpathByIndex(index=7))  # 项目描述字段

    # 第一个项目档案信息
    FIRSTPROJECTRADIOBTN = ("xpath", getProjectXpathByIndex(index=1))  # 单选框
    FIRSTPROJECTCODE = ("xpath", getProjectCodeXpathByIndex(index=1))  # 项目编码
    FIRSTPROJECTNAME = ("xpath", getProjectNameXpathByIndex(index=1))  # 项目名称
    FIRSTPROJECTMANAGER = ("xpath", getProjectManagerXpathByIndex(index=1))  # 项目经理
    FIRSTPROJECTAPPROVALDATE = ("xpath", getProjectApprovalDateXpathByIndex(index=1))  # 立项日期
    FIRSTPROJECTENDDATE = ("xpath", getProjectEndDateXpathByIndex(index=1))  # 结束日期
    FIRSTPROJECTDESCRIPTION = ("xpath", getProjectDescriptionXpathByIndex(index=1))  # 项目描述

    # 标题行
    MODULENAME = ("xpath", ".//*[@id='app']/div/div/div/div[1]/div[1]/h4")  # 模块名称
    SEARCHINPUT = ("xpath", ".//*[@id='app']/div/div/div/div[1]/div[2]/input")  # 搜索框
    SEARCHBTN = ("xpath", ".//*[@id='app']/div/div/div/div[1]/div[2]/button")  # 搜索按钮
    CREATEBTN = ("xpath", getProjectOperationXpathByIndex(index=1))  # 创建按钮
    ENTERPRISEBTN = ("xpath", getProjectOperationXpathByIndex(index=2))  # 项目参与方按钮
    MEMBERBTN = ("xpath", getProjectOperationXpathByIndex(index=3))  # 项目团队按钮
    EDITBTN = ("xpath", getProjectOperationXpathByIndex(index=4))  # 编辑按钮
    ENDBTN = ("xpath", getProjectOperationXpathByIndex(index=5))  # 结束按钮
    DELETEBTN = ("xpath", getProjectOperationXpathByIndex(index=6))  # 删除按钮

    # 项目创建
    NEWCODETEXT2 = ("xpath", INFOCOMMONXPATH2 + "/div[2]/div[1]/div[1]/span")  # 项目编码字段
    NEWNAMETEXT2 = ("xpath", INFOCOMMONXPATH2 + "/div[2]/div[1]/div[2]/span")  # 项目名称字段
    NEWAPPROVALDATETEXT2 = ("xpath", INFOCOMMONXPATH2 + "/div[2]/div[2]/div[1]/span")  # 立项日期字段
    NEWMANAGERTEXT2 = ("xpath", INFOCOMMONXPATH2 + "/div[2]/div[2]/div[2]/span")  # 项目经理字段
    NEWDESCRIPTIONTEXT2 = ("xpath", INFOCOMMONXPATH2 + "/div[2]/div[3]/div[1]")  # 项目描述字段

    NEWCODETEXT3 = ("xpath", INFOCOMMONXPATH3 + "/div[2]/div[1]/div[1]/span")  # 项目编码字段
    NEWNAMETEXT3 = ("xpath", INFOCOMMONXPATH3 + "/div[2]/div[1]/div[2]/span")  # 项目名称字段
    NEWAPPROVALDATETEXT3 = ("xpath", INFOCOMMONXPATH3 + "/div[2]/div[2]/div[1]/span")  # 立项日期字段
    NEWMANAGERTEXT3 = ("xpath", INFOCOMMONXPATH3 + "/div[2]/div[2]/div[2]/span")  # 项目经理字段
    NEWDESCRIPTIONTEXT3 = ("xpath", INFOCOMMONXPATH3 + "/div[2]/div[3]/div[1]")  # 项目描述字段

    NEWCODEINPUT2 = ("xpath", INFOCOMMONXPATH2 + "/div[2]/div[1]/div[1]/input")  # 项目编码输入框
    NEWNAMEINPUT2 = ("xpath", INFOCOMMONXPATH2 + "/div[2]/div[1]/div[2]/input")  # 项目名称输入框
    NEWMANAGERINPUT2 = ("xpath", INFOCOMMONXPATH2 + "/div[2]/div[3]/div[2]/textarea")  # 项目经理输入框
    NEWDESCRIPTIONINPUT2 = ("xpath", INFOCOMMONXPATH2 + "/div[2]/div[3]/div[2]/textarea")  # 项目描述输入框

    NEWCODEINPUT3 = ("xpath", INFOCOMMONXPATH3 + "/div[2]/div[1]/div[1]/input")  # 项目编码输入框
    NEWNAMEINPUT3 = ("xpath", INFOCOMMONXPATH3 + "/div[2]/div[1]/div[2]/input")  # 项目名称输入框
    NEWMANAGERINPUT3 = ("xpath", INFOCOMMONXPATH3 + "/div[2]/div[3]/div[2]/textarea")  # 项目经理输入框
    NEWDESCRIPTIONINPUT3 = ("xpath", INFOCOMMONXPATH3 + "/div[2]/div[3]/div[2]/textarea")  # 项目描述输入框

    # 立项日期控件组
    NEWAPPROVALDATEINPUT2 = ("xpath", INFOCOMMONXPATH2 + "/div[2]/div[2]/div[1]/div/div/input")  # 日期参照
    NEWTODAYDATE3 = ("xpath", "html/body/div[3]/div/div/div/div/div[2]/div[3]/span/a")  # 今天
    NEWAPPROVALDATEINPUT3 = ("xpath", INFOCOMMONXPATH3 + "/div[2]/div[2]/div[1]/div/div/input")  # 日期参照
    NEWTODAYDATE4 = ("xpath", "html/body/div[4]/div/div/div/div/div[2]/div[3]/span/a")  # 今天

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
    EDITNAMETEXT2 = ("xpath", INFOCOMMONXPATH2 + "/div[2]/div[1]/div[1]")  # 项目名称字段
    EDITCODETEXT2 = ("xpath", INFOCOMMONXPATH2 + "/div[2]/div[2]/div[1]")  # 项目编码字段
    EDITMANAGERTEXT2 = ("xpath", INFOCOMMONXPATH2 + "/div[2]/div[2]/div[2]")  # 项目经理字段
    EDITAPPROVALDATETEXT2 = ("xpath", INFOCOMMONXPATH2 + "/div[2]/div[3]/div")  # 立项日期字段
    EDITDESCRIPTIONTEXT2 = ("xpath", INFOCOMMONXPATH2 + "/div[2]/div[4]/div[1]")  # 项目描述字段

    EDITNAMETEXT3 = ("xpath", INFOCOMMONXPATH3 + "/div[2]/div[1]/div[1]")  # 项目名称字段
    EDITCODETEXT3 = ("xpath", INFOCOMMONXPATH3 + "/div[2]/div[2]/div[1]")  # 项目编码字段
    EDITMANAGERTEXT3 = ("xpath", INFOCOMMONXPATH3 + "/div[2]/div[2]/div[2]")  # 项目经理字段
    EDITAPPROVALDATETEXT3 = ("xpath", INFOCOMMONXPATH3 + "/div[2]/div[3]/div")  # 立项日期字段
    EDITDESCRIPTIONTEXT3 = ("xpath", INFOCOMMONXPATH3 + "/div[2]/div[4]/div[1]")  # 项目描述字段

    EDITNAMEINPUTTEXT2 = ("xpath", INFOCOMMONXPATH2 + "/div[2]/div[1]/div[2]")  # 项目名称内容
    EDITCODEINPUTTEXT2 = ("xpath", INFOCOMMONXPATH2 + "/div[2]/div[2]/div[1]/span")  # 项目编码内容
    EDITMANAGERINPUTTEXT2 = ("xpath", INFOCOMMONXPATH2 + "/div[2]/div[2]/div[2]/span")  # 项目经理内容
    EDITAPPROVALDATEINPUTTEXT2 = ("xpath", INFOCOMMONXPATH2 + "/div[2]/div[3]/div/span")  # 立项日期内容
    EDITDESCRIPTIONINPUT2 = ("xpath", INFOCOMMONXPATH2 + "/div[2]/div[4]/div[2]/textarea")  # 项目描述内容

    EDITNAMEINPUTTEXT3 = ("xpath", INFOCOMMONXPATH3 + "/div[2]/div[1]/div[2]")  # 项目名称内容
    EDITCODEINPUTTEXT3 = ("xpath", INFOCOMMONXPATH3 + "/div[2]/div[2]/div[1]/span")  # 项目编码内容
    EDITMANAGERINPUTTEXT3 = ("xpath", INFOCOMMONXPATH3 + "/div[2]/div[2]/div[2]/span")  # 项目经理内容
    EDITAPPROVALDATEINPUTTEXT3 = ("xpath", INFOCOMMONXPATH3 + "/div[2]/div[3]/div/span")  # 立项日期内容
    EDITDESCRIPTIONINPUT3 = ("xpath", INFOCOMMONXPATH3 + "/div[2]/div[4]/div[2]/textarea")  # 项目描述内容

    # 项目结束
    ENDNAMETEXT2 = ("xpath", INFOCOMMONXPATH2 + "/div[2]/div[1]/div[1]")  # 项目名称字段
    ENDCODETEXT2 = ("xpath", INFOCOMMONXPATH2 + "/div[2]/div[2]/div[1]")  # 项目编码字段
    ENDMANAGERTEXT2 = ("xpath", INFOCOMMONXPATH2 + "/div[2]/div[2]/div[2]")  # 项目经理字段
    ENDAPPROVALDATETEXT2 = ("xpath", INFOCOMMONXPATH2 + "/div[2]/div[3]/div")  # 立项日期字段
    ENDENDDATETEXT2 = ("xpath", INFOCOMMONXPATH2 + "/div[2]/div[4]/div/span")  # 结束日期字段
    ENDDESCRIPTIONTEXT2 = ("xpath", INFOCOMMONXPATH2 + "/div[2]/div[5]/div[1]")  # 项目描述字段

    ENDNAMETEXT3 = ("xpath", INFOCOMMONXPATH3 + "/div[2]/div[1]/div[1]")  # 项目名称字段
    ENDCODETEXT3 = ("xpath", INFOCOMMONXPATH3 + "/div[2]/div[2]/div[1]")  # 项目编码字段
    ENDMANAGERTEXT3 = ("xpath", INFOCOMMONXPATH3 + "/div[2]/div[2]/div[2]")  # 项目经理字段
    ENDAPPROVALDATETEXT3 = ("xpath", INFOCOMMONXPATH3 + "/div[2]/div[3]/div")  # 立项日期字段
    ENDENDDATETEXT3 = ("xpath", INFOCOMMONXPATH3 + "/div[2]/div[4]/div/span")  # 结束日期字段
    ENDDESCRIPTIONTEXT3 = ("xpath", INFOCOMMONXPATH3 + "/div[2]/div[5]/div[1]")  # 项目描述字段

    ENDNAMEINPUTTEXT2 = ("xpath", INFOCOMMONXPATH2 + "/div[2]/div[1]/div[2]")  # 项目名称内容
    ENDCODEINPUTTEXT2 = ("xpath", INFOCOMMONXPATH2 + "/div[2]/div[2]/div[1]/span")  # 项目编码内容
    ENDMANAGERINPUTTEXT2 = ("xpath", INFOCOMMONXPATH2 + "/div[2]/div[2]/div[2]/span")  # 项目经理内容
    ENDAPPROVALDATEINPUTTEXT2 = ("xpath", INFOCOMMONXPATH2 + "/div[2]/div[3]/div/span")  # 立项日期内容
    ENDDESCRIPTIONINPUT2 = ("xpath", INFOCOMMONXPATH2 + "/div[2]/div[5]/div[2]/textarea")  # 项目描述内容

    ENDNAMEINPUTTEXT3 = ("xpath", INFOCOMMONXPATH3 + "/div[2]/div[1]/div[2]")  # 项目名称内容
    ENDCODEINPUTTEXT3 = ("xpath", INFOCOMMONXPATH3 + "/div[2]/div[2]/div[1]/span")  # 项目编码内容
    ENDMANAGERINPUTTEXT3 = ("xpath", INFOCOMMONXPATH3 + "/div[2]/div[2]/div[2]/span")  # 项目经理内容
    ENDAPPROVALDATEINPUTTEXT3 = ("xpath", INFOCOMMONXPATH3 + "/div[2]/div[3]/div/span")  # 立项日期内容
    ENDDESCRIPTIONINPUT3 = ("xpath", INFOCOMMONXPATH3 + "/div[2]/div[5]/div[2]/textarea")  # 项目描述内容

    # 结束日期控件组
    ENDENDDATEINPUT2 = ("xpath", INFOCOMMONXPATH2 + "/div[2]/div[4]/div/div/div/input")  # 日期参照
    ENDTODAYDATE3 = ("xpath", "html/body/div[3]/div/div/div/div/div[2]/div[3]/span/a")  # 今天
    ENDENDDATEINPUT3 = ("xpath", INFOCOMMONXPATH3 + "/div[2]/div[4]/div/div/div/input")  # 日期参照
    ENDTODAYDATE4 = ("xpath", "html/body/div[4]/div/div/div/div/div[2]/div[3]/span/a")  # 今天

    # 项目删除
    DELETEMSG2 = ("xpath", INFOCOMMONXPATH2 + "/div[2]")  # 删除提示信息
    DELETEMSG3 = ("xpath", INFOCOMMONXPATH3 + "/div[2]")  # 删除提示信息

    # 项目详情
    INFONAMETEXT2 = ("xpath", INFOCOMMONXPATH2 + "/div[2]/div[1]/div[1]")  # 项目名称字段
    INFOCODETEXT2 = ("xpath", INFOCOMMONXPATH2 + "/div[2]/div[2]/div[1]")  # 项目编码字段
    INFOMANAGERTEXT2 = ("xpath", INFOCOMMONXPATH2 + "/div[2]/div[2]/div[2]")  # 项目经理字段
    INFOAPPROVALDATETEXT2 = ("xpath", INFOCOMMONXPATH2 + "/div[2]/div[3]/div[1]")  # 立项日期字段
    INFOENDDATETEXT2 = ("xpath", INFOCOMMONXPATH2 + "/div[2]/div[3]/div[2]")  # 结束日期字段
    INFODESCRIPTIONTEXT2 = ("xpath", INFOCOMMONXPATH2 + "/div[2]/div[4]/div[1]")  # 项目描述字段

    INFONAMETEXT3 = ("xpath", INFOCOMMONXPATH3 + "/div[2]/div[1]/div[1]")  # 项目名称字段
    INFOCODETEXT3 = ("xpath", INFOCOMMONXPATH3 + "/div[2]/div[2]/div[1]")  # 项目编码字段
    INFOMANAGERTEXT3 = ("xpath", INFOCOMMONXPATH3 + "/div[2]/div[2]/div[2]")  # 项目经理字段
    INFOAPPROVALDATETEXT3 = ("xpath", INFOCOMMONXPATH3 + "/div[2]/div[3]/div[1]")  # 立项日期字段
    INFOENDDATETEXT3 = ("xpath", INFOCOMMONXPATH3 + "/div[2]/div[3]/div[2]")  # 结束日期字段
    INFODESCRIPTIONTEXT3 = ("xpath", INFOCOMMONXPATH3 + "/div[2]/div[4]/div[1]")  # 项目描述字段

    INFONAMEINPUTTEXT2 = ("xpath", INFOCOMMONXPATH2 + "/div[2]/div[1]/div[2]")  # 项目名称内容
    INFOCODEINPUTTEXT2 = ("xpath", INFOCOMMONXPATH2 + "/div[2]/div[2]/div[1]/span")  # 项目编码内容
    INFOMANAGERINPUTTEXT2 = ("xpath", INFOCOMMONXPATH2 + "/div[2]/div[2]/div[2]/span")  # 项目经理内容
    INFOAPPROVALDATEINPUTTEXT2 = ("xpath", INFOCOMMONXPATH2 + "/div[2]/div[3]/div[1]/span")  # 立项日期内容
    INFOENDDATEINPUTTEXT2 = ("xpath", INFOCOMMONXPATH2 + "/div[2]/div[3]/div[2]/span")  # 结束日期内容
    INFODESCRIPTIONINPUTTEXT2 = ("xpath", INFOCOMMONXPATH2 + "/div[2]/div[3]/div[2]/span")  # 项目描述内容

    INFONAMEINPUTTEXT3 = ("xpath", INFOCOMMONXPATH3 + "/div[2]/div[1]/div[2]")  # 项目名称内容
    INFOCODEINPUTTEXT3 = ("xpath", INFOCOMMONXPATH3 + "/div[2]/div[2]/div[1]/span")  # 项目编码内容
    INFOMANAGERINPUTTEXT3 = ("xpath", INFOCOMMONXPATH3 + "/div[2]/div[2]/div[2]/span")  # 项目经理内容
    INFOAPPROVALDATEINPUTTEXT3 = ("xpath", INFOCOMMONXPATH3 + "/div[2]/div[3]/div[1]/span")  # 立项日期内容
    INFOENDDATEINPUTTEXT3 = ("xpath", INFOCOMMONXPATH3 + "/div[2]/div[3]/div[2]/span")  # 结束日期内容
    INFODESCRIPTIONINPUTTEXT3 = ("xpath", INFOCOMMONXPATH3 + "/div[2]/div[3]/div[2]/span")  # 项目描述内容

    # 通用保存、取消、关闭
    CANCELBTN2 = ("xpath", INFOCOMMONXPATH2 + "/div[3]/button[1]")  # 取消按钮
    SAVEBTN2 = ("xpath", INFOCOMMONXPATH2 + "/div[3]/button[2]")  # 保存按钮
    CLOSEBTN2 = ("xpath", INFOCOMMONXPATH2 + "/div[1]/button")  # 右上角关闭按钮

    CANCELBTN3 = ("xpath", INFOCOMMONXPATH3 + "/div[3]/button[1]")  # 取消按钮
    SAVEBTN3 = ("xpath", INFOCOMMONXPATH3 + "/div[3]/button[2]")  # 保存按钮
    CLOSEBTN3 = ("xpath", INFOCOMMONXPATH3 + "/div[1]/button")  # 右上角关闭按钮

    # 项目列表页面下的提示信息
    LISTTOAST = ("xpath", "html/body/div[2]/div/span/div/div/div/div/div[2]")  # 列表页面下弹出的toast提示
    LISTCLOSE = ("xpath", "html/body/div[2]/div/span/div/a/span")  # 关闭提示

    # 项目详情页面下的提示信息
    CARDTOAST = ("xpath", "html/body/div[3]/div/span/div/div/div/div/div[2]")  # 项目详情页面下弹出的toast提示
    CARDCLOSE = ("xpath", "html/body/div[3]/div/span/div/a/span")  # 关闭提示

    # 字段重复校验的提示信息
    REPEATTOAST = ("xpath", "html/body/div[4]/div/span/div/div/div/div/div[2]")  # 校验编码重复弹出的toast提示
    REPEATCLOSE = ("xpath", "html/body/div[4]/div/span/div/a/span")  # 关闭提示
