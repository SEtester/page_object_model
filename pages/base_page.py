# encoding:utf8

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pprint import pprint

class BasePage():

    def __init__(self, driver, path=None):
        # self.url = 'https://github.com'
        self.url = 'https://mail.163.com/'
        self.driver = driver
        self.driver.maximize_window()
        self.load_page(path)
        self.timeout = 15
        self.poll_frequency = 0.2

    def load_page(self, path=None):
        if path != None and isinstance(path, str):
            url = self.url + path
            print(url)
        else:
            url = None
        if url != None:
            self.driver.get(url)

    # def by_css(self, css):
    #     locator = (By.CSS_SELECTOR, css)
    #     self.wait_element_visibility_of_element_located(locator)
    #     return self.driver.find_element(*locator)

    def by_xpath(self, xpath,text=None):
        locator = (By.XPATH, xpath)
        self.wait(locator,text)
        return self.driver.find_element(*locator)

    def wait_element_visibility_of_element_located(self, locator):
        WebDriverWait(self.driver, self.timeout, self.poll_frequency).until(
            EC.visibility_of_element_located(locator))

    def wait_text_to_be_present_in_element(self, locator, text):
        WebDriverWait(self.driver, self.timeout, self.poll_frequency).until(
            EC.text_to_be_present_in_element(locator, text))

    def wait_text_to_be_present_in_element_value(self, locator, text):
        WebDriverWait(self.driver, self.timeout, self.poll_frequency).until(
            EC.text_to_be_present_in_element_value(locator, text))

    def by_css(self,css,text=None):
        locator = (By.CSS_SELECTOR, css)
        self.wait_element_visibility_of_element_located(locator)
        self.wait(locator,text)
        return self.driver.find_element(*locator)

    def wait(self,locator,text=None):
        if text == None:
            self.wait_element_visibility_of_element_located(locator)
        else:
            self.wait_text_to_be_present_in_element(locator,text)

    # def switch_to_frame(self,css=None,xpath=None):
    #     if css != None and xpath == None:
    #         locator = (By.CSS_SELECTOR, css)
    #     elif xpath != None and css == None :
    #         locator = (By.CSS_SELECTOR, xpath)
    #     else:
    #         raise ValueError('参数错误，请传css定位或者xpath,需要指定用什么方式传')
    #     WebDriverWait(self.driver, self.timeout, self.poll_frequency).until(
    #         EC.frame_to_be_available_and_switch_to_it(locator))

    def switch_to_frame(self,choose_iframe=None,css=None,xpath=None):
        if choose_iframe == 'default':
            return self.driver.switch_to.default_content()
        elif choose_iframe == 'parent':
            return self.driver.switch_to.parent_frame()
        elif css != None and xpath == None:
            locator = (By.CSS_SELECTOR, css)
        elif xpath != None and css == None :
            locator = (By.XPATH, xpath)
        else:
            raise ValueError('参数错误，请传css定位或者xpath,需要指定用什么方式传')
        WebDriverWait(self.driver, self.timeout, self.poll_frequency).until(
            EC.frame_to_be_available_and_switch_to_it(locator))


if __name__ == '__main__':
    from selenium import webdriver

    # import logging
    # logging.basicConfig(level=logging.DEBUG)
    dr = webdriver.Chrome()
    b = BasePage(dr, '/')

    # b.switch_to_frame(css='#x-URS-iframe')
    b.switch_to_frame(xpath='//*[@id="x-URS-iframe"]')
    b.by_css('.j-inputtext.dlemail').send_keys('123456')
    # print('测试更改github账号')
