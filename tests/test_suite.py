# Combining Test Suites - unittest

#  ----------------- Unit test framework
import unittest

#  ----------------  Individual test suites
from tests.test_login_and_land_on_analyze import LoginAndLandOnAnalyze
# -----------------  Load all the test cases
suiteList = []
suiteList.append(unittest.TestLoader().loadTestsFromTestCase(LoginAndLandOnAnalyze))

# ----------------   Join them together ane run them
comboSuite = unittest.TestSuite(suiteList)
unittest.TextTestRunner(verbosity=3).run(comboSuite)