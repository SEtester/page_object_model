# encoding:utf8

from selenium import webdriver


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


if __name__ == '__main__':
    dr = webdriver.Chrome()
    BasePage(dr, '/SEtester')
