# coding: utf-8
import unittest
from libs.browser import browser
from libs.logger import Logger
import libs.glo_browsertype as glo
from page_objects import PMCloudIndexActions
from page_objects import PMCloudLoginActions
from page_objects import ApptenantActions

logger = Logger("TestApptenant").getLog()


class TestApptenant(unittest.TestCase):
    """测试友工程的企业帐号"""

    def setUp(self):

        logger.info("测试前准备.")
        self.driver = browser(glo.GLO_BROWSER_TYPE)

        PMCloudIndexActions(self.driver).openPMCloudIndex()
        PMCloudIndexActions(self.driver).clickLoginButton()
        PMCloudLoginActions(self.driver).pmcloudLogin(remember_selected=True)

    def tearDown(self):

        logger.info("测试后退出.")
        self.driver.quit()

    def test_apptenant_login_success(self):
        """企业帐号验证通过"""

        apptenant_page = ApptenantActions(self.driver)

        if apptenant_page.getApptenantTitle() == "企业帐号":

            expected_select_text = "友工程正式环境测试租户001"

            apptenant_page.clickSelect()
            result_select_text = apptenant_page.getSelectApptenantText()
            apptenant_page.clickApptenant()
            apptenant_page.clickOKButton()

            self.assertEqual(expected_select_text, result_select_text,
                             msg="测试不通过, 期望结果为: {expect}, 实际结果为: {result}."
                             .format(expect=expected_select_text, result=result_select_text))

    def test_apptenant_login_error(self):
        """企业帐号验证不通过"""

        apptenant_page = ApptenantActions(self.driver)

        if apptenant_page.getApptenantTitle() == "企业帐号":

            expected_select_text = "友工程正式环境测试租户001error"

            apptenant_page.clickSelect()
            result_select_text = apptenant_page.getSelectApptenantText()
            apptenant_page.clickApptenant()
            apptenant_page.clickOKButton()

            self.assertEqual(expected_select_text, result_select_text,
                             msg="测试不通过, 期望结果为: {expect}, 实际结果为: {result}."
                             .format(expect=expected_select_text, result=result_select_text))


if __name__ == '__main__':
    unittest.main()
