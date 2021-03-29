import math

from selenium import webdriver
import time
try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id("num1")
    x=x_element.text
    y_element = browser.find_element_by_id("num2")
    y=y_element.text
    s = str(int(x) + int(y))
    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(s) # ищем элемент с текстом "Python"
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector(".btn-default")
    button.click()

finally:
    # успеваем скопировать код за 15 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()