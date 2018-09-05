
from util.chrome_driver import ChromeDriver
from pages.login_page import Login
class Start():

    def startLogin(self):
        driver = ChromeDriver.getFromChrome(ChromeDriver)
        login = Login(driver)
        login.sendUsername()
        login.sendPassword()
        login.clicklogIn()

startt = Start()
startt.startLogin()