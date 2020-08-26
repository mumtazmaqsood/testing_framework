from selenium import webdriver
from pages.home.login_page import LoginPage
import time
import unittest
import pytest


class LoginTests(unittest.TestCase):

    baseUrl = "https://letskodeit.teachable.com/"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(baseUrl)
    driver.implicitly_wait(2)
    lp = LoginPage(driver)

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        # self.driver.get(self.baseUrl)
        self.lp.login("test@email.com", "abcabcdedf")
        result = self.lp.verfiyLoginFailed()
        assert result == True

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("test@email.com", "abcabc")
        result = self.lp.verfiyLoginSuccessful()
        assert result == True
        self.driver.quit()


