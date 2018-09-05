import os
from selenium import webdriver

class ChromeDriver():

    def getFromChrome(self):
        baseUrl = "https://www.monkeytest1.com/analyze/browse/VWAr26i5YgzkwWj2iS3kb_2B_2B0lpw6te41JtqDNA4TXz8_3D"
        driverLocation = 'D:\Selenium Chrome Driver\chromedriver.exe'
        os.environ['webdriver.chrome.driver'] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get(baseUrl)
        return driver