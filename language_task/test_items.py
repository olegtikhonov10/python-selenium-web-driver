import time 
def test_guest_should_see_smth(browser):
    result= False
    try:
        result=browser.find_element_by_css_selector(".btn-add-to-basket")
        result= True
    finally:
        assert result,  "Элемент не найден"
        time.sleep(5)