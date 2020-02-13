from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators
from locators import CoursePageLocators
import time

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        #self.browser.maximize_window()
        #self.browser.set_window_size(1920, 1080)
        #size = self.browser.get_window_size()


    def open(self):
        self.browser.get(self.url)
        cookie = self.browser.find_element(*MainPageLocators.COOKIE).click()

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def find_element(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.element_to_be_clickable(locator))


    def is_not_element_present(self, how, what, timeout=10):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=10):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def is_displayed(self, how, what, timeout=10):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def clean_cookie(self):
        self.browser.delete_all_cookies()

    def clear_cache(self, timeout=60):
        get_clear_browsing_button = self.browser.find_element(*MainPageLocators.CLEAR_CACHE)
        self.browser.get("chrome://settings/clearBrowserData")

        # wait for the button to appear
        wait = WebDriverWait(self, timeout)
        wait.until(get_clear_browsing_button)

        # click the button to clear the cache
        get_clear_browsing_button.click()

        # wait for the button to be gone before returning
        wait.until_not(get_clear_browsing_button)