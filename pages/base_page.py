# encoding:utf8
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import sys
import platform

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# SCREENSHOT_PNG_DIR = BASE_DIR + '/screenshot_png'
# PAGES_DIR = BASE_DIR + '/pages'
#
# ALL_DIR = [BASE_DIR, \
#            SCREENSHOT_PNG_DIR, \
#            PAGES_DIR]
# sys.path.extend(ALL_DIR)
# # print(sys.path)
# from pages.driver_obj import Driver

USAGE = '''
USAGE:
python 
python base_page.py https://www.tapd.cn
or
python base_page.py chrome https://www.tapd.cn
'''

# if 'Windows-10' in platform.platform() and len(sys.argv) == 1:
if len(sys.argv) == 1:
    URL = 'https://www.tapd.cn'
    BROWSER_NAME = 'Chrome'
elif len(sys.argv) == 2 and 'http' in sys.argv[-1]:
    URL = sys.argv[-1]
elif len(sys.argv) == 3 and 'http' in sys.argv[-1]:
    BROWSER_NAME, URL = sys.argv[-2], sys.argv[-1]
    print('base_page:',BROWSER_NAME)
else:
    print(USAGE)
    exit()


class BasePage():

    def __init__(self, driver, path=None):
        self.url = URL
        # self.driver = webdriver.Chrome()
        self.driver = driver
        self.driver.maximize_window()
        self.load_page(path)
        self.timeout = 15
        self.poll_frequency = 0.2

    def load_page(self, path=None):
        if path == None:
            self.url = None
        elif isinstance(path, str) and path[0] == '/':
            url = self.url + path
            print(url)
        else:
            raise TypeError('path must be a string ,path must be a uri')
        if path != None:
            self.driver.get(url)

    # def by_css(self, css):
    #     locator = (By.CSS_SELECTOR, css)
    #     self.wait_element_visibility_of_element_located(locator)
    #     return self.driver.find_element(*locator)

    def by_xpath(self, xpath, text=None):
        locator = (By.XPATH, xpath)
        self.wait(locator, text)
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

    def by_css(self, css, text=None):
        locator = (By.CSS_SELECTOR, css)
        # self.wait_element_visibility_of_element_located(locator)
        self.wait(locator, text)
        return self.driver.find_element(*locator)

    def wait(self, locator, text=None):
        if text == None:
            self.wait_element_visibility_of_element_located(locator)
        else:
            self.wait_text_to_be_present_in_element(locator, text)

    def switch_to_frame(self, choose_iframe=None, css=None, xpath=None):
        if choose_iframe == 'default':
            return self.driver.switch_to.default_content()
        elif choose_iframe == 'parent':
            return self.driver.switch_to.parent_frame()
        elif css != None and xpath == None:
            locator = (By.CSS_SELECTOR, css)
        elif xpath != None and css == None:
            locator = (By.XPATH, xpath)
        else:
            raise ValueError('参数错误，请传css定位或者xpath,需要指定用什么方式传')
        WebDriverWait(self.driver, self.timeout, self.poll_frequency).until(
            EC.frame_to_be_available_and_switch_to_it(locator))

    def select_by(self, element, by, value):
        if by == 'index':
            s = Select(element).select_by_index(int(value))
        elif by == 'value':
            s = Select(element).select_by_value(value)
        elif by == 'text':
            s = Select(element).select_by_visible_text(value)
        else:
            raise ValueError("Not found %s , You can enter 'index', 'value', 'text'." % by)
        return s

    def switch_to_alert(self):
        self.alert = WebDriverWait(self.driver, self.timeout, self.poll_frequency).until(EC.alert_is_present())

    def alert_text(self):
        return self.alert.text

    def alert_accept(self):
        return self.alert.accept()

    def alert_dismiss(self):
        return self.alert.dismiss()


if __name__ == '__main__':
    dr = Driver().driver(browser_name=BROWSER_NAME)
    b = BasePage(dr, path='/cloud_logins/login')
