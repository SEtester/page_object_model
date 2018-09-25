# encoding:utf8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')

#显示等待
explicit_wait=WebDriverWait(driver=driver,timeout=10,poll_frequency=0.5)
explicit_wait.until(EC.visibility_of_element_located((By.ID,'kw')))

driver.find_element_by_id('kw').send_keys('深圳-逸遥 博客园')

'''
显示等待套路格式： WebDriverWait(driver,timeout，poll_frequency=0.5，ignored_exceptions=None)
'''

'''
1、WebDriverWait这个类是WebDriver提供的一个等待方法，设定一个超时时间（timeout）,每隔一段时间（poll_frequency）,
直到(until)传入的方法 （  EC.visibility_of_element_located((By.ID,'kw'))  ）返回真，才结束等待，如果超过设定的超时时间（timeout）仍然未返回真，
则抛出异常（TimeoutException）



通过查看源码XXX.py 可得知


'''