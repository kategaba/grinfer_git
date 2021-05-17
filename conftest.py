import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import os


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                 help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en",
                 help="Choose language: ru, en, ... (etc.)")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    if browser_name == "chrome":
        options = Options()
        options.add_argument("--incognito")
        options.add_argument("--window-size=1400,1080")
        #options.add_argument("--disable-notifications")
        #options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
        def fin():
            attach = browser.get_screenshot_as_png()
            allure.attach(attach, attachment_type=allure.attachment_type.PNG)
            #logging.info("Closing webdriver instance")
            browser.quit()
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
        raise pytest.UsageError("--language should be existing")
    yield browser
    print("\nquit browser..")
    #browser.quit()
    request.addfinalizer(fin)
