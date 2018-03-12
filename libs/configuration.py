# coding: utf-8
# 导入libs下的logger日志模块
from libs.logger import Logger
# 导入ConfigParser模块,用于操作配置文件
from configparser import ConfigParser
# 导入os模块，获取文件路径
import os

__author__ = "sunxr"
__version__ = "V1.2"

logger = Logger("Configuration").getLog()

# 获取框架主路径信息
home_path = os.path.dirname(os.path.dirname(__file__))


class Configuration:
    """
    配置文件操作类,用于读取配置文件中的信息.
    """

    def __init__(self):
        """
        初始化一个ConfigParser类,用于配置文件操作.
        """

        self.__config = ConfigParser()

    def __readConfig(self):
        """
        获取配置文件.
        """

        try:
            # 读取配置文件
            config_file_path = home_path + '/config/config.ini'
            self.__config.read(config_file_path)
        except Exception as msg:
            logger.error("获取配置文件异常: %s." % msg)

    def __readConfigOptions(self, section):
        """
        读取配置文件中的某个节点下的所有选项.
        :param section: 节点
        :return: 节点下的所有选项,list列表
        """

        try:
            options = self.__config.options(section=section)
            return options
        except Exception as msg:
            logger.error("读取配置文件选项错误: %s." % msg)

    def __readConfigValue(self, section, option):
        """
        读取配置文件中的具体内容.
        :param section: 节点
        :param option: 选项
        :return: value
        """

        try:
            value = self.__config.get(section=section, option=option)
            return value
        except Exception as msg:
            logger.error("读取配置文件信息错误: %s." % msg)

    def getConfigValue(self, section, option):
        """
        集成读取配置信息中某一节点下的某一选项的具体值的过程.
        :param section: 节点
        :param option: 选项
        :return: 配置文件内容
        """

        self.__readConfig()
        return self.__readConfigValue(section=section, option=option)

    def getConfigOptions(self, section):
        """
        集成读取配置信息中某一节点下的所有选项的过程.
        :param section: 节点
        :return: 节点下的所有选项,list列表
        """

        self.__readConfig()
        return self.__readConfigOptions(section=section)
