import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get("https://magento.softwaretestingboard.com/women/tops-women/tees-women.html")
WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element(
    ('xpath', "//a[text()='Support This Project']"), 'Support This Project'))

girls = browser.find_elements('xpath', "//a[@class='product-item-link']")
first_girl = girls[0]
print(first_girl.id)
print(first_girl.text)
print(first_girl.get_attribute('href'))

sorter = browser.find_element('id', 'sorter')
select = Select(sorter)
select.select_by_value('price')

WebDriverWait(browser, 10).until(EC.staleness_of(first_girl))

girls = browser.find_elements('xpath', "//a[@class='product-item-link']")
first_girl = girls[0]
print(first_girl.text)
print(first_girl.get_attribute('href'))