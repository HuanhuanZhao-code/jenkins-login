import time

import page
from base.base import Base


class PageLogin(Base):
    # 点击登录链接
    def page_click_login_link(self):
        self.base_click(page.login_link)
        print(page.login_link)

    # 输入用户名
    def page_input_username(self, username):
        self.base_input(page.login_username, username)

    # 输入密码
    def page_input_password(self, password):
        self.base_input(page.login_pwd, password)

    # 输入验证码
    def page_input_verify_code(self, verify_code):
        self.base_input(page.login_verify_code, verify_code)

    # 点击登录按钮
    def page_click_login_button(self):
        self.base_click(page.login_btn)

    # 获取登录成功后昵称
    def page_get_login_success_nickname(self):
        return self.base_get_text(page.login_nickname)

    # 点击安全退出
    def page_click_safe_exit(self):
        self.base_click(page.login_logout)

    # 获取登陆失败后弹窗提示信息
    def page_get_login_fail_info(self):
        self.base_get_text(page.login_error_info)

    # 登录失败后异常提示框点击确定按钮
    def page_click_login_fail_info_button(self):
        self.base_click(page.login_error_btn)

    # 组合业务方法
    def page_login(self, username, password, verify_code):
        self.page_input_username(username)
        print("eeeeeee")
        self.page_input_password(password)
        self.page_input_verify_code(verify_code)
        self.page_click_login_button()

    # # 登录成功给购物车和支付使用
    # def page_login_success(self, username="13800001111", password="123456", verify_code="8888"):
    #     print("tttttttttttttt")
    #     # self.page_click_login_button()
    #     self.page_click_login_link()
    #     time.sleep(3)
    #     print("degndai")
    #     self.page_input_username(username)
    #     print("yognhu")
    #     self.page_input_password(password)
    #     print("mima")
    #     self.page_input_verify_code(verify_code)
    #     print("yanzhegnma")
    #     self.page_click_login_button()
    #     print("anniu")

    # 以下依赖登录成功方法 给：购物车、订单、支付模块使用
    def page_login_success(self, username="13800001111", pwd="123456", code="8888"):
        self.page_click_login_link()
        self.page_input_username(username)
        self.page_input_password(pwd)
        self.page_input_verify_code(code)
        self.page_click_login_button()
