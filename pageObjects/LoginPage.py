from selenium import webdriver


class LoginPage:
    link_sign_in_pop_up_id = "logIn"
    link_sign_in_with_email_xpath = '//*[@id="ins-modal-wrapper"]/div/app-login-modal-container/div/app-login/div/div/p/a[1]'
    textbox_username_id = "email"
    textbox_password_id = "pw"
    button_login_id = 'login_submit'


    def __init__(self, driver):
        self.driver = driver

    def click_sign_in(self):
        self.driver.find_element("id",self.link_sign_in_pop_up_id).click()
        self.driver.find_element("xpath", self.link_sign_in_with_email_xpath).click()

    def set_username(self, username):
        self.driver.find_element("id",self.textbox_username_id).clear()
        self.driver.find_element("id",self.textbox_username_id).send_keys(username)

    def set_password(self, password):
        self.driver.find_element("id",self.textbox_password_id).clear()
        self.driver.find_element("id",self.textbox_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element("id",self.button_login_id).click()



