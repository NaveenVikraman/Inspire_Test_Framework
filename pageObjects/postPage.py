import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class PostPage:
    img_profile_id = 'avatarImage'
    link_goto_profile_id = 'goToProfile'
    button_create_post_xpath = '/html/body/app-root/app-profile/div[2]/aside[1]/app-profile-info/div/div[4]/button[1]'
    section_journal_select_id = 'journal_select'
    textbox_title_xpath = '//*[@id="journal-post-title-textbox"]'
    textbox_description_xpath = '//*[@id="editor"]/div[2]/div[2]/div'
    dropdown_privacy_id = 'dropdown_wrapper'
    div_privacy_friends_xpath = '/html/body/app-root/app-profile/div[2]/main/div/app-create-post/app-post-form-wrapper/app-journal-post-form/div/form/div[4]/ins-custom-dropdown/div/div[2]/div[4]'
    button_publish_post_id = 'publish-post-button'

    def __init__(self, driver):
        self.driver = driver

    def click_profile(self):
        WebDriverWait(self.driver, 60).until(
            expected_conditions.presence_of_element_located((By.ID, self.img_profile_id)))
        self.driver.find_element("id", self.img_profile_id).click()
        time.sleep(1)
        WebDriverWait(self.driver, 60).until(
            expected_conditions.presence_of_element_located((By.ID, self.link_goto_profile_id)))
        self.driver.find_element("id", self.link_goto_profile_id).click()
        time.sleep(1)

    def create_post(self):
        self.driver.find_element("xpath", self.button_create_post_xpath).click()
        time.sleep(1)
        self.driver.find_element("id", self.section_journal_select_id).click()

    def set_title(self,title):
        self.driver.find_element("xpath", self.textbox_title_xpath).send_keys(title)

    def set_description(self,description):
        self.driver.find_element("xpath", self.textbox_description_xpath).send_keys(description)

    def set_privacy(self):
        privacy_dropdown =  self.driver.find_element("id", self.dropdown_privacy_id)
        self.driver.execute_script('arguments[0].click()', privacy_dropdown)
        privacy_friends = self.driver.find_element("xpath", self.div_privacy_friends_xpath)
        self.driver.execute_script('arguments[0].click()', privacy_friends)

    def publish_post(self):
        publish_button = self.driver.find_element("id", self.button_publish_post_id)
        self.driver.execute_script('arguments[0].click()', publish_button)



