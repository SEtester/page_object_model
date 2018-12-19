#encoding:utf8

from selenium import webdriver
class Driver():

    def driver(self,browser_name='Chrome'):
        if browser_name == 'Chrome':
            dr = webdriver.Chrome()
        elif browser_name == 'Firefox':
            dr = webdriver.Firefox()
        elif browser_name == 'Ie':
            dr = webdriver.Ie()
        elif browser_name == 'Edge':
            dr = webdriver.Edge()
        elif browser_name == 'Safari':
            dr = webdriver.Safari()
        else:
            raise NameError(
                "Not found %s browser,You can enter 'Chrome', 'Firefox', 'Ie', 'Edge', 'Safari' ." % browser_name)
        return dr

