# coding: utf-8
class PMCloudLogin:
    """友工程登录页元素定位"""

    # 登录框
    USERNAME = ("id", "username")  # 用户名
    PASSWORD = ("id", "password")  # 密码
    REMEMBER = ("xpath", ".//*[@id='fm1']/section[7]/label[1]")  # 记住密码
    LOGINBTN = ("id", "submit_btn_login")  # 登录按钮

    # 账号
    USER = "zxcyui9637410@126.com"
    PSW = "123qwe!@#"
