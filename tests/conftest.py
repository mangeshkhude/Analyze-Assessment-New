from util.chrome_driver import ChromeDriver
import util.custom_logger as cl
import logging
import pytest

@pytest.yield_fixture(scope="class")
def getDriver():
    log = cl.customLogger(logging.DEBUG)
    log.info("=" * 50)
    log.info("Get Driver")
    driver = ChromeDriver.getFromChrome(ChromeDriver)
    yield driver
    driver.close()