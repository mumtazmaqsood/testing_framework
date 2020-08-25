import time
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        login_link = self.driver.find_element(By.XPATH, "//a[@class='navbar-link fedora-navbar-link']")
        login_link.click()
        time.sleep(5)
        email_id = self.driver.find_element(By.ID, "user_email")
        email_id.send_keys(username)
        password_id = self.driver.find_element(By.ID, "user_password")
        password_id.send_keys(password)
        login_btn = self.driver.find_element(By.NAME, "commit")
        login_btn.click()