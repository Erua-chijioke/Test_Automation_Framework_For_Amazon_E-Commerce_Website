from selenium.webdriver.common.by import By


class settings:

    language_name = (By.XPATH, "//*[@id='icp-language-settings']/div[2]/div/label/span/span")
    languages = (By.XPATH, "//label/span")
    currency_button = (By.XPATH, "//span/span[@data-csa-c-type='widget']")
    currency_selected = (By.XPATH, "//*[@id='icp-currency-dropdown_54']/span")
    save_button = (By.XPATH, "//*[@id='icp-save-button']/span/input")

    def __init__(self, driver):
        self.driver = driver

    def select_language(self):
        return self.driver.find_element(*settings.language_name)

    def language_list(self):
        return self.driver.find_elements(*settings.languages)

    def click_currency_button(self):
        return self.driver.find_element(*settings.currency_button)

    def select_currency(self):
        return self.driver.find_element(*settings.currency_selected)

    def click_save_button(self):
        return self.driver.find_element(*settings.save_button)

