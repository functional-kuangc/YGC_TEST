# coding: utf-8

__author__ = "sunxr"
__version__ = "V1.0"


class Apptenant:
    """企业帐号选择页元素定位"""

    # 选择框
    SELECTTEXT = ("xpath", ".//*[@id='tenantSelect']/div/div/span")  # 选择框名称
    SELECT = ("xpath", ".//*[@id='combo1']/div/span")  # 下拉框
    # APPTENANT = ("xpath", '//*[@id="combo1"]/ul/li[4]')  # 下拉框选择中的名称
    APPTENANT = ("xpath", '//*[@id="combo1"]/ul/li[3]')  # 下拉框选择中的名称
    OKBTN = ("id", "submitbtn")  # 确定按钮
