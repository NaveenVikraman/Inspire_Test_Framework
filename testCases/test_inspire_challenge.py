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
from pageObjects.HomePage import HomePage
from utilities.readData import ReadData
from utilities.customLogger import LogGen
import time
import os


class TestLogin01:
    input_data = ReadData().read_input_json_data()
    logger,base_log_dir = LogGen.logGen()
    input_data['screenshot_url'] =  LogGen.screenshotGen(base_log_dir)

    def test_signin(self, setup):
        '''
        STEPS:

        1. LOADING THE DRIVER
        2. LOGIN & VERIFY LOGIN
        3. NAVIGATE TO PROFILE
        4. CREATE POST
        5. VERIFY POST

        Author: Naveen V
        '''

        # LOADING THE DRIVER SECTION
        self.logger.info("*************** STEP1: LOADING THE DRIVER *****************")
        self.driver = setup
        self.driver.get(self.input_data['baseURL'])

        self.lp = LoginPage(self.driver)

        # LOGIN SECTION
        self.logger.info("*************** STEP2: LOGIN WITH EMAIL & PASSWORD *****************")
        ret, err = self.lp.click_sign_in()
        if ret == -1:
            self.logger.error("*************** Login  Failed *****************" + str(err))
            self.driver.save_screenshot(self.input_data['screenshot_url'] + "failed_click_signing.png")
            self.driver.close()
            assert False
        ret, err = self.lp.set_username(self.input_data['email'])
        if ret == -1:
            self.logger.error("*************** Login  Failed *****************" + str(err))
            self.driver.save_screenshot(self.input_data['screenshot_url'] + "failed_setting_username.png")
            self.driver.close()
            assert False
        ret, err = self.lp.set_password(self.input_data['password'])
        if ret == -1:
            self.logger.error("*************** Login  Failed *****************" + str(err))
            self.driver.save_screenshot(self.input_data['screenshot_url'] + "failed_setting_password.png")
            self.driver.close()
            assert False
        ret, err = self.lp.click_login()
        if ret == -1:
            self.logger.error("*************** Login  Failed *****************" + str(err))
            self.driver.save_screenshot(self.input_data['screenshot_url'] + "failed_during_login.png")
            self.driver.close()
            assert False
        self.logger.info("*************** Verifying Login *****************")
        ret, err = self.lp.verify_login()
        if ret == -1:
            self.logger.error("*************** LOGIN FAILED *****************" + str(err))
            self.driver.save_screenshot(self.input_data['screenshot_url'] + "login_failed.png")
            self.driver.close()
            assert False
        self.logger.info("*************** LOGIN SUCCESSFUL *****************" + str(err))

        # NAVIGATE TO PROFILE SECTION
        self.logger.info("*************** STEP3: NAVIGATE TO PROFILE *****************")
        self.profile = PostPage(self.driver)
        ret, err = self.profile.click_profile()
        if ret == -1:
            self.logger.error("*************** Navigating to Profile Failed *****************" + str(err))
            self.driver.save_screenshot(self.input_data['screenshot_url'] + "navigating_profile_failed.png")
            self.driver.close()
            assert False

        self.logger.info("*************** NAVIGATE TO PROFILE SUCCESSFUL *****************" + str(err))
        # CREATE A POST SECTION
        self.logger.info("*************** STEP4: CREATE A POST *****************")
        ret, err = self.profile.create_post()
        if ret == -1:
            self.logger.error("*************** Creating Post Failed  *****************" + str(err))
            self.driver.save_screenshot(self.input_data['screenshot_url'] + "click_create_post_failed.png")
            self.driver.close()
            assert False

        self.logger.info("*************** Setting Journal Title *****************")
        ret, err = self.profile.set_title(self.input_data['journal_title'])
        if ret == -1:
            self.logger.error("***************  Setting Journal Title Failed  *****************" + str(err))
            self.driver.save_screenshot(self.input_data['screenshot_url'] + "setting_journal_tile_failed.png")
            self.driver.close()
            assert False
        self.logger.info("*************** Setting Journal Description *****************")
        ret, err = self.profile.set_description(self.input_data['journal_description'])
        if ret == -1:
            self.logger.error("***************  Setting Journal Description Failed  *****************" + str(err))
            self.driver.save_screenshot(self.input_data['screenshot_url'] + "setting_journal_description_failed.png")
            self.driver.close()
            assert False
        self.logger.info("*************** Setting Privacy *****************")
        ret, err = self.profile.set_privacy()
        if ret == -1:
            self.logger.error("***************  Setting Privacy Failed  *****************" + str(err))
            self.driver.save_screenshot(self.input_data['screenshot_url'] + "setting_privacy_failed.png")
            self.driver.close()
            assert False
        self.logger.info("*************** Publishing Post*****************")
        ret, err = self.profile.publish_post()
        if ret == -1:
            self.logger.error("***************  Publishing Post Failed  *****************" + str(err))
            self.driver.save_screenshot(self.input_data['screenshot_url'] + "publishing_post_failed.png")
            self.driver.close()
            assert False
        self.logger.info("*************** POST CREATION SUCCESSFUL *****************" + str(err))

        # VERIFICATION OF POST SECTION
        self.logger.info("*************** STEP5: VERIFY POST *****************")

        self.driver.get(self.input_data['baseURL'])
        self.hp = HomePage(self.driver)
        time.sleep(2)
        self.logger.info("*************** Sort by Latest Post *****************")
        ret, err = self.hp.click_sort_new_post()
        if ret == -1:
            self.logger.error("***************  Sort by Latest Post Failed  *****************" + str(err))
            self.driver.save_screenshot(self.input_data['screenshot_url'] + "sort_by_new_failed.png")
            self.driver.close()
            assert False
        self.logger.info("*************** Verifying the post data *****************")
        ret, err = self.hp.traverse_post(self.input_data['username'], self.input_data['journal_title'],
                                         self.input_data['journal_description'])
        if ret == -1:
            self.logger.error("*************** Verification of Post Failed *****************" + str(err))
            self.driver.save_screenshot(self.input_data['screenshot_url'] + "verify_post_failed.png")
            self.driver.close()
            assert False
        self.logger.info("*************** POST VERIFICATION SUCCESSFUL *****************" + str(err))

        self.driver.close()
