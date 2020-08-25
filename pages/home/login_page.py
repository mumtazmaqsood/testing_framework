import time
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver


class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    # _login_link = "//a[@class='navbar-link fedora-navbar-link']"
    _login_link = "Login"
    _email_id = "user_email"
    _password_id = "user_password"
    _login_btn = "commit"
#----------------------------------------------------------------------------------------------
# getting home page elements
# ----------------------------------------------------------------------------------------------
#     def getLoginLink(self):
#         return self.driver.find_element(By.XPATH, self._login_link)
#     def getEmailField(self):
#         return self.driver.find_element(By.ID, self._email_id)
#     def getPasswordField(self):
#         return self.driver.find_element(By.ID, self._password_id)
#     def getLoginBtn(self):
#         return self.driver.find_element(By.NAME, self._login_btn)


#Actions performed on the elements , elementClick(), SendKeys() are the dynamic methods created in base class
# ----------------------------------------------------------------------------------------------
    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="link")
    def enterEmail(self, email):
        self.sendKeys(email, self._email_id)
    def enterPassword(self, password):
        self.sendKeys(password, self._password_id)
    def clickLoginBtn(self):
        self.elementClick(self._login_btn, locatorType="name")
# ----------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------
#functionality, wrape all the actions
    def login(self, email, password):
        self.clickLoginLink()
        time.sleep(5)
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginBtn()