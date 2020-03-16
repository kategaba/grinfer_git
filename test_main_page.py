from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.course_page import CoursePage
import pytest
import time

#link = "https://foo:bar@test.grinfer.com/"

#@pytest.mark.need_review
#pytest -v -m need_review

class TestRegistraion():
    def test_user_can_go_to_registration_page(self, browser):
        page = MainPage(browser)
        page.open()
        page.go_to_registration_page()

    #@pytest.mark.need_review
    def test_user_can_go_to_login_page(self, browser):
        page = MainPage(browser)
        page.open()
        page.go_to_login_page()

    def test_user_can_go_to_search_page(self, browser):
        page = MainPage(browser)
        page.open()
        page.go_to_search_page()

    #@pytest.mark.need_review
    def test_user_can_login(self, browser):
        page = MainPage(browser)
        page.open()
        page.user_login()

    @pytest.mark.need_review
    def test_author_can_login(self, browser):
        page = MainPage(browser)
        page.open()
        page.author_login()
        page.log_out()

    def test_author_can_login_with_avatar(self, browser):
        page = MainPage(browser)
        page.open()
        page.author_login_with_avatar()
        page.log_out_with_avatar()

    #@pytest.mark.need_review
    def test_user_can_registration(self, browser):
        page = MainPage(browser)
        page.open()
        page.user_registration()

    #@pytest.mark.need_review
    def test_author_can_registration(self, browser):
        page = MainPage(browser)
        page.open()
        page.author_registration()

    #@pytest.mark.need_review
    def test_user_become_author(self, browser):
        page = MainPage(browser)
        page.open()
        page.user_registration()
        page.user_become_author()

    def test_user_become_author_without_avatar(self, browser):
        page = MainPage(browser)
        page.open()
        page.user_registration()
        page.become_author_without_avatar()

    # @pytest.mark.need_review
    def test_author_can_create_draft_course(self, browser):
        page = MainPage(browser)
        page.open()
        page.author_registration()
        page1 = CoursePage(browser)
        page1.create_draft_course()

    # @pytest.mark.need_review
    def test_author_can_edit_draft_course(self, browser):
        page = MainPage(browser)
        page.open()
        page.author_login()
        page1 = CoursePage(browser)
        page1.edit_draft_course()

    def test_author_can_edit_lesson_draft_course(self, browser):
        page = MainPage(browser)
        page.open()
        page.author_login()
        page1 = CoursePage(browser)
        page1.add_lesson_draft_course()

    # @pytest.mark.need_review
    def test_author_can_delete_lesson_draft_course(self, browser):
        page = MainPage(browser)
        page.open()
        page.author_login()
        page1 = CoursePage(browser)
        page1.delete_lesson_draft_course()

    # @pytest.mark.parametrize('execution_number', range(20))
    def test_author_can_delete_draft_course(self, browser):
        page = MainPage(browser)
        page.open()
        page.author_login()
        page1 = CoursePage(browser)
        page1.delete_draft_course()

    def test_new_author_can_send_new_course_to_moderation(self, browser):
        page = MainPage(browser)
        page.open()
        page.author_registration()
        page1 = CoursePage(browser)
        page1.create_draft_course()
        page1.send_course_to_moderation()

    def test_author_can_send_new_course_to_moderation(self, browser):
        page = MainPage(browser)
        page.open()
        page.author_login()
        page1 = CoursePage(browser)
        page1.create_draft_course()
        page1.send_course_to_moderation()

    def test_moderator_can_decline_course(self, browser):
        page = MainPage(browser)
        page.open()
        page.moderator_login()
        page1 = CoursePage(browser)
        page1.moderator_decline_course()
        page.log_out()
        page2 = BasePage(browser)
        page2.clean_cookie()

    def test_moderator_can_approve_course(self, browser):
        page = MainPage(browser)
        page.open()
        page.moderator_login()
        page1 = CoursePage(browser)
        page1.moderator_approve_course()
        page.log_out()
        page2 = BasePage(browser)
        page2.clean_cookie()

    def test_author_can_update_course_price(self, browser):
        page = MainPage(browser)
        page.open()
        page.author_login_with_avatar()
        page1 = CoursePage(browser)
        page1.update_course_price()

    def test_author_can_hide_course(self, browser):
        page = MainPage(browser)
        page.open()
        page.author_login_with_avatar()
        page1 = CoursePage(browser)
        page1.hide_course()

    def test_author_can_unhide_course(self, browser):
        page = MainPage(browser)
        page.open()
        page.author_login_with_avatar()
        page1 = CoursePage(browser)
        page1.unhide_course()

    def test_author_can_delete_course(self, browser):
        page = MainPage(browser)
        page.open()
        page.author_login()
        page1 = CoursePage(browser)
        page1.delete_course()

    def test_user_can_buy_course(self, browser):
        page = MainPage(browser)
        page.open()
        page.user_registration()
        page.search_test_course()
        page1 = CoursePage(browser)
        page1.user_buy_course()

    def test_guest_can_buy_course(self, browser):
        page = MainPage(browser)
        page.open()
        page.search_test_course()
        page1 = CoursePage(browser)
        page1.guest_buy_course()

    def test_user_start_course_after_purchase(self, browser):
        page = MainPage(browser)
        page.open()
        page.user_registration()
        page.search_test_course()
        page1 = CoursePage(browser)
        page1.user_buy_course()
        page1.user_start_learning_course()
        page1.user_start_course()

    def test_user_complete_course(self, browser):
        page = MainPage(browser)
        page.open()
        page.user_registration()
        page.search_test_course()
        page1 = CoursePage(browser)
        page1.user_buy_course()
        page1.user_start_learning_course()
        page1.user_start_course()
        page1.user_complete_course()