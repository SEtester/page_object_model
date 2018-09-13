# encoding:utf8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():

    def __init__(self, driver, path=None):
        self.url = 'https://github.com'
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

    def by_css(self, css):
        locator = (By.CSS_SELECTOR, css)
        self.wait_element_visibility(*locator)
        return self.driver.find_element(*locator)

    def by_xpath(self, css):
        locator = (By.CSS_SELECTOR, css)
        return self.driver.find_element(*locator)

    def wait_element_visibility(self, *locator):
        WebDriverWait(self.driver, self.timeout, self.poll_frequency).until(EC.visibility_of_element_located(locator))


if __name__ == '__main__':
    dr = webdriver.Chrome()
    b = BasePage(dr, '/SEtester')
    b.by_css('.repo.js-repo').click()
