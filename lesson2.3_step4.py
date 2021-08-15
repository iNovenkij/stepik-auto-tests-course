from selenium import webdriver
from time import sleep
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_tag_name('button')
    button.click()
    sleep(1)

    confirm = browser.switch_to.alert
    confirm.accept()

    sleep(1)

    x = int(browser.find_element_by_id('input_value').text)
    result = calc(x)
    answer = browser.find_element_by_id('answer').send_keys(result)

    button = browser.find_element_by_tag_name('button')
    button.click()



finally:
    # успеваем скопировать код за 30 секунд
    sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()