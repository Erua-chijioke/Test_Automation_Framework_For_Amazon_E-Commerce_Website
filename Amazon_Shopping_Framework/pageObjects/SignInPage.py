from selenium.webdriver.common.by import By


class SignInPage:

    username = (By.CSS_SELECTOR, "div input[type='email']")
    continue_button = (By.CSS_SELECTOR, "span input[id='continue']")
    password = (By.CSS_SELECTOR, "div input[type='password']")
    login_button = (By.CSS_SELECTOR, "span input[id='signInSubmit']")

    def __init__(self, driver):
        self.driver = driver

    def input_username(self):
        return self.driver.find_element(*SignInPage.username)

    def click_continue_button(self):
        return self.driver.find_element(*SignInPage.continue_button)

    def input_password(self):
        return self.driver.find_element(*SignInPage.password)

    def submit_button(self):
        return self.driver.find_element(*SignInPage.login_button)
