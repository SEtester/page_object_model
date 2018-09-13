# encoding:utf8

from selenium import webdriver
from selenium.webdriver.common.by import By


class BasePage():

    def __init__(self, driver, path=None):
        self.url = 'https://github.com'
        self.driver = driver
        self.driver.maximize_window()
        self.load_page(path)

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
        return self.driver.find_element(*locator)

    def by_xpath(self, css):
        locator = (By.CSS_SELECTOR, css)
        return self.driver.find_element(*locator)


if __name__ == '__main__':
    dr = webdriver.Chrome()
    b = BasePage(dr, '/SEtester')
    b.by_css('.repo.js-repo').click()
