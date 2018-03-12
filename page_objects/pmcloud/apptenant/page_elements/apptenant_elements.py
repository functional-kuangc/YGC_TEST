# coding: utf-8
class Apptenant:
    """企业帐号选择页元素定位"""

    # 选择框
    SELECTTEXT = ("xpath", ".//*[@id='tenantSelect']/div/div/span")  # 选择框名称
    SELECT = ("xpath", ".//*[@id='combo1']/div/span")  # 下拉框
    APPTENANT = ("xpath", ".//*[@id='combo1']/ul/li[2]/span")  # 下拉框选项：数据中心-回归验证004
    OKBTN = ("id", "submitbtn")  # 确定按钮
