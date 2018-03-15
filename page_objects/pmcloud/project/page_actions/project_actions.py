# coding: utf-8
# 导入公共函数Selenium封装类
from libs.pagepubselenium import PagePubSelenium
# 导入项目档案元素定位
from page_objects.pmcloud.project.page_elements.project import Project
# 导入页面等待装饰器
from libs.timedecorator import timeDecorator

__author__ = "sunxr"
__version__ = "V1.0"


class ProjectActions(PagePubSelenium):
    """项目档案操作类"""

    # 列表页面相关操作
    @timeDecorator(1)
    def clickProject(self):
        """
        点击项目.
        :return: 项目详情打开
        """

        self.click(locator=Project.FIRSTPROJECTCODE)

    @timeDecorator(1)
    def selectFirstProject(self):
        """
        选中项目列表中第一个项目.
        :return: 第一个项目被选中
        """

        self.click(locator=Project.FIRSTPROJECTRADIOBTN)

    @timeDecorator(1)
    def clickCreateButton(self):
        """
        点击创建按钮.
        :return: 打开创建项目窗体
        """

        self.click(locator=Project.CREATEBTN)

    @timeDecorator(1)
    def clickEnterpriseButton(self):
        """
        点击项目参与方按钮.
        :return: 打开项目参与方窗体
        """

        self.click(locator=Project.ENTERPRISEBTN)

    @timeDecorator(1)
    def clickMemberButton(self):
        """
        点击项目团队按钮.
        :return: 打开项目团队成员窗体
        """

        self.click(locator=Project.MEMBERBTN)

    @timeDecorator(1)
    def clickEditButton(self):
        """
        点击编辑按钮.
        :return: 打开项目信息编辑窗体
        """

        self.click(locator=Project.EDITBTN)

    @timeDecorator(1)
    def clickEndButton(self):
        """
        点击结束按钮.
        :return: 打开项目结束编辑窗体
        """

        self.click(locator=Project.ENDBTN)

    @timeDecorator(1)
    def clickDeleteButton(self):
        """
        点击删除按钮.
        :return: 项目删除提示信息
        """

        self.click(locator=Project.DELETEBTN)

    @timeDecorator(1)
    def clearSearchKeyword(self):
        """
        清空搜索框中关键字.
        """

        self.clear(locator=Project.SEARCHINPUT)

    @timeDecorator(1)
    def typeSearchKeyword(self, keyword=""):
        """
        在搜索框中输入搜索关键字.
        :param keyword: 搜索关键字
        """

        self.sendText(locator=Project.SEARCHINPUT, text=keyword)

    @timeDecorator(1)
    def clickSearchButton(self):
        """
        点击搜索按钮.
        :return: 搜索结果
        """

        self.click(locator=Project.SEARCHBTN)

    # 创建项目相关操作
    @timeDecorator(1)
    def typeProjectCode(self, projcode="auto_test01"):
        """
        填写项目编码.
        :param projcode: 项目编码
        """

        if self.getElementText(locator=Project.NEWCODETEXT2) == "项目编码":
            self.sendText(locator=Project.NEWCODEINPUT2, text=projcode)
        elif self.getElementText(locator=Project.NEWCODETEXT3) == "项目编码":
            self.sendText(locator=Project.NEWCODEINPUT3, text=projcode)

    @timeDecorator(1)
    def typeProjectName(self, projname="自动化项目"):
        """
        填写项目名称.
        :param projname: 项目名称
        """

        if self.getElementText(locator=Project.NEWNAMETEXT2) == "项目名称":
            self.sendText(locator=Project.NEWNAMEINPUT2, text=projname)
        elif self.getElementText(locator=Project.NEWNAMETEXT3) == "项目名称":
            self.sendText(locator=Project.NEWNAMEINPUT3, text=projname)

    @timeDecorator(1)
    def clickApprovalDate(self):
        """
        点击立项日期控件.
        """

        if self.getElementText(locator=Project.NEWAPPROVALDATETEXT2) == "立项日期":
            self.click(locator=Project.NEWAPPROVALDATEINPUT2)
        elif self.getElementText(locator=Project.NEWAPPROVALDATETEXT3) == "立项日期":
            self.click(locator=Project.NEWAPPROVALDATEINPUT3)

    @timeDecorator(1)
    def selectTodayApprovalDate(self):
        """
        选择今天日期.
        """

        if self.getElementText(locator=Project.NEWTODAYDATE3) == "今天":
            self.click(locator=Project.NEWTODAYDATE3)
        elif self.getElementText(locator=Project.NEWTODAYDATE4) == "今天":
            self.click(locator=Project.NEWTODAYDATE4)

    def selectProjectApprovalDate(self):
        """
        选择立项日期全过程.
        """

        self.clickApprovalDate()
        self.selectTodayApprovalDate()

    @timeDecorator(1)
    def typeProjectDescription(self, projdescription="自动化项目描述字段"):
        """
        填写项目描述.
        :param projdescription: 项目描述内容
        """

        if self.getElementText(locator=Project.NEWDESCRIPTIONTEXT2) == "项目描述":
            self.sendText(locator=Project.NEWDESCRIPTIONINPUT2, text=projdescription)
        elif self.getElementText(locator=Project.NEWDESCRIPTIONTEXT3) == "项目描述":
            self.sendText(locator=Project.NEWDESCRIPTIONINPUT3, text=projdescription)

    @timeDecorator(1)
    def clickCancelCancelButton(self):
        """
        在弹出的取消确认框中点击取消.
        """

        if self.getElementText(locator=Project.CANCELMSGDIV3) == "一旦执行，所填信息将会丢失！是否确认？":
            self.click(locator=Project.CANCELCANCELBTN3)
        elif self.getElementText(locator=Project.CANCELMSGDIV4) == "一旦执行，所填信息将会丢失！是否确认？":
            self.click(locator=Project.CANCELCANCELBTN4)
        elif self.getElementText(locator=Project.CANCELMSGDIV5) == "一旦执行，所填信息将会丢失！是否确认？":
            self.click(locator=Project.CANCELCANCELBTN5)

    @timeDecorator(1)
    def clickCancelCloseButton(self):
        """
        在弹出的取消确认框中点击右上角关闭.
        """

        if self.getElementText(locator=Project.CANCELMSGDIV3) == "一旦执行，所填信息将会丢失！是否确认？":
            self.click(locator=Project.CANCELCLOSEBTN3)
        elif self.getElementText(locator=Project.CANCELMSGDIV4) == "一旦执行，所填信息将会丢失！是否确认？":
            self.click(locator=Project.CANCELCLOSEBTN4)
        elif self.getElementText(locator=Project.CANCELMSGDIV5) == "一旦执行，所填信息将会丢失！是否确认？":
            self.click(locator=Project.CANCELCLOSEBTN5)

    @timeDecorator(1)
    def clickCancelOKButton(self):
        """
        在弹出的取消确认框中点击确定取消创建.
        """

        if self.getElementText(locator=Project.CANCELMSGDIV3) == "一旦执行，所填信息将会丢失！是否确认？":
            self.click(locator=Project.CANCELOKBTN3)
        elif self.getElementText(locator=Project.CANCELMSGDIV4) == "一旦执行，所填信息将会丢失！是否确认？":
            self.click(locator=Project.CANCELOKBTN4)
        elif self.getElementText(locator=Project.CANCELMSGDIV5) == "一旦执行，所填信息将会丢失！是否确认？":
            self.click(locator=Project.CANCELOKBTN5)

    def cancelCreateByCancelButton(self):
        """
        通过取消按钮取消创建项目.
        """

        self.clickCancelButton()
        self.clickCancelOKButton()

    def cancelCreateByCloseButton(self):
        """
        通过右上角关闭按钮取消创建项目.
        """

        self.clickCloseButton()
        self.clickCancelOKButton()

    # 编辑项目相关操作
    @timeDecorator(1)
    def clearEditProjectDescription(self):
        """
        编辑功能清空项目描述中的内容.
        """

        if self.getElementText(locator=Project.EDITDESCRIPTIONTEXT3) == "项目描述":
            self.clear(locator=Project.EDITDESCRIPTIONINPUT3)
        elif self.getElementText(locator=Project.EDITDESCRIPTIONTEXT2) == "项目描述":
            self.clear(locator=Project.EDITDESCRIPTIONINPUT2)

    @timeDecorator(1)
    def typeEditProjectDescription(self, projdescription="自动化项目编辑功能编辑项目描述"):
        """
        编辑功能填写项目描述.
        :param projdescription: 编辑后的项目描述内容
        """

        if self.getElementText(locator=Project.EDITDESCRIPTIONTEXT3) == "项目描述":
            self.sendText(locator=Project.EDITDESCRIPTIONINPUT3, text=projdescription)
        elif self.getElementText(locator=Project.EDITDESCRIPTIONTEXT2) == "项目描述":
            self.sendText(locator=Project.EDITDESCRIPTIONINPUT2, text=projdescription)

    def editProjectDescription(self, projdescription="自动化项目编辑功能编辑项目描述"):
        """
        编辑功能编辑项目描述字段.
        :param projdescription: 编辑后的项目描述内容
        """

        self.clearEditProjectDescription()
        self.typeEditProjectDescription(projdescription=projdescription)

    # 结束项目相关操作
    @timeDecorator(1)
    def clickEndDate(self):
        """
        点击结束日期控件.
        """

        if self.getElementText(locator=Project.ENDENDDATETEXT3) == "结束日期":
            self.click(locator=Project.ENDENDDATEINPUT3)
        elif self.getElementText(locator=Project.ENDENDDATETEXT2) == "结束日期":
            self.click(locator=Project.ENDENDDATEINPUT2)

    @timeDecorator(1)
    def selectTodayEndDate(self):
        """
        选择今天结束日期.
        """

        if self.getElementText(locator=Project.ENDTODAYDATE4) == "今天":
            self.click(locator=Project.ENDTODAYDATE4)
        elif self.getElementText(locator=Project.ENDTODAYDATE3) == "今天":
            self.click(locator=Project.ENDTODAYDATE3)

    def selectProjectEndDate(self):
        """
        选择结束日期全过程.
        """

        self.clickEndDate()
        self.selectTodayEndDate()

    @timeDecorator(1)
    def clearEndProjectDescription(self):
        """
        结束功能清空项目描述中的内容.
        """

        if self.getElementText(locator=Project.ENDDESCRIPTIONTEXT3) == "项目描述":
            self.clear(locator=Project.ENDDESCRIPTIONINPUT3)
        elif self.getElementText(locator=Project.ENDDESCRIPTIONTEXT2) == "项目描述":
            self.clear(locator=Project.ENDDESCRIPTIONINPUT2)

    @timeDecorator(1)
    def typeEndProjectDescription(self, projdescription="自动化项目结束功能编辑项目描述"):
        """
        结束功能填写项目描述.
        :param projdescription: 编辑后的项目描述内容
        """

        if self.getElementText(locator=Project.ENDDESCRIPTIONTEXT3) == "项目描述":
            self.sendText(locator=Project.ENDDESCRIPTIONINPUT3, text=projdescription)
        elif self.getElementText(locator=Project.ENDDESCRIPTIONINPUT2) == "项目描述":
            self.sendText(locator=Project.ENDDESCRIPTIONINPUT2, text=projdescription)

    def endProjectDescription(self, projdescription="自动化项目结束功能编辑项目描述"):
        """
        结束功能编辑项目描述字段.
        :param projdescription: 编辑后的项目描述内容
        """

        self.clearEndProjectDescription()
        self.typeEndProjectDescription(projdescription=projdescription)

    # 公共按钮操作
    @timeDecorator(2)
    def clickSaveButton(self):
        """
        点击创建项目编辑窗体的保存按钮.
        """

        if self.getElementText(locator=Project.CANCELBTN2) == "取消":
            self.click(locator=Project.SAVEBTN2)
        elif self.getElementText(locator=Project.CANCELBTN3) == "取消":
            self.click(locator=Project.SAVEBTN3)

    @timeDecorator(1)
    def clickCancelButton(self):
        """
        点击创建项目编辑窗体的取消按钮.
        """

        if self.getElementText(locator=Project.CANCELBTN2) == "取消":
            self.click(locator=Project.CANCELBTN2)
        elif self.getElementText(locator=Project.CANCELBTN3) == "取消":
            self.click(locator=Project.CANCELBTN3)

    @timeDecorator(1)
    def clickCloseButton(self):
        """
        点击创建项目编辑窗体右上角的关闭按钮.
        """

        if self.getElementText(locator=Project.CANCELBTN2) == "取消":
            self.click(locator=Project.CLOSEBTN2)
        elif self.getElementText(locator=Project.CANCELBTN3) == "取消":
            self.click(locator=Project.CLOSEBTN3)

    # 获取提示信息
    def getListToastMsg(self):
        """
        获取列表页面下出现的toast提示信息.
        :return: 提示信息内容
        """

        return self.getElementText(locator=Project.LISTTOAST)

    def getCardToastMsg(self):
        """
        获取项目详情页面下出现的toast提示信息.
        :return: 提示信息内容
        """

        return self.getElementText(locator=Project.CARDTOAST)

    def getRepeatToastMsg(self):
        """
        获取校验重复时出现的toast提示信息.
        :return: 提示信息内容
        """

        return self.getElementText(locator=Project.REPEATTOAST)

    def getCancelMsg(self):
        """
        获取取消操作时弹出的提示信息.
        :return: 提示信息内容
        """

        if self.getElementText(locator=Project.CANCELCANCELBTN3) == "取消":
            return self.getElementText(locator=Project.CANCELMSGDIV3)
        elif self.getElementText(locator=Project.CANCELCANCELBTN4) == "取消":
            return self.getElementText(locator=Project.CANCELMSGDIV4)
        elif self.getElementText(locator=Project.CANCELCANCELBTN5 == "取消"):
            return self.getElementText(locator=Project.CANCELMSGDIV5)

    def getDeleteMsg(self):
        """
        获取删除操作时弹出的提示信息.
        :return: 提示信息内容
        """

        if self.getElementText(locator=Project.CANCELBTN3) == "取消":
            return self.getElementText(locator=Project.DELETEMSG3)
        elif self.getElementText(locator=Project.CANCELBTN2) == "取消":
            return self.getElementText(locator=Project.DELETEMSG2)

    # 关闭提示信息
    def closeListToast(self):
        """
        关闭列表页面下出现的toast提示信息.
        """

        self.click(locator=Project.LISTTOASTCLOSE)

    def closeCardToast(self):
        """
        关闭项目详情页面下出现的toast提示信息.
        """

        self.click(locator=Project.CARDTOASTCLOSE)

    def closeRepeatToast(self):
        """
        关闭校验重复时出现的toast提示信息.
        """

        self.click(locator=Project.REPEATTOASTCLOSE)

    # 流程类操作
    # 搜索
    def searchProject(self, keyword=""):
        """
        搜索项目全流程.
        :param keyword: 搜索关键字
        :return: 搜索结果
        """

        self.clearSearchKeyword()
        self.typeSearchKeyword(keyword=keyword)
        self.clickSearchButton()

    # 创建项目
    def saveCreateProject(self, projcode="auto_test01", projname="自动化项目", projdescription="自动化项目描述字段"):
        """
        创建项目并保存全流程.
        :param projcode: 项目编码
        :param projname: 项目名称
        :param projdescription: 项目描述内容
        """

        self.clickCreateButton()
        self.typeProjectCode(projcode=projcode)
        self.typeProjectName(projname=projname)
        self.selectProjectApprovalDate()
        self.typeProjectDescription(projdescription=projdescription)
        self.clickSaveButton()

    def cancelCreateProjectByCancelButton(self, projcode="auto_test01", projname="自动化项目",
                                          projdescription="自动化项目描述字段"):
        """
        通过取消按钮取消创建项目全流程.
        :param projcode: 项目编码
        :param projname: 项目名称
        :param projdescription: 项目描述内容
        """

        self.clickCreateButton()
        self.typeProjectCode(projcode=projcode)
        self.typeProjectName(projname=projname)
        self.selectProjectApprovalDate()
        self.typeProjectDescription(projdescription=projdescription)
        self.cancelCreateByCancelButton()

    def cancelCreateProjectByCloseButton(self, projcode="auto_test01", projname="自动化项目",
                                         projdescription="自动化项目描述字段"):
        """
        通过右上角关闭按钮取消创建项目全流程.
        :param projcode: 项目编码
        :param projname: 项目名称
        :param projdescription: 项目描述内容
        """

        self.clickCreateButton()
        self.typeProjectCode(projcode=projcode)
        self.typeProjectName(projname=projname)
        self.selectProjectApprovalDate()
        self.typeProjectDescription(projdescription=projdescription)
        self.cancelCreateProjectByCloseButton()

    # 编辑项目
    def saveEditProject(self, projdescription="自动化项目编辑功能编辑项目描述"):
        """
        编辑并保存项目描述全流程.
        :param projdescription: 编辑后的项目描述内容
        """

        self.selectFirstProject()
        self.clickEditButton()
        self.editProjectDescription(projdescription=projdescription)
        self.clickSaveButton()

    def cancelEditProjectByCancelButton(self, projdescription="自动化项目编辑功能编辑项目描述"):
        """
        通过取消按钮取消编辑项目描述全流程.
        :param projdescription: 编辑后的项目描述内容
        """

        self.selectFirstProject()
        self.clickEditButton()
        self.editProjectDescription(projdescription=projdescription)
        self.clickCancelButton()

    def cancelEditProjectByCloseButton(self, projdescription="自动化项目编辑功能编辑项目描述"):
        """
        通过右上角关闭按钮取消编辑项目描述全流程.
        :param projdescription: 编辑后的项目描述内容
        """

        self.selectFirstProject()
        self.clickEditButton()
        self.editProjectDescription(projdescription=projdescription)
        self.clickCloseButton()

    # 结束项目
    def saveEndProject(self, projdescription="自动化项目结束功能编辑项目描述"):
        """
        结束项目全流程.
        """

        self.selectFirstProject()
        self.clickEndButton()
        self.selectProjectEndDate()
        self.endProjectDescription(projdescription=projdescription)
        self.clickSaveButton()

    def cancelEndProjectByCancelButton(self, projdescription="自动化项目结束功能编辑项目描述"):
        """
        通过取消按钮取消结束项目全流程.
        """

        self.selectFirstProject()
        self.clickEndButton()
        self.selectProjectEndDate()
        self.endProjectDescription(projdescription=projdescription)
        self.clickCancelButton()

    def cancelEndProjectByCloseButton(self, projdescription="自动化项目结束功能编辑项目描述"):
        """
        通过右上角关闭按钮取消结束项目全流程.
        """

        self.selectFirstProject()
        self.clickEndButton()
        self.selectProjectEndDate()
        self.endProjectDescription(projdescription=projdescription)
        self.clickCloseButton()

    # 删除项目
    def saveDeleteProject(self):
        """
        删除项目全流程.
        """

        self.selectFirstProject()
        self.clickDeleteButton()
        self.clickSaveButton()

    def cancelDeleteProjectByCancelButton(self):
        """
        通过取消按钮取消删除项目全流程.
        """

        self.selectFirstProject()
        self.clickDeleteButton()
        self.clickCancelButton()

    def cancelDeleteProjectByCloseButton(self):
        """
        通过右上角关闭按钮消删除项目全流程.
        :return:
        """

        self.selectFirstProject()
        self.clickDeleteButton()
        self.clickCloseButton()
