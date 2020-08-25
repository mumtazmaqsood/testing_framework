from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
import time
import unittest


class LoginTests(unittest.TestCase):
    def test_validLogin(self):
        baseUrl = "https://letskodeit.teachable.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(2)

        lp = LoginPage(driver)
        lp.login("test@email.com", "abcabc")

        user_icon = driver.find_element(By.XPATH, "//img[@class='course-box-image']")
        if user_icon is not None :
            print("Login test passed")
        else:
            print("Login Test Failed")
        time.sleep(5)

