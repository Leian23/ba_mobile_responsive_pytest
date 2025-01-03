from selenium.webdriver.common.keys import Keys
from Pages.access_page import BasePage
from Utilities.baseclass import BaseClass
from Assets.credentials import username, password
import time


class TestBase(BaseClass):
    def test_homepage(self):
        homepage = BasePage(self.driver)
        homepage.get_icon().click()

    def test_login(self):
        homepage = BasePage(self.driver)
        homepage.get_username().send_keys(username)
        homepage.get_password().send_keys(password)
        homepage.get_submit().send_keys(Keys.RETURN)
        time.sleep(2)

    def test_explore(self):
        homepage = BasePage(self.driver)
        homepage.get_hamburger_menu().click()
        time.sleep(2)
        homepage.get_customizer().click()
        time.sleep(5)


