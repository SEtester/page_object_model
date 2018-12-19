# encoding:utf8

from .base_page import BasePage


class LoginPage(BasePage):

    # 用户名输入框定位
    def form_username(self):
        return self.by_css('#username')

    # 密码输入框定位
    def form_password(self):
        return self.by_css('#password_input')

    # 登陆按钮
    def login_button(self):
        return self.by_css('#tcloud_login_button')


class LoginAction(LoginPage):

    def login(self, username, password):
        self.form_username().clear()
        self.form_username().send_keys(username)
        self.form_password().clear()
        self.form_password().send_keys(password)
        self.login_button().click()
