# coding: utf-8
# 导入Configuration模块,用于操作配置文件
from libs.configuration import Configuration
# 导入libs下的logger日志模块
from libs.logger import Logger
# 导入selenium中的webdriver
from selenium import webdriver

__author__ = "sunxr"
__version__ = "V1.1"

logger = Logger("Browser").getlog()


def browser(browser_type):
    """
    打开浏览器.
    :param browser_type: 浏览器类型
    :return: driver
    """

    # 创建配置文件实例
    config = Configuration()

    # 读取配置文件中框架主路径信息
    home_path = config.getConfigValue("frameworkPath", "path")

    # 定义浏览器驱动的路径
    chrome_driver_path = home_path + '/tools/chromedriver'
    firefox_driver_path = home_path + '/tools/geckodriver'
    safari_driver_path = home_path + '/tools/safaridriver'

    try:
        if browser_type == "firefox":
            driver = webdriver.Firefox(executable_path=firefox_driver_path)
            logger.info("启动firefox浏览器.")
            return driver
        elif browser_type == "chrome":
            driver = webdriver.Chrome(executable_path=chrome_driver_path)
            logger.info("启动chrome浏览器.")
            return driver
        elif browser_type == "safari":
            driver = webdriver.Safari(executable_path=safari_driver_path)
            logger.info("启动safari浏览器.")
            return driver
        else:
            logger.error("暂不支持当前浏览器: %s,请配置firefox,chrome或safari." % browser_type)
    except Exception as msg:
        logger.error("启动浏览器异常: %s." % msg)
