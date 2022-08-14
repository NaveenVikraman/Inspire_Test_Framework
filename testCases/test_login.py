import pdb
import time
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
import pytest
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.LoginPage import LoginPage
from pageObjects.postPage import PostPage
from utilities.readData import ReadData
from utilities.customLogger import LogGen
import time
import os


class TestLogin01:
    input_data = ReadData().read_input_json_data()
    logger = LogGen.logGen()

    def page_is_loading(self,driver):
        while True:
            x = self.driver.execute_script("return document.readyState")
            if x == "complete":
                return True
            else:
                yield False

    def test_signin(self, setup):
        self.logger.info("*************** Inside test_signin *****************")
        self.driver = setup
        self.driver.get(self.input_data['baseURL'])

        self.lp = LoginPage(self.driver)
        self.logger.info("*************** Logging In *****************")
        self.lp.click_sign_in()
        self.lp.set_username(self.input_data['username'])
        self.lp.set_password(self.input_data['password'])
        self.lp.click_login()
        time.sleep(2)
        self.logger.info("*************** Navigating to Profile *****************")
        self.profile = PostPage(self.driver)
        self.profile.click_profile()
        time.sleep(2)
        self.logger.info("*************** Creating a Post *****************")
        self.profile.create_post()

        time.sleep(2)
        self.logger.info("*************** Setting Journal Title *****************")
        self.profile.set_title(self.input_data['journal_title'])

        self.logger.info("*************** Setting Journal Description *****************")
        self.profile.set_description(self.input_data['journal_description'])

        self.logger.info("*************** Setting Privacy *****************")
        self.profile.set_privacy()

        self.logger.info("*************** Publishing Post*****************")
        self.profile.publish_post()
        time.sleep(2)
        self.driver.get(self.input_data['baseURL'])
        time.sleep(2)
        self.logger.info("*************** Verifying Post*****************")
        page_src = self.driver.page_source

        if self.input_data['journal_title'] in page_src:
            assert True
            self.logger.info("*************** Post(Journal) Verification Successful *****************")
        else:
            self.logger.error("*************** Post(Journal) Verification Failed *****************")
            self.driver.save_screenshot(self.input_data['screenshot_url'] + "test_post_verification.png")
            self.driver.close()
            assert False
        self.driver.close()



