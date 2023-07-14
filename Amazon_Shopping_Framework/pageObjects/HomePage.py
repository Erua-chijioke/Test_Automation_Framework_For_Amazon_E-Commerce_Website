from selenium.webdriver.common.by import By

from pageObjects.BuyingItemPage import Buying__Item__Page
from pageObjects.SettingsPage import settings
from pageObjects.SignInPage import SignInPage


class Home__Page:

    # location of the flag icon clicked on the Home page
    flag = (By.CSS_SELECTOR, ".icp-nav-link-inner")
    # location of signin section on the homepage
    signin_block = (By.XPATH, "//*[@id='nav-link-accountList']/div")
    signin_button = (By.XPATH, "//*[@id='nav-flyout-ya-signin']/a/span")
    no_of_cartItems = (By.CSS_SELECTOR, "a div span[id='nav-cart-count']")
    hamburger = (By.XPATH, "//div/a/i[@class='hm-icon nav-sprite']")
    computer_button = (By.XPATH, "//li/a/div[text()='Computers']")
    computersTablets = (By.XPATH, "//li/a[text()='Computers & Tablets']")

    def __init__(self, driver):
        self.driver = driver

    def change_currency(self):
        self.driver.find_element(*Home__Page.flag).click()
        Settings = settings(self.driver)
        return Settings

    def hover_over_signin(self):
        return self.driver.find_element(*Home__Page.signin_block)

    # clicks on the sign in button and returns the class object of the next page (SignInPage.py)
    def click_signin(self):
        self.driver.find_element(*Home__Page.signin_button).click()
        Sign_in = SignInPage(self.driver)
        return Sign_in

    def check_numberOfCartItems(self):
        return self.driver.find_element(*Home__Page.no_of_cartItems)

    def click_hamburgerMenu(self):
        return self.driver.find_element(*Home__Page.hamburger)

    def click_computerButton(self):
        return self.driver.find_element(*Home__Page.computer_button)

    # clicks on the Tablet&Tablet tab and returns the class object of the next page (BuyingItemPage.py)
    def click_computersTablets(self):
        self.driver.find_element(*Home__Page.computersTablets).click()
        itemsBuying = Buying__Item__Page(self.driver)
        return itemsBuying





