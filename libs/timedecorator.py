# coding: utf-8
# 导入时间模块
import time


def timeDecorator(timeout=2):
    """页面等待装饰器"""
    def funcDecorator(func):
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)
            time.sleep(timeout)
        return wrapper
    return funcDecorator
