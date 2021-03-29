import unittest
from selenium import webdriver


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        browser.find_element_by_xpath('//*[@placeholder="Введите имя"]').send_keys("Vladimir")
        browser.find_element_by_xpath('//*[@placeholder="Введите фамилию"]').send_keys("Katin")
        browser.find_element_by_xpath('//*[@placeholder="Введите Email"]').send_keys("sendme@somespam.please")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        browser.implicitly_wait(5)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Поздравляем! Вы успешно зарегистировались!", welcome_text)

    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        browser.find_element_by_xpath('//*[@placeholder="Введите имя"]').send_keys("Vladimir")
        browser.find_element_by_xpath('//*[@placeholder="Введите фамилию"]').send_keys("Katin")
        browser.find_element_by_xpath('//*[@placeholder="Введите Email"]').send_keys("sendme@somespam.please")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        browser.implicitly_wait(5)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Поздравляем! Вы успешно зарегистировались!", welcome_text, msg="ERRRRRROOOOOOORRRRRRRR!!!!!")


if __name__ == "__main__":
    unittest.main()






