import time
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging



class LoginPage(SeleniumDriver):

    log = cl.customLogger(logLevel=logging.DEBUG)
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    _login_link = "Login"
    _email_id = "user_email"
    _password_id = "user_password"
    _login_btn = "commit"
    _login_successful_element = "//img[@class='course-box-image']"
    _login_unsuccessful_element = "//div[contains(text(),'Invalid email or password')]"

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
    def login(self, email="", password=""):
        self.clickLoginLink()
        # time.sleep(2)
        self.clearFields()
        self.enterEmail(email)
        self.enterPassword(password)
        time.sleep(3)
        self.clickLoginBtn()

#isElementPresent() return true or false , check element is present or not, after logging in
    def verfiyLoginSuccessful(self):
        result = self.isElementPresent("//img[@class='course-box-image']", locatorType="xpath")
        return result

    def verfiyLoginFailed(self):
        result = self.isElementPresent("//div[contains(text(),'Invalid email or password')]", locatorType="xpath")
        return result

#this method use to clear text fields
    def clearFields(self):
        email_field = self.getElement(self._email_id)
        email_field.clear()
        password_field = self.getElement(self._password_id)
        password_field.clear()