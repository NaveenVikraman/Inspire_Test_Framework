import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities.readData import ReadData


class HomePage:
    locator_data = ReadData().read_locator_json_data()['home_page']

    def __init__(self, driver):
        self.driver = driver

    def click_sort_new_post(self):
        """
                 click_sort_new_post(): To sort by latest posts by clicking new button
                 :return: ret,err
        """
        try:
            self.driver.find_element("id", self.locator_data['button_new_post_id']).click()
            time.sleep(2)
            return 0, ""
        except Exception as e:
            return -1, str(e)

    def traverse_post(self, username, title, description):
        """
               traverse_post(): To traverse through the posts to match the expected data and actual data
               :return: ret,err
        """
        try:
            elements = self.driver.find_elements("xpath", self.locator_data['section_post_elements_xpath'])
            check_matched = False
            index = 0
            for i in range(len(elements)):
                feed_data = elements[i].text
                if username in feed_data and title in feed_data:
                    if "Read more" in feed_data:
                        read_more = \
                            self.driver.find_elements("xpath",
                                                      self.locator_data['div_post_elements_description_xpath'])[
                                i - index]
                        self.driver.execute_script('arguments[0].click()', read_more)
                    if description in elements[i].text:
                        check_matched = True
                if "Read more" not in feed_data:
                    index += 1
            if check_matched:
                return 0, ""
            else:
                return -1, ""

        except Exception as e:
            return -1, str(e)
