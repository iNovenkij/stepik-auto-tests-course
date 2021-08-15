from selenium import webdriver
from time import sleep
import math


link = "http://suninjuly.github.io/cats.html"


try:
    options = webdriver.ChromeOptions() 
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    browser.get(link)

    button = browser.find_element_by_id("button")
    button.click()



finally:
    # успеваем скопировать код за 30 секунд
    sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()