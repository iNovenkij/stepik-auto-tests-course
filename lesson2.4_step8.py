from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    options = webdriver.ChromeOptions() 
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(3)
    browser.get(link)

    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    browser.find_element_by_id('book').click()

    x = int(browser.find_element_by_id('input_value').text)
    result = calc(x)
    answer = browser.find_element_by_id('answer').send_keys(result)

    button = browser.find_element_by_id('solve')
    print(button.get_attribute("blabla"))
    button.click()

    

finally:
    # успеваем скопировать код за 30 секунд
    sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()