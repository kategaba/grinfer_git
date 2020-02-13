from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.course_page import CoursePage
import pytest
import time
import requests
from selenium import webdriver
from requests.auth import HTTPBasicAuth
from getpass import getpass

link = "https://foo:bar@test.grinfer.com/"

#@pytest.mark.need_review
#pytest -v -m need_review

class TestRegistraionCreationCourse():
    def test_user_can_go_to_registration_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_registration_page()

    #@pytest.mark.need_review
    def test_user_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()

    def test_user_can_go_to_search_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_search_page()

    #@pytest.mark.need_review
    def test_user_can_login(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.user_login()

    @pytest.mark.need_review
    def test_author_can_login(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.author_login()
        page1 = BasePage(browser, link)
        page1.clean_cookie()

    #@pytest.mark.need_review
    def test_user_can_registration(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.user_registration()

    #@pytest.mark.need_review
    def test_author_can_registration(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.author_registration()

    #@pytest.mark.need_review
    def test_user_become_author(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.become_author()


    #@pytest.mark.need_review
    def test_author_can_create_draft_course(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.author_login()
        page1 = CoursePage(browser, link)
        page1.create_draft_course()

    #@pytest.mark.need_review
    def test_author_can_edit_draft_course(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.author_login()
        page1 = CoursePage(browser, link)
        page1.edit_draft_course()

    def test_author_can_edit_lesson_draft_course(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.author_login()
        page1 = CoursePage(browser, link)
        page1.add_lesson_draft_course()

    def test_author_can_edit_lesson_draft_course(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.author_login()
        page1 = CoursePage(browser, link)
        page1.edit_lesson_draft_course()

    #@pytest.mark.need_review
    def test_author_can_delete_lesson_draft_course(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.author_login()
        page1 = CoursePage(browser, link)
        page1.delete_lesson_draft_course()

    @pytest.mark.parametrize('execution_number', range(20))
    def test_author_can_delete_draft_course(self, browser, execution_number):
        page = MainPage(browser, link)
        page.open()
        page.author_login()
        page1 = CoursePage(browser, link)
        page1.delete_draft_course()

    def test_author_can_send_course_to_moderation(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.author_login()
        page1 = CoursePage(browser, link)
        page1.create_draft_course()
        page1.send_course_to_moderation()

    def test_moderator_can_decline_course(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.moderator_login()
        page1 = CoursePage(browser, link)
        page1.moderator_decline_course()
        page.log_out()
        page2 = BasePage(browser, link)
        page2.clean_cookie()

    def test_moderator_can_approve_course(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.moderator_login()
        page1 = CoursePage(browser, link)
        page1.moderator_approve_course()
        page.log_out()
        page2 = BasePage(browser, link)
        page2.clean_cookie()

    def test_author_can_delete_course(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.author_login()
        page1 = CoursePage(browser, link)
        page1.delete_course()

