import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pageObjects.LoginPage import LoginPage
from utillities.readProperties import ReadConfig
from utillities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("**********Test_001_Login**********")
        self.logger.info("**********Verify Home Page Title**********")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("**********Home Page Title test is Passed**********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle1.png")
            self.driver.close()
            self.logger.error("**********Home Page Title test is Failed**********")
            assert False

    @pytest.mark.regression
    def test_Login(self, setup):
        self.logger.info("**********Login test is Started**********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("**********Login test is Passed**********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Login1.png")
            self.driver.close()
            self.logger.error("**********Login test is Failed**********")
            assert False