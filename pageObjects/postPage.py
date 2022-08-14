import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utilities.readData import ReadData


class PostPage:
    locator_data = ReadData().read_locator_json_data()['post_page']

    def __init__(self, driver):
        self.driver = driver

    def click_profile(self):
        try:
            WebDriverWait(self.driver, 60).until(
                expected_conditions.presence_of_element_located((By.ID, self.locator_data['img_profile_id'])))
            self.driver.find_element("id", self.locator_data['img_profile_id']).click()
            time.sleep(1)
            WebDriverWait(self.driver, 60).until(
                expected_conditions.presence_of_element_located((By.ID, self.locator_data['link_goto_profile_id'])))
            self.driver.find_element("id", self.locator_data['link_goto_profile_id']).click()
            time.sleep(2)
            return 0, ""

        except Exception as e:
            return -1, str(e)

    def create_post(self):
        try:
            self.driver.find_element("xpath", self.locator_data['button_create_post_xpath']).click()
            time.sleep(2)
            self.driver.find_element("id", self.locator_data['section_journal_select_id']).click()
            time.sleep(2)
            return 0, ""
        except Exception as e:
            return -1, str(e)

    def set_title(self, title):
        try:
            self.driver.find_element("xpath", self.locator_data['textbox_title_xpath']).send_keys(title)
            return 0, ""
        except Exception as e:
            return -1, str(e)

    def set_description(self, description):
        try:
            self.driver.find_element("xpath", self.locator_data['textbox_description_xpath']).send_keys(description)
            return 0, ""
        except Exception as e:
            return -1, str(e)

    def set_privacy(self):
        try:
            privacy_dropdown = self.driver.find_element("id", self.locator_data['dropdown_privacy_id'])
            self.driver.execute_script('arguments[0].click()', privacy_dropdown)
            privacy_friends = self.driver.find_element("xpath", self.locator_data['div_privacy_friends_xpath'])
            self.driver.execute_script('arguments[0].click()', privacy_friends)
            return 0, ""
        except Exception as e:
            return -1, str(e)

    def publish_post(self):
        try:
            publish_button = self.driver.find_element("id", self.locator_data['button_publish_post_id'])
            self.driver.execute_script('arguments[0].click()', publish_button)
            time.sleep(2)
            return 0, ""
        except Exception as e:
            return -1, str(e)
