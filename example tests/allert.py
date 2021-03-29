import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
from selenium import webdriver
import time #импортируем необходимые библиотеки и заранее заводим функцию, которая высчитает значение для проверки
try: 
    link = "http://suninjuly.github.io/alert_accept.html" 
    browser = webdriver.Chrome()
    browser.get(link) #переходим по ссылке на страницу, которую будем тестировать
    button = browser.find_element_by_css_selector(".btn-primary") #находим элемент с помощью css-селектора
    button.click()#кликаем по элементу
    confirm = browser.switch_to.alert #смотрим на всплывающее уведомление
    confirm.accept() #подтверждаем переход
    x_element = browser.find_element_by_id("input_value") #находим элемент x по его ID
    x=x_element.text #переводим переменную в текс
    y = calc(x) #расчитываем проверочное значение с элементом x в качестве аргумента
    button1 = browser.find_element_by_id("answer") #находим форму ответа по ID
    button1.send_keys(y) #вводим вычисленное проверочное значение
    # Отправляем заполненную форму
    button2 = browser.find_element_by_css_selector(".btn-primary")
    button2.click()

finally:
    time.sleep(15)
    browser.quit() #закрываем браузер