# coding: utf-8
# 导入测试用例执行模块
from libs.testcasesuite import TestCaseSuite
# 导入邮件模块
from libs.sendmail import SendMail

__author__ = "sunxr"
__version__ = "V1.1"

TestCaseSuite().executeTestcases()
SendMail().sendTestReport()
