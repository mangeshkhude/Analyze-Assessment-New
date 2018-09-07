from util.basepage import BasePage
import time
import util.custom_logger as cl
import logging

class Login(BasePage):

    _username = "username"
    _password = "password"
    _login_button = "//button[contains(@type,'submit')]"
    _verify_user = "//a[@id='userAcctTab_MainMenu']"
    _sign_out = "//ul[contains(@class,'nav-submenu')]//li[contains(@class,'last')]/a[contains(text(), 'Sign Out' )]"
    _respondant = "//a[contains(@class,'respondent-goto-menu-btn sm-float-l wds-button wds-button--util wds-button--arrow-down')]"
    _respondant_count = "//input[contains(@value,'2')]"
    _previous_respondant = "//a[contains(@title,'Previous respondent ( j )')]"
    _first_respondant = "//input[contains(@value,'1')]"
    _filter = "//a[@id='FilterBuilderTab']"
    _filter_by_question = "//a[contains(text(),'Filter by Question and Answer')]"
    _select_question_filter = "//section[contains(@class,'lane qna select open')]//select"
    _select_question_option = "//section[contains(@class,'lane qna select open')]//option[contains(@value,'114042894')][contains(text(),'Q1: Which color is the best?')]"
    _select_answer = "//label[contains(text(),'blue')]"
    _apply_filter = "//a[contains(@class,'wds-button wds-button--primary wds-button--sm apply-btn')]"
    _verify_filter = "//span[contains(@class,'soft-text')][contains(text(), 'filter:')]"
    _close_dashboard_popup = "//div[@id='dashboard-announcement_dialog']/a[@class='dialog-close-btn cb-dialog-b smf-icon']"
    _edit_respondant = "//div[contains(@class,'respondents clearfix slideable')]//div[2]//div[1]//div[1]//div[1]//a[contains(text(), 'Edit')]"
    _delete_respondant = "//div[contains(@class,'respondents clearfix slideable')]//div[2]//div[1]//div[1]//div[1]//a[contains(text(), 'Delete')]"
    _export_respondant = "//div[contains(@class,'respondents clearfix slideable')]//div[2]//div[1]//div[1]//div[1]//a[contains(text(), 'Export')]"
    _delete_respondant_popup = "//h5[contains(text(),'Delete Respondent')]"
    _export_respondant_popup = "//h5[contains(text(),'Export Survey Data')]"
    _close_delete_popup = "//div[contains(@class,'dialog-btn-bar short-btn-bar clearfix')]//a[contains(@class,'wds-button wds-button--util wds-button--sm cancel-btn')][contains(text(),'CANCEL')]"
    _close_export_popup = "//div[contains(@class,'clearfix sm-corner-b')]//a[contains(@class,'wds-button wds-button--util wds-button--sm cancel-btn')][contains(text(),'CANCEL')]"


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def sendUsername(self):
        self.sendKeys("ib_test_gold", locator=self._username)

    def sendPassword(self):
        self.sendKeys("ib_test_gold1234", locator=self._password)

    def clicklogIn(self):
        self.elementClick(self._login_button, locatorType="xpath")

    def verifyUser(self):
        self.elementClick(self._verify_user, locatorType="xpath")
        signOutText = self.getText(self._sign_out, locatorType="xpath")
        self.log.info("Sign out text : "+str(signOutText))
        str(signOutText).strip()
        if signOutText == 'Sign Out' :
            dashBoardPopup = self.isElementPresent(self._close_dashboard_popup, locatorType="xpath")
            if dashBoardPopup:
                self.log.info("Closing dashboard popup")
                self.elementClick(self._close_dashboard_popup, locatorType="xpath")
            return True
        else:
            return False

    def getRespondantCount(self):
        respndantCount = self.getElement(self._respondant_count, locatorType="xpath").get_attribute("value")
        self.log.info("Respondant Count : "+str(respndantCount))
        return respndantCount

    def goToFirstRespondant(self):
        self.elementClick(self._respondant, locatorType="xpath")
        respondantCount = self.getRespondantCount()
        self.elementClick(self._respondant, locatorType="xpath")
        for x in range(int(respondantCount)):
            self.log.info("in for loop")
            self.elementClick(self._previous_respondant, locatorType="xpath")


    def verifyOnFirstRespondant(self):
        self.goToFirstRespondant()
        self.elementClick(self._respondant, locatorType="xpath")
        firstRespondant = self.getElement(self._first_respondant, locatorType="xpath").get_attribute("value")
        if int(firstRespondant) == 1:
            self.elementClick(self._respondant, locatorType="xpath")
            return True
        else:
            self.elementClick(self._respondant, locatorType="xpath")
            return False



    def addFilter(self):
        self.elementClick(self._filter, locatorType="xpath")
        self.elementClick(self._filter_by_question, locatorType="xpath")
        self.elementClick(self._select_question_filter, locatorType="xpath")
        self.elementClick(self._select_question_option, locatorType="xpath")
        self.elementClick(self._select_answer, locatorType="xpath")
        self.elementClick(self._apply_filter, locatorType="xpath")

    def verifyFilter(self):
        self.addFilter()
        time.sleep(5)
        return self.isElementPresent(self._verify_filter, locatorType="xpath")

    def verifyEditRespondant(self):
        self.elementClick(self._edit_respondant, locatorType="xpath")
        windowHandler = self.driver.window_handles
        self.driver.switch_to.window(windowHandler[1])
        self.log.info("Title name of new browser: "+self.driver.title)
        if self.driver.title == "Test Analyze Survey" :
            self.log.info("EXPORT IF : "+str(self.driver.title))
            #self.driver.close()
            return True


    def verifyDeleteRespondant(self):
        self.elementClick(self._delete_respondant, locatorType="xpath")
        result = self.isElementPresent(self._delete_respondant_popup, locatorType="xpath")
        self.elementClick(self._close_delete_popup, locatorType="xpath")
        return result

    def verifyExportRespondant(self):
        self.elementClick(self._export_respondant, locatorType="xpath")
        result = self.isElementPresent(self._export_respondant_popup, locatorType="xpath")
        self.elementClick(self._close_export_popup, locatorType="xpath")
        return result