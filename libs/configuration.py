# coding: utf-8
# 导入ConfigParser模块,用于操作配置文件
from configparser import ConfigParser

__author__ = "sunxr"
__version__ = "V1.1"

# 手动设置公共的配置文件路径,为了读取其中框架目录
path_config = ConfigParser()
config_path = '/Users/sunxr/Documents/automation_framework/config/config.ini'
path_config.read(config_path)
home_path = path_config.get("frameworkPath", "path")


class Configuration:
    """
    配置文件操作类,用于读取配置文件中的信息.
    """

    def __init__(self):
        """
        初始化一个ConfigParser类,用于配置文件操作.
        """

        self.__config = ConfigParser()

    def readConfig(self):
        """
        获取配置文件.
        """

        try:
            # 读取配置文件
            config_file_path = home_path + '/config/config.ini'
            self.__config.read(config_file_path)
        except Exception as msg:
            print("获取配置文件异常: %s." % msg)

    def readConfigOptions(self, section):
        """
        读取配置文件中的某个节点下的所有选项.
        :param section: 节点
        :return: 节点下的所有选项,list列表
        """

        try:
            options = self.__config.options(section=section)
            return options
        except Exception as msg:
            print("读取配置文件选项错误: %s." % msg)

    def readConfigValue(self, section, option):
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
            print("读取配置文件信息错误: %s." % msg)

    def getConfigValue(self, section, option):
        """
        集成读取配置信息中某一节点下的某一选项的具体值的过程.
        :param section: 节点
        :param option: 选项
        :return: 配置文件内容
        """

        self.readConfig()
        return self.readConfigValue(section=section, option=option)

    def getConfigOptions(self, section):
        """
        集成读取配置信息中某一节点下的所有选项的过程.
        :param section: 节点
        :return: 节点下的所有选项,list列表
        """

        self.readConfig()
        return self.readConfigOptions(section=section)
