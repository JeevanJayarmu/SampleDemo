from selenium import webdriver
from time import sleep
from page.loginpage import LoginPage

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.facebook.com')
driver.implicitly_wait(10)

lp = LoginPage(driver)
lp.enterUsername('jeevanjeev111@gmail.com')
lp.enterPassword('Bfacebook')
lp.clickLoginButton()