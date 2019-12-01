from selenium.webdriver.common.by import By

class Genric:
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

#-----------------------------------------------------------------------
    def getByType(self,locatortype):
        locator = locatortype.lower()
        if locator == 'id':
            return By.ID
        elif locator == 'name':
            return By.NAME
        elif locator == 'class_name':
            return By.CLASS_NAME
        elif locator == 'xpath':
            return By.XPATH
        else:
            print('locator',locatortype,'is not found')
        return False

#---------------------------------------------------------------------------

    def getElement(self,locatortype,locatorvalue):
        try:
            bytype = self.getByType(locatortype)
            element = self.driver.find_element(bytype,locatorvalue)
            print('element with locatortype',locatortype,'and locatorvalue',locatorvalue,'is not found')
        except:
            print('element without locatortype', locatortype, 'and locatorvalue', locatorvalue, 'is not found')
        return element

    def sendData(self,locatortype,locatorvalue,data):
        try:
            getelement = self.getElement(locatortype,locatorvalue)
            getelement.send_keys(data)
            print('data',data,'send the element with locatortype',locatorvalue,'with locatorvalue',locatorvalue)
        except:
            print('data',data,'is not sent to the element with locatortype',locatortype,'with locatorvalue', locatorvalue)

    def clickOn(self,locatortype,locatorvalue):
        try:
            getelement = self.getElement(locatortype,locatorvalue)
            getelement.click()
            print('clicked on the element with locatortype',locatorvalue,'and locatorvalue',locatorvalue)
        except:
            print('Not clicked on the element with locatortype', locatorvalue, 'and locatorvalue', locatorvalue)
