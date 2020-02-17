from selenium.webdriver.common.by import By
from locators import MainPageLocators
from locators import CoursePageLocators
from .base_page import BasePage
import time
import os
import faker
from selenium.webdriver.common.keys import Keys
import random
from selenium.webdriver.support.ui import Select


class MainPage(BasePage):
    #def __init__(self, *args, **kwargs):
        #super(MainPage, self).__init__(*args, **kwargs)

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK).click()

    def go_to_registration_page(self):
        reg_link = self.browser.find_element(*MainPageLocators.REG_LINK).click()

    def go_to_search_page(self):
        search_button = self.browser.find_element(*MainPageLocators.SEARCH_BUTTON).click()

    def search_test_course(self):
        search_button = self.browser.find_element(*MainPageLocators.SEARCH_BUTTON)
        search_button.send_keys("Test course")
        search_button.send_keys(Keys.ENTER)

    def user_login(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK).click()
        input_email = self.browser.find_element(*MainPageLocators.EMAIL)
        input_email.send_keys("grinuserqa2@mail.ru")
        input_password = self.browser.find_element(*MainPageLocators.PASSWORD)
        input_password.send_keys("QWEasd123")
        login_button = self.browser.find_element(*MainPageLocators.LOG_BUTTON).click()
        time.sleep(2)
        login_text = self.browser.find_element(*MainPageLocators.POPUP_LOGIN).text
        assert login_text == "Logged in."
        assert self.is_element_present(*MainPageLocators.USER_LOGIN_TEXT), "No Become an Author text"
        #close_notification = self.browser.find_element(*CoursePageLocators.CLOSE_NOTIFICATION).click()

    def author_login(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK).click()
        input_email = self.browser.find_element(*MainPageLocators.EMAIL)
        input_email.send_keys("grinqauser22@mail.ru")
        input_password = self.browser.find_element(*MainPageLocators.PASSWORD)
        input_password.send_keys("QWEasd123")
        login_button = self.browser.find_element(*MainPageLocators.LOG_BUTTON).click()
        time.sleep(2)
        login_text = self.browser.find_element(*MainPageLocators.POPUP_LOGIN).text
        assert login_text == "Logged in."
        time.sleep(2)
        #close_notification = self.browser.find_element(*CoursePageLocators.CLOSE_NOTIFICATION).click()
        #assert self.is_element_present(*MainPageLocators.WELCOME_TEXT), "No welcome text"

    def author_login_with_avatar(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK).click()
        input_email = self.browser.find_element(*MainPageLocators.EMAIL)
        input_email.send_keys("grinuserqa22@mail.ru")
        input_password = self.browser.find_element(*MainPageLocators.PASSWORD)
        input_password.send_keys("QWEasd123")
        login_button = self.browser.find_element(*MainPageLocators.LOG_BUTTON).click()
        time.sleep(2)
        login_text = self.browser.find_element(*MainPageLocators.POPUP_LOGIN).text
        assert login_text == "Logged in."
        time.sleep(2)
        #close_notification = self.browser.find_element(*CoursePageLocators.CLOSE_NOTIFICATION).click()
        #assert self.is_element_present(*MainPageLocators.WELCOME_TEXT), "No welcome text"

    def user_registration(self):
        f = faker.Faker()
        email = f.email()
        name = f.name()
        reg_link = self.browser.find_element(*MainPageLocators.REG_LINK).click()
        input_email = self.browser.find_element(*MainPageLocators.REG_EMAIL)
        input_email.send_keys("auto_py_"+email)
        input_fn = self.browser.find_element(*MainPageLocators.FIRST_NAME)
        input_fn.send_keys(name)
        input_ln = self.browser.find_element(*MainPageLocators.LAST_NAME)
        input_ln.send_keys(name)
        input_password = self.browser.find_element(*MainPageLocators.REG_PASSWORD)
        input_password.send_keys("QWEasd123")
        agree = self.browser.find_element(*MainPageLocators.AGREE).click()
        reg_button = self.browser.find_element(*MainPageLocators.REG_BUTTON).click()
        time.sleep(2)
        reg_text = self.browser.find_element(*MainPageLocators.POPUP_LOGIN).text
        assert reg_text == "User account successfully created."


    def author_registration(self):
        f = faker.Faker()
        email = f.email()
        name = f.name()
        title = f.company()
        reg_link = self.browser.find_element(*MainPageLocators.REG_LINK).click()
        subtopic_list = ['Academics', 'Arabic', 'English']
        toggler = self.browser.find_element(*MainPageLocators.TOGGLER).click()
        input_email = self.browser.find_element(*MainPageLocators.REG_EMAIL)
        input_email.send_keys("auto_py_"+email)
        input_fn = self.browser.find_element(*MainPageLocators.FIRST_NAME)
        input_fn.send_keys(name)
        input_ln = self.browser.find_element(*MainPageLocators.LAST_NAME)
        input_ln.send_keys(name)
        input_password = self.browser.find_element(*MainPageLocators.REG_PASSWORD)
        input_password.send_keys("QWEasd123")
        agree = self.browser.find_element(*MainPageLocators.AGREE).click()
        reg_button = self.browser.find_element(*MainPageLocators.REG_BUTTON).click()
        time.sleep(2)
        close_notification = self.browser.find_element(*CoursePageLocators.CLOSE_NOTIFICATION).click()
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'avatar.jpg')
        upload_photo = self.browser.find_element(*MainPageLocators.UPLOAD_AUTHOR_PHOTO)
        upload_photo.send_keys(file_path)
        topic = self.browser.find_element(*MainPageLocators.TOPIC).click()
        select_topic = self.browser.find_element(*MainPageLocators.SELECTED_TOPIC).click()
        subtopic = self.browser.find_element(*MainPageLocators.SUBTOPIC).click()
        select_subtopic = self.browser.find_element(*MainPageLocators.SELECTED_SUBTOPIC).click()
        time.sleep(2)
        job_title = self.browser.find_element(*MainPageLocators.JOB_TITLE)
        job_title.send_keys(title)
        time.sleep(2)
        next = self.browser.find_element(*MainPageLocators.NEXT).click()
        agree_author = self.browser.find_element(*MainPageLocators.AGREE_AUTHOR).click()
        complete = self.browser.find_element(*MainPageLocators.COMPLETE).click()
        time.sleep(2)

    def user_become_author(self):
        f = faker.Faker()
        title = f.company()
        become_author = self.browser.find_element(*MainPageLocators.BECOME_AUTHOR).click()
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'avatar.jpg')
        upload_photo = self.browser.find_element(*MainPageLocators.UPLOAD_AUTHOR_PHOTO).send_keys(file_path)
        topic = self.browser.find_element(*MainPageLocators.TOPIC).click()
        select_topic = self.browser.find_element(*MainPageLocators.SELECTED_TOPIC).click()
        time.sleep(3)
        subtopic = self.browser.find_element(*MainPageLocators.SUBTOPIC).click()
        select_subtopic = self.browser.find_element(*MainPageLocators.SELECTED_SUBTOPIC).click()
        job_title = self.browser.find_element(*MainPageLocators.JOB_TITLE)
        job_title.send_keys(title)
        time.sleep(5)
        next = self.browser.find_element(*MainPageLocators.NEXT).click()
        agree_author = self.browser.find_element(*MainPageLocators.AGREE_AUTHOR).click()
        complete = self.browser.find_element(*MainPageLocators.COMPLETE).click()
        time.sleep(2)
        reg_text = self.browser.find_element(*MainPageLocators.POPUP_LOGIN).text
        assert reg_text == "Author profile successfully created."

    def become_author_without_avatar(self):
        f = faker.Faker()
        title = f.company()
        become_author = self.browser.find_element(*MainPageLocators.BECOME_AUTHOR).click()
        topic = self.browser.find_element(*MainPageLocators.TOPIC).click()
        select_topic = self.browser.find_element(*MainPageLocators.SELECTED_TOPIC).click()
        time.sleep(3)
        subtopic = self.browser.find_element(*MainPageLocators.SUBTOPIC).click()
        select_subtopic = self.browser.find_element(*MainPageLocators.SELECTED_SUBTOPIC).click()
        job_title = self.browser.find_element(*MainPageLocators.JOB_TITLE)
        job_title.send_keys(title)
        time.sleep(5)
        next = self.browser.find_element(*MainPageLocators.NEXT).click()
        agree_author = self.browser.find_element(*MainPageLocators.AGREE_AUTHOR).click()
        complete = self.browser.find_element(*MainPageLocators.COMPLETE).click()
        time.sleep(2)
        reg_text = self.browser.find_element(*MainPageLocators.POPUP_LOGIN).text
        assert reg_text == "Author profile successfully created."

    def log_out(self):
        avatar_button = self.browser.find_element(*MainPageLocators.AVATAR_BUTTON_MENU).click()
        sign_out = self.browser.find_element(*MainPageLocators.SIGN_OUT).click()

    def log_out_with_avatar(self):
        has_avatar_button = self.browser.find_element(*MainPageLocators.HAS_AVATAR_BUTTON_MENU).click()
        sign_out = self.browser.find_element(*MainPageLocators.SIGN_OUT).click()

    def moderator_login(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK).click()
        input_email = self.browser.find_element(*MainPageLocators.EMAIL)
        input_email.send_keys("u21@d.com")
        input_password = self.browser.find_element(*MainPageLocators.PASSWORD)
        input_password.send_keys("0breedish")
        login_button = self.browser.find_element(*MainPageLocators.LOG_BUTTON).click()
        time.sleep(2)
        close_notification = self.browser.find_element(*CoursePageLocators.CLOSE_NOTIFICATION).click()
        assert self.is_element_present(*MainPageLocators.USER_LOGIN_TEXT), "No Become an Author text"
