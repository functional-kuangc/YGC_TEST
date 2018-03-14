# coding: utf-8
# 导入时间模块
import time


def timeDecorator(timeout=2):
    """
    页面等待装饰器.
    :param timeout: 页面等待时间，单位：秒
    :return: 执行操作后页面等待一定时间
    """

    def funcDecorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            time.sleep(timeout)
            return result
        return wrapper
    return funcDecorator
