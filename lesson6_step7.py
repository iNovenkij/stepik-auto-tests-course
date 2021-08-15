from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_xpath_form ")
    elements = browser.find_elements_by_css_selector ('input')
    for element in elements:
        element.send_keys("Мой ответ")
    time.sleep(1)
    button = browser.find_element_by_xpath(r'//button[@type="submit"]')
    print(button)
    button.click()
except Exception:
    print("Произошли технические шоколадки")

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
