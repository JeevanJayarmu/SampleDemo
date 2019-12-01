from time import sleep
from base.genric import Genric

class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    usn_text_field = 'email'
    pwd_text_field = 'pass'
    login_button = 'loginbutton'

    # def getUsernameTextField(self):
    #     return self.driver.find_element_by_id(self.usn_text_field)
    #
    # def getPasswordTextField(self):
    #     return self.driver.find_element_by_name(self.pwd_text_field)
    #
    # def getloginButton(self):
    #     return self.driver.find_element_by_id(self.login_button)


    def enterUsername(self,username):
        self.sendData('id',self.usn_text_field,username)

    def enterPassword(self,password):
        self.sendData('name',self.pwd_text_field,password)

    def clickLoginButton(self):
        self.clickOn('id',self.login_button)

