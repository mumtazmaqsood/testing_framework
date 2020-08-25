import time
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    #Locators
    _login_link = "//a[@class='navbar-link fedora-navbar-link']"
    _email_id = "user_email"
    _password_id = "user_password"
    _login_btn = "commit"
#----------------------------------------------------------------------------------------------
# getting home page elements
# ----------------------------------------------------------------------------------------------
    def getLoginLink(self):
        return self.driver.find_element(By.XPATH, self._login_link)
    def getEmailField(self):
        return self.driver.find_element(By.ID, self._email_id)
    def getPasswordField(self):
        return self.driver.find_element(By.ID, self._password_id)
    def getLoginBtn(self):
        return self.driver.find_element(By.NAME, self._login_btn)

# ----------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------
    # enter and clicking  on home page elements
# ----------------------------------------------------------------------------------------------
    def clickLoginLink(self):
        self.getLoginLink().click()
    def enterEmail(self, email):
        self.getEmailField().send_keys(email)
    def enterPassword(self, password):
        self.getPasswordField().send_keys(password)
    def  clickLoginBtn(self):
        self.getLoginBtn().click()

# ----------------------------------------------------------------------------------------------



    def login(self, email, password):
        self.clickLoginLink()
        time.sleep(5)
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginBtn()