# coding: utf-8
"""
定义全局变量glo_browser_type,用于多线程启动不同浏览器的兼容性测试
"""

__author__ = "sunxr"
__version__ = "V1.1"

GLO_BROWSER_TYPE = "firefox"
GLO_TESTCASES = None


def setBrowserType(browser_type):

    global GLO_BROWSER_TYPE
    GLO_BROWSER_TYPE = browser_type


def setBrowserTypeAndTestcase(browser_type, testcases):

    global GLO_BROWSER_TYPE
    GLO_BROWSER_TYPE = browser_type

    global GLO_TESTCASES
    GLO_TESTCASES = testcases
