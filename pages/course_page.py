from selenium.webdriver.common.by import By
from locators import CoursePageLocators
from locators import MainPageLocators
from locators import PaymentLocators
from .base_page import BasePage
from .main_page import MainPage
import time
import os
import faker
import random
from faker import Faker
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CoursePage(BasePage):
    def create_draft_course(self):
        fake = Faker()
        course_title = fake.text()
        course_description = fake.text()
        avatar_button = self.browser.find_element(*MainPageLocators.AVATAR_BUTTON_MENU).click()
        time.sleep(1)
        courses_tab = self.browser.find_element(*MainPageLocators.AVATAR_MENU_COURSES).click()
        #courses_tab = self.browser.find_element(*CoursePageLocators.COURSES).click()
        time.sleep(2)
        create_new_course = self.browser.find_element(*CoursePageLocators.CREATE_NEW_COURSE).click()
        topic = self.browser.find_element(*CoursePageLocators.TOPIC).click()
        select_topic = self.browser.find_element(*CoursePageLocators.SELECTED_TOPIC).click()
        subtopic = self.browser.find_element(*CoursePageLocators.SUBTOPIC).click()
        select_subtopic = self.browser.find_element(*CoursePageLocators.SELECTED_SUBTOPIC).click()
        language = self.browser.find_element(*CoursePageLocators.LANGUAGE).click()
        select_language = self.browser.find_element(*CoursePageLocators.SELECT_LANGUAGE).click()
        time.sleep(1)
        upload_course_cover = self.browser.find_element(*CoursePageLocators.UPLOAD_COURSE_COVER).click()
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'python.jpg')
        upload_from_drive = self.browser.find_element(*CoursePageLocators.UPLOAD_FROM_HARD_DRIVE).send_keys(file_path)
        time.sleep(5)
        #select_file_button = self.browser.find_element(*CoursePageLocators.SELECT_FILE_BUTTON).click()
        #select_file = self.browser.find_element(*CoursePageLocators.SELECT_FILE).click()
        #close_notification = self.browser.find_element(*CoursePageLocators.CLOSE_NOTIFICATION).click()
        complete_button = self.browser.find_element(*CoursePageLocators.COMPLETE).click()
        input_course_title = self.browser.find_element(*CoursePageLocators.COURSE_TITLE).send_keys("Test course")
        input_course_description = self.browser.find_element(*CoursePageLocators.COURSE_DESCRIPTION).send_keys("Test description")
        upload_welcome_video_button = self.browser.find_element(*CoursePageLocators.UPLOAD_WELCOME).click()
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'python.mp4')
        upload_from_drive = self.browser.find_element(*CoursePageLocators.UPLOAD_FROM_HARD_DRIVE).send_keys(file_path)
        time.sleep(5)
        #select_file_button = self.browser.find_element(*CoursePageLocators.SELECT_FILE_BUTTON).click()
        #select_file = self.browser.find_element(*CoursePageLocators.SELECT_FILE).click()
        #close_notification = self.browser.find_element(*CoursePageLocators.CLOSE_NOTIFICATION).click()
        complete_button = self.browser.find_element(*CoursePageLocators.COMPLETE).click()
        click_course_price = self.browser.find_element(*CoursePageLocators.COURSE_PRICE).click()
        select_price = self.browser.find_element(*CoursePageLocators.SELECT_PRICE).click()
        time.sleep(2)
        next_create_lesson = self.browser.find_element(*CoursePageLocators.NEXT).click()
        time.sleep(2)
        create_new_lesson = self.browser.find_element(*CoursePageLocators.CREATE_NEW_LESSON).click()
        input_lesson_title = self.browser.find_element(*CoursePageLocators.LESSON_TITLE).send_keys("Test lesson title")
        input_lesson_description = self.browser.find_element(*CoursePageLocators.LESSON_DESCRIPTION).send_keys("Test lesson description")
        #lesson_content = self.browser.find_element(*CoursePageLocators.LESSON_CONTENT).send_keys("Add an image")
        lesson_new_line = self.browser.find_element(*CoursePageLocators.LESSON_CONTENT).send_keys(Keys.ENTER)
        add_button = self.browser.find_element(*CoursePageLocators.ADD_BUTTON).click()
        add_image = self.browser.find_element(*CoursePageLocators.ADD_IMAGE).click()
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'course_cover.jpeg')
        upload_from_drive = self.browser.find_element(*CoursePageLocators.UPLOAD_FROM_HARD_DRIVE).send_keys(file_path)
        time.sleep(5)
        #select_file_button = self.browser.find_element(*CoursePageLocators.SELECT_FILE_BUTTON).click()
        #select_file = self.browser.find_element(*CoursePageLocators.SELECT_FILE).click()
        #close_notification = self.browser.find_element(*CoursePageLocators.CLOSE_NOTIFICATION).click()
        complete_button = self.browser.find_element(*CoursePageLocators.COMPLETE).click()
        time.sleep(2)
        create_lesson_button = self.browser.find_element(*CoursePageLocators.CREATE_LESSON_BUTTON).click()
        time.sleep(2)

    def edit_draft_course(self):
        fake = Faker()
        course_title = fake.text()
        course_description = fake.text()
        #courses_tab = self.browser.find_element(*CoursePageLocators.COURSES).click()
        avatar_button = self.browser.find_element(*MainPageLocators.HAS_AVATAR_BUTTON_MENU).click()
        time.sleep(1)
        courses_tab = self.browser.find_element(*MainPageLocators.AVATAR_MENU_COURSES).click()
        dot_menu = self.browser.find_element(*CoursePageLocators.DOTS_MENU).click()
        edit_draft = self.browser.find_element(*CoursePageLocators.EDIT_DRAFT).click()
        edit_course_cover = self.browser.find_element(*CoursePageLocators.EDIT_COURSE_COVER).click()
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'python.jpg')
        upload_from_drive = self.browser.find_element(*CoursePageLocators.UPLOAD_FROM_HARD_DRIVE).send_keys(file_path)
        time.sleep(5)
        #select_file_button = self.browser.find_element(*CoursePageLocators.SELECT_FILE_BUTTON).click()
        #select_file = self.browser.find_element(*CoursePageLocators.SELECT_FILE).click()
        #close_notification = self.browser.find_element(*CoursePageLocators.CLOSE_NOTIFICATION).click()
        complete_button = self.browser.find_element(*CoursePageLocators.COMPLETE).click()
        time.sleep(2)
        input_course_title = self.browser.find_element(*CoursePageLocators.COURSE_TITLE).send_keys("Test course")
        input_course_description = self.browser.find_element(*CoursePageLocators.COURSE_DESCRIPTION).send_keys("Test description")
        edit_welcome_video_button = self.browser.find_element(*CoursePageLocators.EDIT_WELCOME).click()
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'python.mp4')
        upload_from_drive = self.browser.find_element(*CoursePageLocators.UPLOAD_FROM_HARD_DRIVE).send_keys(file_path)
        time.sleep(5)
        #select_file_button = self.browser.find_element(*CoursePageLocators.SELECT_FILE_BUTTON).click()
        #select_file = self.browser.find_element(*CoursePageLocators.SELECT_FILE).click()
        #close_notification = self.browser.find_element(*CoursePageLocators.CLOSE_NOTIFICATION).click()
        complete_button = self.browser.find_element(*CoursePageLocators.COMPLETE).click()
        time.sleep(2)
        self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        time.sleep(2)
        save_draft = self.browser.find_element(*CoursePageLocators.SAVE_DRAFT).click()
        time.sleep(2)

    def edit_lesson_draft_course(self):
        avatar_button = self.browser.find_element(*MainPageLocators.HAS_AVATAR_BUTTON_MENU).click()
        time.sleep(1)
        courses_tab = self.browser.find_element(*MainPageLocators.AVATAR_MENU_COURSES).click()
        #courses_tab = self.browser.find_element(*CoursePageLocators.COURSES).click()
        dot_menu = self.browser.find_element(*CoursePageLocators.DOTS_MENU).click()
        edit_draft = self.browser.find_element(*CoursePageLocators.EDIT_DRAFT).click()
        course_lessons_tab = self.browser.find_element(*CoursePageLocators.COURSE_LESSON).click()
        dot_menu = self.browser.find_element(*CoursePageLocators.DOTS_MENU).click()
        edit_leeson = self.browser.find_element(*CoursePageLocators.EDIT_LESSON).click()
        input_lesson_title = self.browser.find_element(*CoursePageLocators.LESSON_TITLE).send_keys("Test lesson title")
        input_lesson_description = self.browser.find_element(*CoursePageLocators.LESSON_DESCRIPTION).send_keys("Test lesson description")
        lesson_content = self.browser.find_element(*CoursePageLocators.LESSON_CONTENT).send_keys("Add an image")
        lesson_new_line = self.browser.find_element(*CoursePageLocators.LESSON_CONTENT).send_keys(Keys.ENTER)
        #lesson_content = self.browser.find_element(*CoursePageLocators.LESSON_CONTENT).click()
        add_button = self.browser.find_element(*CoursePageLocators.ADD_BUTTON).click()
        add_image = self.browser.find_element(*CoursePageLocators.ADD_IMAGE).click()
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'course_cover.jpeg')
        upload_from_drive = self.browser.find_element(*CoursePageLocators.UPLOAD_FROM_HARD_DRIVE).send_keys(file_path)
        time.sleep(2)
        #select_file_button = self.browser.find_element(*CoursePageLocators.SELECT_FILE_BUTTON).click()
        #select_file = self.browser.find_element(*CoursePageLocators.SELECT_FILE).click()
        #close_notification = self.browser.find_element(*CoursePageLocators.CLOSE_NOTIFICATION).click()
        complete_button = self.browser.find_element(*CoursePageLocators.COMPLETE).click()
        time.sleep(2)
        self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        time.sleep(2)
        save_lesson_button = self.browser.find_element(*CoursePageLocators.SAVE_LESSON_BUTTON).click()
        time.sleep(2)

    def add_lesson_draft_course(self):
        avatar_button = self.browser.find_element(*MainPageLocators.HAS_AVATAR_BUTTON_MENU).click()
        time.sleep(1)
        courses_tab = self.browser.find_element(*MainPageLocators.AVATAR_MENU_COURSES).click()
        #courses_tab = self.browser.find_element(*CoursePageLocators.COURSES).click()
        dot_menu = self.browser.find_element(*CoursePageLocators.DOTS_MENU).click()
        edit_draft = self.browser.find_element(*CoursePageLocators.EDIT_DRAFT).click()
        course_lessons_tab = self.browser.find_element(*CoursePageLocators.COURSE_LESSON).click()
        create_new_lesson = self.browser.find_element(*CoursePageLocators.CREATE_NEW_LESSON).click()
        input_lesson_title = self.browser.find_element(*CoursePageLocators.LESSON_TITLE).send_keys("Test lesson title")
        input_lesson_description = self.browser.find_element(*CoursePageLocators.LESSON_DESCRIPTION).send_keys("Test lesson description")
        lesson_content = self.browser.find_element(*CoursePageLocators.LESSON_CONTENT).send_keys("Add an image")
        time.sleep(2)
        self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        time.sleep(2)
        create_new_lesson = self.browser.find_element(*CoursePageLocators.CREATE_NEW_LESSON).click()
        time.sleep(2)

    def delete_lesson_draft_course(self):
        avatar_button = self.browser.find_element(*MainPageLocators.HAS_AVATAR_BUTTON_MENU).click()
        time.sleep(1)
        courses_tab = self.browser.find_element(*MainPageLocators.AVATAR_MENU_COURSES).click()
        #courses_tab = self.browser.find_element(*CoursePageLocators.COURSES).click()
        dot_menu = self.browser.find_element(*CoursePageLocators.DOTS_MENU).click()
        edit_draft = self.browser.find_element(*CoursePageLocators.EDIT_DRAFT).click()
        course_lessons_tab = self.browser.find_element(*CoursePageLocators.COURSE_LESSON).click()
        dot_menu = self.browser.find_element(*CoursePageLocators.DOTS_MENU).click()
        edit_lesson = self.browser.find_element(*CoursePageLocators.EDIT_LESSON).click()
        delete_lesson_button = self.browser.find_element(*CoursePageLocators.DELETE_LESSON_BUTTON).click()
        time.sleep(1)
        delete_lesson_confirm = self.browser.find_element(*CoursePageLocators.DELETE_LESSON_CONFIRM).click()
        time.sleep(1)

    def delete_draft_course(self):
        avatar_button = self.browser.find_element(*MainPageLocators.HAS_AVATAR_BUTTON_MENU).click()
        time.sleep(1)
        courses_tab = self.browser.find_element(*MainPageLocators.AVATAR_MENU_COURSES).click()
        #courses_tab = self.browser.find_element(*CoursePageLocators.COURSES).click()
        dot_menu = self.browser.find_element(*CoursePageLocators.DOTS_MENU).click()
        time.sleep(1)
        delete_draft = self.browser.find_element(*CoursePageLocators.DELETE_DRAFT).click()
        time.sleep(1)
        delete_confirm = self.browser.find_element(*CoursePageLocators.DELETE_CONFIRM).click()
        time.sleep(1)

    def back_to_courses(self):
        back_button = self.browser.find_element(*CoursePageLocators.BACK_BUTTON).click()

    def send_course_to_moderation(self):
        publish_course = self.browser.find_element(*CoursePageLocators.PUBLISH_COURSE).click()
        time.sleep(2)
        send_to_moderation = self.browser.find_element(*CoursePageLocators.SEND_TO_MODERATION).click()

    def moderator_approve_course(self):
        avatar_button = self.browser.find_element(*MainPageLocators.AVATAR_BUTTON_MENU).click()
        time.sleep(1)
        courses_on_review = self.browser.find_element(*CoursePageLocators.COURSES_ON_REVIEW).click()
        self.browser.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
        open_course = self.browser.find_element(*CoursePageLocators.COURSE_TILE).click()
        self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        approve = self.browser.find_element(*CoursePageLocators.APPROVE).click()
        time.sleep(1)
        confirm_approve = self.browser.find_element(*CoursePageLocators.MODERATOR_CONFIRM).click()
        time.sleep(2)

    def moderator_decline_course(self):
        open_course = self.browser.find_element(*CoursePageLocators.COURSE_TILE).click()
        self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        approve = self.browser.find_element(*CoursePageLocators.DECLINE).click()
        time.sleep(1)
        input_comment = self.browser.find_element(*CoursePageLocators.COMMENT).send_keys("Please, complete your course!")
        confirm_approve = self.browser.find_element(*CoursePageLocators.MODERATOR_CONFIRM).click()
        time.sleep(2)

    def delete_course(self):
        avatar_button = self.browser.find_element(*MainPageLocators.HAS_AVATAR_BUTTON_MENU).click()
        time.sleep(1)
        courses_tab = self.browser.find_element(*MainPageLocators.AVATAR_MENU_COURSES).click()
        #courses_tab = self.browser.find_element(*CoursePageLocators.COURSES).click()
        time.sleep(2)
        #self.browser.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
        dot_menu = self.browser.find_element(*CoursePageLocators.DOTS_MENU).click()
        time.sleep(2)
        delete_course = self.browser.find_element(*CoursePageLocators.DELETE_COURSE).click()
        time.sleep(2)
        delete_confirm = self.browser.find_element(*CoursePageLocators.DELETE_CONFIRM).click()

    def update_course_price(self):
        avatar_button = self.browser.find_element(*MainPageLocators.HAS_AVATAR_BUTTON_MENU).click()
        time.sleep(1)
        courses_tab = self.browser.find_element(*MainPageLocators.AVATAR_MENU_COURSES).click()
        #courses_tab = self.browser.find_element(*CoursePageLocators.COURSES).click()
        #time.sleep(2)
        #self.browser.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
        dot_menu = self.browser.find_element(*CoursePageLocators.DOTS_MENU).click()
        time.sleep(2)
        update_price = self.browser.find_element(*CoursePageLocators.UPDATE_PRICE_BUTTON).click()
        click_course_price = self.browser.find_element(*CoursePageLocators.COURSE_PRICE).click()
        select_price = self.browser.find_element(*CoursePageLocators.SELECT_PRICE).click()
        self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        time.sleep(2)
        update_on_market = self.browser.find_element(*CoursePageLocators.UPDATE_ON_MARKET).click()

    def hide_course(self):
        avatar_button = self.browser.find_element(*MainPageLocators.HAS_AVATAR_BUTTON_MENU).click()
        time.sleep(1)
        courses_tab = self.browser.find_element(*MainPageLocators.AVATAR_MENU_COURSES).click()
        #courses_tab = self.browser.find_element(*CoursePageLocators.COURSES).click()
        #time.sleep(2)
        #self.browser.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
        dot_menu = self.browser.find_element(*CoursePageLocators.DOTS_MENU).click()
        time.sleep(2)
        hide_price = self.browser.find_element(*CoursePageLocators.HIDE_COURSE).click()
        time.sleep(2)

    def unhide_course(self):
        avatar_button = self.browser.find_element(*MainPageLocators.HAS_AVATAR_BUTTON_MENU).click()
        time.sleep(1)
        courses_tab = self.browser.find_element(*MainPageLocators.AVATAR_MENU_COURSES).click()
        #courses_tab = self.browser.find_element(*CoursePageLocators.COURSES).click()
        #time.sleep(2)
        #self.browser.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
        dot_menu = self.browser.find_element(*CoursePageLocators.DOTS_MENU).click()
        time.sleep(2)
        hide_price = self.browser.find_element(*CoursePageLocators.UNHIDE_COURSE).click()
        time.sleep(2)

    def user_buy_course(self):
        card_number = "4242424242424242"
        exp_date = "12/21"
        cvc = "123"
        open_course = self.browser.find_element(*CoursePageLocators.COURSE_TILE).click()
        buy_now = self.browser.find_element(*CoursePageLocators.BUY_NOW).click()
        time.sleep(2)
        input_card_number = self.browser.find_element(*PaymentLocators.CARD_NUMBER)
        for ch in card_number:
            input_card_number.send_keys(ch)
            time.sleep(0.1)
        time.sleep(1)
        input_exp_date = self.browser.find_element(*PaymentLocators.EXPIRE_DATE)
        input_exp_date.send_keys(exp_date)
        input_cvc = self.browser.find_element(*PaymentLocators.CVC)
        input_cvc.send_keys(cvc)
        complete_payment = self.browser.find_element(*PaymentLocators.COMPLETE_PAYMENT).click()
        time.sleep(10)

    def guest_buy_course(self):
        f = faker.Faker()
        email = f.email()
        password = "QWEasd123"
        card_number = "4242424242424242"
        exp_date = "12/21"
        cvc = "123"
        open_course = self.browser.find_element(*CoursePageLocators.COURSE_TILE).click()
        buy_now = self.browser.find_element(*CoursePageLocators.BUY_NOW).click()
        time.sleep(2)
        input_email = self.browser.find_element(*PaymentLocators.FAST_EMAIL)
        input_email.send_keys("auto_py_"+email)
        input_password = self.browser.find_element(*PaymentLocators.FAST_PASSWORD)
        input_password.send_keys(password)
        create_account = self.browser.find_element(*PaymentLocators.CREATE_ACCOUNT).click()
        time.sleep(1)
        input_card_number = self.browser.find_element(*PaymentLocators.CARD_NUMBER)
        for ch in card_number:
            input_card_number.send_keys(ch)
            time.sleep(0.1)
        time.sleep(1)
        input_exp_date = self.browser.find_element(*PaymentLocators.EXPIRE_DATE)
        input_exp_date.send_keys(exp_date)
        input_cvc = self.browser.find_element(*PaymentLocators.CVC)
        input_cvc.send_keys(cvc)
        complete_payment = self.browser.find_element(*PaymentLocators.COMPLETE_PAYMENT).click()
        time.sleep(10)

    def user_start_learning_course(self):
        start_learning = self.browser.find_element(*CoursePageLocators.START_LEARNING).click()

    def user_start_course(self):
        start_course = self.browser.find_element(*CoursePageLocators.START_COURSE).click()

    def user_complete_course(self):
        complete_lesson = self.browser.find_element(*CoursePageLocators.COMPLETE_LESSON).click()
        assert self.is_element_present(*CoursePageLocators.COMPLETED_LABEL), "No completed label"
        #completed_label = self.browser.find_element(*CoursePageLocators.COMPLETED_LABEL).text
        #assert completed_label == "COMPLETED"