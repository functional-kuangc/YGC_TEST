# coding: utf-8
# 导入同目录下的logger日志模块
from libs.logger import Logger
# 导入Configuration模块,用于操作配置文件
from libs.configuration import Configuration
# 导入MySQL操作pymysql模块
import pymysql

__author__ = "sunxr"
__version__ = "V1.1"

logger = Logger("MySQLOperation").getlog()


class MySQLOperation:
    """
    将pymysql中的部分方法进行封装,处理对MySQL数据库的简单操作.
    """

    def __init__(self):

        # 创建配置文件实例
        self.__config = Configuration()

        # 从配置文件获取数据库相关信息
        self.__host = self.__config.getConfigValue("mysqlInfo", "host")
        self.__user = self.__config.getConfigValue("mysqlInfo", "user")
        self.__password = self.__config.getConfigValue("mysqlInfo", "password")
        self.__database = self.__config.getConfigValue("mysqlInfo", "database")

        # 连接数据库,获取操作游标
        self.__db = self.dbConnect()
        self.__cursor = self.__db.cursor()

    def dbConnect(self):
        """
        连接MySQL数据库.
        """

        try:
            logger.info("开始连接MySQL数据库: {host}:{database}.".format(host=self.__host, database=self.__database))
            db = pymysql.connect(self.__host, self.__user, self.__password, self.__database)
            logger.info("MySQL数据库连接成功: {host}:{database}.".format(host=self.__host, database=self.__database))
            return db
        except Exception as msg:
            logger.error("连接MySQL数据库发生异常: %s." % msg)

    def dbClose(self):
        """
        关闭MySQL数据库连接.
        """

        try:
            self.__db.close()
            logger.info("关闭数据库连接.")
        except Exception as msg:
            logger.error("关闭数据库连接发生异常: %s." % msg)

    def sqlExecute(self, sql):
        """
        执行sql语句公共方法.
        :param sql: 需要处理的sql语句
        """

        try:
            self.__cursor.execute(sql)
            self.__db.commit()
            logger.info("执行SQL语句成功: %s." % sql)
        except Exception as msg:
            logger.error("执行SQL语句异常: %s." % msg)
            self.__db.rollback()

    def sqlCreate(self, sql):
        """
        处理sql创建语句.
        :param sql: 需要处理的sql创建语句
        """
        self.sqlExecute(sql)

    def sqlSelect(self, sql):
        """
        处理sql查询语句.
        :param sql: 需要处理的sql查询语句
        """

        self.sqlExecute(sql)

    def sqlInsert(self, sql):
        """
        处理sql插入语句.
        :param sql: 需要处理的sql插入语句
        """

        self.sqlExecute(sql)

    def sqlUpdate(self, sql):
        """
        处理sql修改语句.
        :param sql: 需要处理的sql修改语句
        """

        self.sqlExecute(sql)

    def sqlDelete(self, sql):
        """
        处理sql删除语句.
        :param sql: 需要处理的sql删除语句
        """

        self.sqlExecute(sql)

    def sqlFetchOne(self, sql):
        """
        处理sql查询结果,获取下一个查询结果.
        :param sql: 需要处理的sql查询语句
        :return: 下一个查询结果
        """

        try:
            self.sqlSelect(sql)
            if self.__cursor.fetchone():
                logger.info("获取到查询结果.")
                return self.__cursor.fetchone()
            else:
                logger.info("没有查询到结果.")
        except Exception as msg:
            logger.error("获取查询结果出现异常: %s." % msg)

    def sqlFetchAll(self, sql):
        """
        处理sql查询结果,获取全部的查询结果.
        :param sql: 需要处理的sql查询语句
        :return: 全部的查询结果
        """

        try:
            self.sqlSelect(sql)
            if self.__cursor.fetchall():
                logger.info("获取到查询结果.")
                return self.__cursor.fetchall()
            else:
                logger.info("没有查询到结果.")
        except Exception as msg:
            logger.error("获取查询结果出现异常: %s." % msg)
