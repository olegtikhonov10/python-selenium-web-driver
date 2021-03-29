import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
from selenium import webdriver
import time
try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id("treasure")
    x_element1 = x_element.get_attribute("valuex")
    x = x_element1
    y = calc(x)
    input4 = browser.find_element_by_id("answer")
    input4.send_keys(y)
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
    option2 = browser.find_element_by_id("robotsRule")
    option2.click()
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector(".btn-default")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()