# coding: utf-8
# 导入模拟鼠标事件类
from selenium.webdriver.common.action_chains import ActionChains
# 导入下拉框操作类
from selenium.webdriver.support.select import Select
# 导入所有异常类
from selenium.common.exceptions import *
# 导入元素判断类
from selenium.webdriver.support import expected_conditions as EC
# 导入页面等待类
from selenium.webdriver.support.ui import WebDriverWait
# 导入同目录下的logger日志模块
from libs.logger import Logger
# 导入Configuration模块，用于操作配置文件
from libs.configuration import Configuration
# 导入时间类
import time
# 导入os模块，获取文件路径
import os

__author__ = "sunxr"
__version__ = "V1.2"

logger = Logger("PagePubSelenium").getLog()


class PagePubSelenium:
    """
    将Selenium中的页面公共操作进行封装,所有的页面操作类都要继承此类.
    """

    def __init__(self, browser):
        """
        初始化测试浏览器.
        """

        self.__driver = browser

        # 创建配置文件实例
        self.__config = Configuration()

        # 获取框架主路径信息
        self.__home_path = os.path.dirname(os.path.dirname(__file__))

    def __getScreenShot(self):
        """
        截图操作,将图片保存在screenshots中.
        """

        # 设置截图保存路径
        screenshot_path = self.__home_path + '/screenshots/'
        # 通过时间戳定义图片名称
        nowtime = time.strftime("%Y%m%d%H%M%S")
        screenshot_name = screenshot_path + nowtime + '.png'

        try:
            self.__driver.get_screenshot_as_file(screenshot_name)
            logger.info("截图已保存在screenshots中,名称为: %s." % screenshot_name)
        except Exception as msg:
            logger.error("截图异常: %s." % msg)

    def __catchExceptionAndGetScreenshot(self, msg):
        """
        捕获当前测试异常,并且截图保存在screenshots文件夹中.
        :param msg: 捕获的异常信息
        """

        logger.error(msg)
        self.__getScreenShot()

    def openURL(self):
        """
        打开待测网址.
        """

        # 读取待测网址
        url = self.__config.getConfigValue("testServerURL", "URL")
        self.__driver.implicitly_wait(30)
        logger.info("待测网址为: %s." % url)

        # 打开待测网址
        try:
            self.__driver.get(url)
            logger.info("打开待测网址: %s." % url)
        except Exception as msg:
            self.__catchExceptionAndGetScreenshot("打开待测网址异常: %s." % msg)

    def openExceptedURL(self, expected_title='', timeout=30):
        """
        打开待测网址,并判断打开的网址title是否符合预期.
        :param expected_title: 待测网址期望title
        :param timeout: 查找元素等待时间
        :return: 网址的title是否符合预期，布尔值
        """

        # 读取待测网址
        url = self.__config.getConfigValue("testServerURL", "URL")
        logger.info("待测网址为: %s." % url)

        # 打开待测网址
        try:
            self.__driver.get(url)
            logger.info("打开待测网址: %s." % url)
            # EC.title_is  判断当前页面的title是否完全等于预期字符串,返回布尔值
            return WebDriverWait(self.__driver, timeout, 1).until(EC.title_is(expected_title))
        except Exception as msg:
            self.__catchExceptionAndGetScreenshot("打开待测网址异常: %s." % msg)

    def maximizeWindow(self):
        """
        浏览器窗口最大化.
        """

        try:
            self.__driver.set_window_size("1024", "768")
            self.__driver.maximize_window()
            logger.info("浏览器最大化.")
        except Exception as msg:
            self.__catchExceptionAndGetScreenshot("浏览器最大化异常: %s." % msg)

    def back(self):
        """
        浏览器执行返回操作.
        """

        try:
            self.__driver.back()
            logger.info("浏览器执行返回操作.")
        except Exception as msg:
            self.__catchExceptionAndGetScreenshot("浏览器执行返回操作异常: %s." % msg)

    def forward(self):
        """
        浏览器执行前进操作.
        """

        try:
            self.__driver.forward()
            logger.info("浏览器执行前进操作.")
        except Exception as msg:
            self.__catchExceptionAndGetScreenshot("浏览器执行前进操作异常: %s." % msg)

    def closeCurrentBrowser(self):
        """
        关闭当前浏览器.
        """

        try:
            self.__driver.close()
            logger.info("关闭当前浏览器.")
        except Exception as msg:
            self.__catchExceptionAndGetScreenshot("关闭当前浏览器异常: %s." % msg)

    def quitAllBrowsers(self):
        """
        退出驱动并关闭所有关联的窗口.
        """

        try:
            self.__driver.quit()
            logger.info("关闭所有浏览器进程.")
        except Exception as msg:
            self.__catchExceptionAndGetScreenshot("关闭所有浏览器进程异常: %s." % msg)

    @staticmethod
    def pageSleep(timeout=5):
        """
        页面等待,单位:秒.
        :param timeout: seconds
        """

        time.sleep(timeout)
        logger.info("页面等待: %s秒." % timeout)

    def findElement(self, locator, timeout=3):
        """
        定位单个元素方法封装.
        locator支持: "id", "xpath", "link text", "partial link text", "name", "tag name", "class name", "css selector".
        :param locator: ("id", "xxx")
        :param timeout: 查找元素等待时间
        :return: 定位到的元素element
        """

        try:
            # EC.presence_of_element_located  判断某个元素是否被加到了DOM树里,并不代表该元素一定可见
            element = WebDriverWait(self.__driver, timeout, 1).until(EC.presence_of_element_located(locator))
            logger.info("定位到指定元素: {key} => {value}.".format(key=locator[0], value=locator[1]))
            return element
        except TimeoutException:
            self.__catchExceptionAndGetScreenshot("没有找到指定元素: {key} => {value}."
                                                  .format(key=locator[0], value=locator[1]))
        except Exception as msg:
            self.__catchExceptionAndGetScreenshot("定位元素其他异常: %s." % msg)

    def findElements(self, locator, timeout=3):
        """
        定位一组元素方法封装.
        locator支持: "id", "xpath", "link text", "partial link text", "name", "tag name", "class name", "css selector".
        :param locator: ("id", "xxx")
        :param timeout: 查找元素等待时间
        :return: 定位到的一组元素elements
        """

        try:
            # EC.presence_of_all_elements_located  判断是否至少有1个元素存在于DOM树
            elements = WebDriverWait(self.__driver, timeout, 1).until(EC.presence_of_all_elements_located(locator))
            # elements = self.__driver.find_elements(locator)
            logger.info("定位到指定元素: {key} => {value}.".format(key=locator[0], value=locator[1]))
            return elements
        except TimeoutException:
            self.__catchExceptionAndGetScreenshot("没有找到指定元素: {key} => {value}."
                                                  .format(key=locator[0], value=locator[1]))
        except Exception as msg:
            self.__catchExceptionAndGetScreenshot("定位元素其他异常: %s." % msg)

    def click(self, locator, timeout=3):
        """
        鼠标左键点击元素.
        locator支持: "id", "xpath", "link text", "partial link text", "name", "tag name", "class name", "css selector".
        :param locator: ("id", "xxx")
        :param timeout: 查找元素等待时间
        """

        try:
            element = self.findElement(locator=locator, timeout=timeout)
            element.click()
            logger.info("鼠标左键点击指定元素: {key} => {value}.".format(key=locator[0], value=locator[1]))
        except Exception as msg:
            self.__catchExceptionAndGetScreenshot("鼠标左键点击指定元素异常: %s." % msg)

    def moveMouseToElement(self, locator, timeout=3):
        """
        鼠标悬停在指定元素上.
        locator支持: "id", "xpath", "link text", "partial link text", "name", "tag name", "class name", "css selector".
        :param locator: ("id", "xxx")
        :param timeout: 查找元素等待时间
        """

        try:
            mouse = self.findElement(locator=locator, timeout=timeout)
            ActionChains(self.__driver).move_to_element(mouse).perform()
            logger.info("鼠标悬停在指定元素上: {key} => {value}.".format(key=locator[0], value=locator[1]))
        except Exception as msg:
            self.__catchExceptionAndGetScreenshot("鼠标悬停在指定元素上异常: %s." % msg)

    def clear(self, locator, timeout=3):
        """
        清空文本框内容.
        locator支持: "id", "xpath", "link text", "partial link text", "name", "tag name", "class name", "css selector".
        :param locator: ("id", "xxx")
        :param timeout: 查找元素等待时间
        """

        try:
            element = self.findElement(locator=locator, timeout=timeout)
            element.clear()
            logger.info("清空指定文本框元素中内容,元素为: {key} => {value}.".format(key=locator[0], value=locator[1]))
        except Exception as msg:
            self.__catchExceptionAndGetScreenshot("清空指定文本框元素中内容异常: %s." % msg)

    def sendText(self, locator, text, timeout=3):
        """
        发送文本到指定文本框.
        locator支持: "id", "xpath", "link text", "partial link text", "name", "tag name", "class name", "css selector".
        :param locator: ("id", "xxx")
        :param timeout: 查找元素等待时间
        :param text: 输入的内容
        """

        try:
            self.clear(locator=locator, timeout=timeout)
            element = self.findElement(locator=locator, timeout=timeout)
            element.send_keys(text)
            logger.info("在指定文本框元素中输入文本,元素为: {key} => {value}.".format(key=locator[0], value=locator[1]))
        except Exception as msg:
            self.__catchExceptionAndGetScreenshot("在指定文本框中输入文本异常: %s." % msg)

    def selectByIndex(self, locator, index, timeout=3):
        """
        根据索引选择下拉框中内容.
        locator支持: "id", "xpath", "link text", "partial link text", "name", "tag name", "class name", "css selector".
        :param locator: ("id", "xxx")
        :param index: 下拉框索引
        :param timeout: 查找元素等待时间
        """

        try:
            select = self.findElement(locator=locator, timeout=timeout)
            Select(select).select_by_index(index=index)
            logger.info("根据索引选择下拉框中指定内容,指定索引为: %s." % str(index))
        except Exception as msg:
            self.__catchExceptionAndGetScreenshot("根据索引选择下拉框中指定内容异常: %s." % msg)

    def selectByValue(self, locator, value, timeout=3):
        """
        根据元素value值选择下拉框中内容.
        locator支持: "id", "xpath", "link text", "partial link text", "name", "tag name", "class name", "css selector".
        :param locator: ("id", "xxx")
        :param value: 下拉框索引
        :param timeout: 查找元素等待时间
        """

        try:
            select = self.findElement(locator=locator, timeout=timeout)
            Select(select).select_by_value(value=value)
            logger.info("根据元素value值选择下拉框中指定内容,指定value值为: %s." % value)
        except Exception as msg:
            self.__catchExceptionAndGetScreenshot("根据元素value值选择下拉框中指定内容异常: %s." % msg)

    def selectByText(self, locator, text, timeout=3):
        """
        根据下拉选项内容选择下拉框中内容.
        locator支持: "id", "xpath", "link text", "partial link text", "name", "tag name", "class name", "css selector".
        :param locator: ("id", "xxx")
        :param text: 下拉选项内容
        :param timeout: 查找元素等待时间
        """

        try:
            select = self.findElement(locator=locator, timeout=timeout)
            Select(select).select_by_visible_text(text=text)
            logger.info("根据下拉选项内容选择下拉框中指定内容,指定内容为: %s." % text)
        except Exception as msg:
            self.__catchExceptionAndGetScreenshot("根据下拉选项内容选择下拉框中指定内容异常: %s." % msg)

    def getTitle(self):
        """
        获取网页标题.
        :return: 网页标题
        """

        logger.info("获取当前网页标题: %s." % self.__driver.title)
        return self.__driver.title

    def getElementText(self, locator, timeout=3):
        """
        获取元素文本.
        locator支持: "id", "xpath", "link text", "partial link text", "name", "tag name", "class name", "css selector".
        :param locator: ("id", "xxx")
        :param timeout: 查找元素等待时间
        :return: 元素文本
        """

        try:
            element = self.findElement(locator=locator, timeout=timeout)
            element_text = element.text
            logger.info("获取到的元素文本为: %s." % element_text)
            return element_text
        except Exception as msg:
            self.__catchExceptionAndGetScreenshot("获取元素文本异常: %s." % msg)

    def getElementAttribute(self, locator, name, timeout=3):
        """
        获取元素指定属性的值.
        locator支持: "id", "xpath", "link text", "partial link text", "name", "tag name", "class name", "css selector".
        :param locator: ("id", "xxx")
        :param name: 属性名称
        :param timeout: 查找元素等待时间
        :return: 属性值
        """

        try:
            element = self.findElement(locator=locator, timeout=timeout)
            value = element.get_attribute(name)
            logger.info("获取到的元素属性值为: {name} => {value}.".format(name=name, value=value))
            return value
        except Exception as msg:
            self.__catchExceptionAndGetScreenshot("获取元素属性值异常: %s." % msg)

    def switchToFrame(self, locator, timeout=3):
        """
        切换网页内嵌iframe框架.
        locator支持: "id", "xpath", "link text", "partial link text", "name", "tag name", "class name", "css selector".
        :param locator: ("id", "xxx")
        :param timeout: 查找元素等待时间
        """

        try:
            iframe = self.findElement(locator=locator, timeout=timeout)
            self.__driver.switch_to.frame(iframe)
            logger.info("切换到指定的iframe: %s." % iframe)
        except Exception as msg:
            self.__catchExceptionAndGetScreenshot("切换到指定的iframe异常: %s." % msg)

    def switchToDefaultContent(self):
        """
        释放iframe重新回到主页面上.
        """

        self.__driver.switch_to.default_content()
        logger.info("释放iframe重新回到主页面上.")

    def getCurrentWindowHandle(self):
        """
        获取当前窗口的句柄.
        :return: 当前窗口的句柄
        """

        logger.info("获取当前窗口的句柄,句柄值为: %s." % str(self.__driver.current_window_handle))
        return self.__driver.current_window_handle

    def getAllWindowHandles(self):
        """
        获取所有窗口的句柄.
        :return: 所有窗口的句柄,list
        """
        logger.info("获取所有窗口的句柄.")
        return self.__driver.window_handles

    def switchToWindow(self, handle_value):
        """
        切换到指定窗口.
        :param handle_value: 指定窗口的句柄
        """

        try:
            self.__driver.switch_to.window(handle_value)
            logger.info("切换到指定窗口,窗口句柄为: %s." % str(handle_value))
        except Exception as msg:
            logger.error("切换到指定窗口异常: %s." % msg)

    def switchToAlert(self):
        """
        切换到弹出窗体.
        :return: 弹窗alert
        """

        try:
            alert = self.__driver.switch_to.alert
            if alert.text:
                logger.info("切换到弹窗.")
                return alert
            else:
                self.__catchExceptionAndGetScreenshot("没有发现弹窗.")
        except NoAlertPresentException:
            self.__catchExceptionAndGetScreenshot("没有发现弹窗.")

    def getAlertText(self):
        """
        获取弹窗中的文本信息.
        :return: 文本信息
        """

        alert = self.switchToAlert()
        logger.info("获取弹窗中的文本信息,内容为: %s." % alert.text)
        return alert.text

    def alertAccept(self):
        """
        点击弹窗中的确认.
        """

        alert = self.switchToAlert()
        alert.accept()
        logger.info("点击弹窗中的确认按钮.")

    def alertCancel(self):
        """
        取消弹窗.
        """

        alert = self.switchToAlert()
        alert.dismiss()
        logger.info("取消弹窗.")

    def alertSendkeys(self, text):
        """
        弹窗的文本框中输入信息.
        :param text: 需要输入的信息
        """

        try:
            alert = self.switchToAlert()
            alert.send_keys(text)
            logger.info("在弹窗的文本框中输入信息.")
        except Exception as msg:
            self.__catchExceptionAndGetScreenshot("在弹窗的文本框中输入信息异常: %s." % msg)

    def isTitle(self, expected_title, timeout=3):
        """
        验证网页title是否跟期望完全一样.
        :param expected_title: 期望title值
        :param timeout: 查找元素等待时间
        :return: 是否一样,布尔值
        """

        try:
            # EC.title_is  判断当前页面的title是否完全等于预期字符串,返回布尔值
            result = WebDriverWait(self.__driver, timeout, 1).until(EC.title_is(expected_title))
            logger.info("验证title是否为: %s." % expected_title)
            return result
        except Exception as msg:
            self.__catchExceptionAndGetScreenshot("验证title异常: %s." % msg)

    def isTitleContains(self, expected_title, timeout=3):
        """
        验证网页title是否包含期望值.
        :param expected_title: 期望包含title值
        :param timeout: 查找元素等待时间
        :return: 是否包含,布尔值
        """

        try:
            # EC.title_contains  判断当前页面的title是否包含预期字符串,返回布尔值
            result = WebDriverWait(self.__driver, timeout, 1).until(EC.title_contains(expected_title))
            logger.info("验证title是否包含: %s." % expected_title)
            return result
        except Exception as msg:
            self.__catchExceptionAndGetScreenshot("验证title异常: %s." % msg)

    def isElementSelected(self, locator, timeout=3):
        """
        验证元素是否被选中.
        locator支持: "id", "xpath", "link text", "partial link text", "name", "tag name", "class name", "css selector".
        :param locator: ("id", "xxx")
        :param timeout: 查找元素等待时间
        :return: 是否选中，布尔值
        """

        try:
            expected_element = self.findElement(locator=locator, timeout=timeout)
            result = expected_element.is_selected()
            logger.info("验证元素是否被选中: {key} => {value}.".format(key=locator[0], value=locator[1]))
            return result
        except Exception as msg:
            self.__catchExceptionAndGetScreenshot("验证元素是否被选中异常: %s." % msg)
