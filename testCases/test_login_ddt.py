import time
import pytest
import openpyxl
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pageObjects.LoginPage import LoginPage
from utillities.readProperties import ReadConfig
from utillities.customLogger import LogGen
from utillities import XLUtils


class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData//LoginData.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_Login_ddt(self, setup):
        self.logger.info("**********Test_002_DDT_Login**********")
        self.logger.info("**********Login test is Started**********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("Number of Rows in a Excel:", self.rows)
        lst_status = []  # Empty list Variable

        for r in range(2, self.rows+1):
            self.username = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("*****Passed****")
                    self.lp.clickLogout();
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("*****Failed****")
                    self.lp.clickLogout();
                    lst_status.append("Fail")
            elif act_title != "Pass":
                if self.exp == "Pass":
                    self.logger.info("*****Failed****")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("*****Passed****")
                    lst_status.append("Pass")
        if "Fail " not in lst_status:
            self.logger.info("*****Login DDT test Pass*****")
            self.driver.close()
            assert True
        else:
            self.logger.info("*****Login DDT test Failed*****")
            self.driver.close()
            assert False

        self.logger.info("*****End of Login DDT TEST*****")
        self.logger.info("*****Complete TC_LoginDDT_002 TEST*****");

