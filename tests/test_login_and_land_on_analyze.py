
import unittest
import pytest
import util.custom_logger as cl
import logging
from pages.login_page import Login

@pytest.mark.usefixtures("getDriver")
class LoginAndLandOnAnalyze(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, getDriver):
        log = cl.customLogger(logging.DEBUG)
        log.info("=" * 50)
        log.info("Login Operation")
        self.lp = Login(getDriver)

    def test_T1login_and_land_analyze(self):
        self.lp.sendUsername()
        self.lp.sendPassword()
        self.lp.clicklogIn()
        assert self.lp.verifyUser()

    def test_T2go_to_first_respondant(self):
        assert self.lp.verifyOnFirstRespondant()

    def test_T3verify_filter(self):
        assert self.lp.verifyFilter()

    def test_T4verify_delete_respondant(self):
        assert self.lp.verifyDeleteRespondant()

    def test_T5verify_export_respondant(self):
        assert self.lp.verifyExportRespondant()

    def test_T6verify_edit_respondant(self):
        assert self.lp.verifyEditRespondant()