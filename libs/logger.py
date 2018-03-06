# coding: utf-8
# 导入python的日志模块
import logging
# 导入time模块,用于时间戳处理
import time
# 导入Configuration模块,用于操作配置文件
from libs.configuration import Configuration

__author__ = "sunxr"
__version__ = "V1.1"


class Logger:
    """
    公共日志类,创建日志记录器,记录所有信息,生成的日志存储在logs文件中.
    """

    def __init__(self, logger):
        """
        指定保存日志的文件路径,日志级别.
        将日志存入到指定的文件中.
        """

        # logging.getLogger("name")创建要记录的日志级别的记录器
        self.__logger = logging.getLogger(logger)
        # setLevel(level)指定最低的日志级别,低于level的级别将被忽略,debug是最低的内置级别,critical为最高
        self.__logger.setLevel(logging.DEBUG)

        # 定义日志名称中的时间戳
        nowtime = time.strftime("%Y%m%d%H%M%S")

        # 创建配置文件实例
        config = Configuration()

        # 读取配置文件中框架主路径信息
        home_path = config.getConfigValue("frameworkPath", "path")

        # 定义日志存放路径
        log_path = home_path + '/logs/'

        # 定义日志名称
        log_name = log_path + nowtime + '.log'

        # 创建日志处理程序handler
        # FileHandler将日志信息输出到磁盘文件上,用于写入日志文件
        filehandler = logging.FileHandler(log_name)
        # 定义被处理的信息的级别
        filehandler.setLevel(logging.INFO)

        # StreamHandler(),用于输出到控制台
        streamhandler = logging.StreamHandler()
        # 定义被处理的信息的级别
        streamhandler.setLevel(logging.INFO)

        # 定义handler的输出格式
        # %(asctime)s 字符串形式的当前时间,默认格式是 “2003-07-08 16:49:45,896”,逗号后面的是毫秒
        # %(name)s Logger的名字
        # %(levelname)s 文本形式的日志级别
        # %(message)s 用户输出的消息
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        filehandler.setFormatter(formatter)
        streamhandler.setFormatter(formatter)

        # 给logger对象添加Handler
        self.__logger.addHandler(filehandler)
        self.__logger.addHandler(streamhandler)

    def getlog(self):
        return self.__logger
