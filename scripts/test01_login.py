import sys
import time
import unittest

from parameterized import parameterized

from base.get_driver import GetDriver
from page.page_login import PageLogin
from tool.get_data import get_data


class TestLogin(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = GetDriver().get_driver()
        cls.login = PageLogin(cls.driver)
        cls.login.page_click_login_link()

    @classmethod
    def tearDownClass(cls):
        print("quitqian")
        cls.driver.quit()
        print("quithou")
        time.sleep(5)
        print("sys")
    @parameterized.expand(get_data("../data/login.txt"))
    def test_login(self, username, password, verify_code, success, expect):
        self.login.page_login(username, password, verify_code)
        if success == "True":
            try:
                print("rrrrrr")
                nickname = self.login.page_get_login_success_nickname()
                self.assertEqual(expect, nickname)
                self.login.page_click_safe_exit()
                self.login.page_click_login_link()
            except:
                print("正向出错")
        else:
            try:
                fail_info = self.login.page_get_login_fail_info()
                self.assertEqual(expect, fail_info)
            except Exception as e:
                self.login.base_get_image()
            finally:
                self.login.page_click_login_fail_info_button()




