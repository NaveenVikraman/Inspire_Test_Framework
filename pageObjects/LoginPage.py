import time

from selenium import webdriver
from utilities.readData import ReadData


class LoginPage:
    locator_data = ReadData().read_locator_json_data()['login_page']

    def __init__(self, driver):
        self.driver = driver

    def click_sign_in(self):
        """
                  click_sign_in(): To click sign_in button  and to click the signing by email button
                  :return: ret,err
        """
        try:
            self.driver.find_element("id", self.locator_data['link_sign_in_pop_up_id']).click()
            self.driver.find_element("xpath", self.locator_data['link_sign_in_with_email_xpath']).click()
            return 0, ""
        except Exception as e:
            return -1, str(e)

    def set_username(self, username):
        """
                 set_username(): To set username in username field
                 :return: ret,err
        """
        try:
            if len(username) > 0 and username != " ":
                self.driver.find_element("id", self.locator_data['textbox_username_id']).clear()
                self.driver.find_element("id", self.locator_data['textbox_username_id']).send_keys(username)
                return 0, ""
            else:
                return -1, "Username Length is short"
        except Exception as e:
            return -1, str(e)

    def set_password(self, password):
        """
                 set_password(): To set password in password field
                 :return: ret,err
        """
        try:
            if len(password) > 0 and password != " ":
                self.driver.find_element("id", self.locator_data['textbox_password_id']).clear()
                self.driver.find_element("id", self.locator_data['textbox_password_id']).send_keys(password)
                return 0, ""
            else:
                return -1, "Password Length is short"

        except Exception as e:
            return -1, str(e)

    def click_login(self):
        """
                 click_login(): To click login button
                 :return: ret,err
        """
        try:
            self.driver.find_element("id", self.locator_data['button_login_id']).click()
            time.sleep(2)
            return 0, ""
        except Exception as e:
            return -1, str(e)

    def verify_login(self):
        """
                 verify_login(): To Verify the login is successful or not by checking on login-error section
                 :return: ret,err
        """
        try:
            login_failure = self.driver.find_element("id", self.locator_data['div_login_error_id']).text
            return -1, login_failure
        except:
            return 0, ''
