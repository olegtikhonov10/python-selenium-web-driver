import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru or en")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.get(f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/")
    yield browser
    print("\nquit browser..")
    browser.quit()
