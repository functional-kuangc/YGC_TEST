# coding: utf-8
# 导入Configuration模块,用于操作配置文件
from libs.configuration import Configuration
# 导入smtplib模块,用于连接邮件服务器
import smtplib
# 导入MIMEText模块,用于发送邮件
from email.mime.text import MIMEText
# 导入MIMEMultipart模块,用于发送带有附件的邮件
from email.mime.multipart import MIMEMultipart
# 导入os.path,用于路径操作
import os.path
# 导入同目录下的logger日志模块
from libs.logger import Logger
# 导入time模块,用于时间戳定义
import time

__author__ = "sunxr"
__version__ = "V1.1"

logger = Logger(logger="SendMail").getlog()


class SendMail:
    """
    自动发送邮件类,测试结束后,将测试报告发送到配置文件中指定的邮箱.
    """

    def __init__(self):
        """
        初始化发送邮件配置,从配置文件中,获取发邮件的基本信息:发件服务器,端口,账号,密码,收件人.
        """

        # 创建配置文件实例
        config = Configuration()

        # 读取配置文件中框架主路径信息
        self.__home_path = config.getConfigValue("frameworkPath", "path")

        # 读取发件服务器,端口,账号,密码,收件人
        self.__smtpserver = config.getConfigValue("sendMailInfo", "smtp_server")
        self.__port = config.getConfigValue("sendMailInfo", "port")
        self.__sender = config.getConfigValue("sendMailInfo", "sender")
        self.__psw = config.getConfigValue("sendMailInfo", "password")
        self.__receivers = config.getConfigValue("sendMailInfo", "receivers").split(";")  # 得到收件人列表

    def getReportFile(self):
        """
        获取最新的测试报告,作为发送邮件的内容以及附件.
        :return: report_file
        """

        try:
            # listdir 返回指定的文件夹包含的文件或文件夹的名字的列表
            report_path = self.__home_path + '/test_reports'
            lists = os.listdir(report_path)
            # getmtime 输出最近的修改时间
            # sort按key的关键字进行升序排序，lambda的入参fn为lists列表的元素，获取文件的最后修改时间，
            # 所以最终以文件时间从小到大排序
            lists.sort(key=lambda fn: os.path.getmtime(os.path.join(report_path, fn)))
            # 找到最新生成的报告文件
            report_file = os.path.join(report_path, lists[-1])
            logger.info("最新测试生成的报告: %s." % lists[-1])
            return report_file
        except Exception as msg:
            logger.error("获取最新测试报告异常: %s." % msg)

    def editMail(self):
        """
        读取最新的测试报告,并且编辑到邮件中,返回需要发送的邮件.
        :return: mail
        """

        # 读取测试报告内容
        report_file = self.getReportFile()
        with open(report_file, "rb") as report:
           test_report_file = report.read()

        # 邮件内容
        mail = MIMEMultipart()
        mail_body = MIMEText(test_report_file, _subtype='html', _charset='utf-8')
        mail["Subject"] = "自动化测试报告"
        mail["from"] = self.__sender
        mail["to"] = ";".join(self.__receivers)
        mail["data"] = time.strftime('%a, %d %b %Y %H_%M_%S %Z')
        mail.attach(mail_body)

        # 添加附件
        try:
            mail_attachment = MIMEText(open(report_file, "rb").read(), "base64", "utf-8")
            mail_attachment["Content-Type"] = "application/octet-stream"
            mail_attachment["Content-Disposition"] = 'attachment; filename="report.html"'
            mail.attach(mail_attachment)
            logger.info("添加附件: %s." % report_file)
            logger.info("测试报告邮件编辑完成,准备发送.")
            return mail
        except Exception as msg:
            logger.error("添加附件异常: %s." % msg)

    def sendTestReport(self):
        """
        将测试报告邮件发送给配置文件中的指定收件人.
        """

        # 获取邮件内容
        global smtp
        mail_file = self.editMail()

        # 登录邮箱并发送邮件
        try:
            if "@qq.com" in self.__sender:
                # 连接邮箱服务器
                smtp = smtplib.SMTP_SSL(host=self.__smtpserver, port=self.__port)
                # 登录邮箱
                smtp.login(user=self.__sender, password=self.__psw)
                logger.info("登录QQ邮箱发送测试报告: %s." % self.__sender)
            elif "@163.com" in self.__sender:
                # 连接邮箱
                smtp = smtplib.SMTP()
                smtp.connect(host=self.__smtpserver, port=self.__port)
                # 登录邮箱
                smtp.login(user=self.__sender, password=self.__psw)
                logger.info("登录163邮箱发送测试报告: %s." % self.__sender)
            elif "@yonyou.com" in self.__sender:
                # 连接邮箱
                smtp = smtplib.SMTP()
                smtp.connect(host=self.__smtpserver, port=self.__port)
                # 登录邮箱
                smtp.login(user=self.__sender, password=self.__psw)
                logger.info("登录yonyou邮箱发送测试报告: %s." % self.__sender)
            else:
                logger.error("暂不支持当前邮箱: %s,请配置QQ邮箱,yonyou邮箱或163邮箱." % self.__sender)
            # 发送邮件
            smtp.sendmail(from_addr=self.__sender, to_addrs=self.__receivers, msg=mail_file.as_string())
            logger.info("开始发送邮件到: %s." % ";".join(self.__receivers))
            # 关闭邮件
            smtp.quit()
            logger.info("邮件成功发送到: %s." % ";".join(self.__receivers))
        except Exception as msg:
            logger.error("邮件发送异常: %s." % msg)
