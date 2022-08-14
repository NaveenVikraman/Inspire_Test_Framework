import time

from selenium import webdriver
from utilities.readData import ReadData


class LoginPage:
    locator_data = ReadData().read_locator_json_data()['login_page']

    def __init__(self, driver):
        self.driver = driver

    def click_sign_in(self):
        try:
            self.driver.find_element("id", self.locator_data['link_sign_in_pop_up_id']).click()
            self.driver.find_element("xpath", self.locator_data['link_sign_in_with_email_xpath']).click()
            return 0, ""
        except Exception as e:
            return -1, str(e)

    def set_username(self, username):
        try:
            self.driver.find_element("id", self.locator_data['textbox_username_id']).clear()
            self.driver.find_element("id", self.locator_data['textbox_username_id']).send_keys(username)
            return 0, ""
        except Exception as e:
            return -1, str(e)

    def set_password(self, password):
        try:
            self.driver.find_element("id", self.locator_data['textbox_password_id']).clear()
            self.driver.find_element("id", self.locator_data['textbox_password_id']).send_keys(password)
            return 0, ""
        except Exception as e:
            return -1, str(e)

    def click_login(self):
        try:
            self.driver.find_element("id", self.locator_data['button_login_id']).click()
            time.sleep(2)
            return 0, ""
        except Exception as e:
            return -1, str(e)

    def verify_login(self):
        try:
            login_failure = self.driver.find_element("id", self.locator_data['div_login_error_id']).text
            return -1, login_failure
        except:
            return 0, ''
