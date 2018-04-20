# coding: utf-8

__author__ = "sunxr"
__version__ = "V1.0"


class ContactType:
    """联系类型元素定位"""

    # 联系类型新增
    ADDCONTACTTYPEINPUT = ("xpath", ".//*[@id='app']/div/div/div/div[2]/div[2]/div[1]/div/div[1]/input")  # 新增联系类型文本框
    ADDCONTACTTYPEBTN = ("xpath", ".//*[@id='app']/div/div/div/div[2]/div[2]/div")  # 联系类型新增按钮
    ADDCONTACTTYPESAVEBTN = ("xpath", ".//*[@id='app']/div/div/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/button")  # 新增联系类型保存按钮
    ADDCONTACTTYPECANCELBTN = ("xpath", ".//*[@id='app']/div/div/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/button")  # 新增联系类型取消按钮
    ADDCONTACTTYPETEXT = ("xpath", "/html/body/div[1]/div/div/div/div[2]/div[1]/span/div[5]/div/div[1]/input")  # 新增的联系类型

    # 联系类型编辑
    EDITCONTACTTYPEINPUT = ("xpath", ".//*[@id='app']/div/div/div/div[2]/div[1]/span/div[5]/div/div[1]/input")  # 编辑联系类型文本框
    EDITCONTACTTYPEBTN = ("xpath", ".//*[@id='app']/div/div/div/div[2]/div[1]/span/div[5]/div/div[2]/div[1]/button")  # 联系类型编辑按钮
    EDITCONTACTTYPESAVEBTN = ("xpath", ".//*[@id='app']/div/div/div/div[2]/div[1]/span/div[5]/div/div[2]/div[1]/button")  # 编辑联系类型保存按钮
    EDITCONTACTTYPECANCELBTN = ("xpath", ".//*[@id='app']/div/div/div/div[2]/div[1]/span/div[5]/div/div[2]/div[2]/button")  # 编辑联系类型取消按钮
    EDITCONTACTTYPETEXT = ("xpath", "/html/body/div[1]/div/div/div/div[2]/div[1]/span/div[5]/div/div[1]/input")  # 编辑后的联系类型

    # 联系类型删除
    DELETECONTACTTYPENOTUSEDBTN = ("xpath", ".//*[@id='app']/div/div/div/div[2]/div[1]/span/div[5]/div/div[2]/div[2]/button")  # 联系类型未被引用删除按钮
    DELETECONTACTTYPEUSEDBTN = ("xpath", ".//*[@id='app']/div/div/div/div[2]/div[1]/span/div[1]/div/div[2]/div[2]/button")  # 联系类型被引用删除按钮
    DELETECONTACTTYPETEXT = ("xpath", "/html/body/div[1]/div/div/div/div[2]/div[1]/span/div[5]/div/div[1]/input")  # 删除后的联系类型

    DELETECONTACTTYPEMSG3 = ("xpath", "html/body/div[3]/div/div[2]/div/div/div[2]")  # 联系类型删除提示信息
    DELETECONTACTTYPEOKBTN3 = ("xpath", "html/body/div[3]/div/div[2]/div/div/div[3]/div/button[2]")  # 删除确定按钮
    DELETECONTACTTYPECANCELBTN3 = ("xpath", "html/body/div[3]/div/div[2]/div/div/div[3]/div/button[1]")  # 删除取消按钮
    DELETECONTACTTYPECLOSEBTN3 = ("xpath", "html/body/div[3]/div/div[2]/div/div/div[1]/button")  # 删除右上角关闭按钮

    DELETECONTACTTYPEMSG4 = ("xpath", "html/body/div[4]/div/div[2]/div/div/div[2]")  # 联系类型删除提示信息
    DELETECONTACTTYPEOKBTN4 = ("xpath", "html/body/div[4]/div/div[2]/div/div/div[3]/div/button[2]")  # 删除确定按钮
    DELETECONTACTTYPECANCELBTN4 = ("xpath", "html/body/div[4]/div/div[2]/div/div/div[3]/div/button[1]")  # 删除取消按钮
    DELETECONTACTTYPECLOSEBTN4 = ("xpath", "html/body/div[4]/div/div[2]/div/div/div[1]/button")  # 删除右上角关闭按钮

    # 公共定位
    TOAST = ("xpath", "html/body/div[3]/div/span/div/div/div/div/div[2]")  # toast提示
    TOASTCLOSEBTN = ("xpath", "html/body/div[3]/div/span/div/a")  # toast关闭按钮
    CONTACTTYPELISTS = ("xpath", "/html/body/div[1]/div/div/div/div[2]/div[1]/span//input")  # 联系类型列表
