from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.CartsPage import CartsPage



class Buying__Item__Page:

    miniValue = (By.XPATH, "//span/form/input[@id='low-price']")
    maxValue = (By.XPATH, "//span/form/input[@id='high-price']")
    go_button = (By.XPATH, "//span/span/input[@type='submit']")
    contents_locator = "//div[@class='a-section a-spacing-small puis-padding-left-small puis-padding-right-small']"
    items_list = (By.XPATH, contents_locator)
    filter_icon = (By.XPATH, "//span[@id='aod-filter-string']")
    option_New = (By.XPATH, "//div[@id='new']/div/label/i")
    laptop_pic = (By.XPATH, "//div[@id='pinned-image-id']")
    third_segment = (By.XPATH, "//div/div[@id='aod-offer'][3]")
    seventh_segment = (By.XPATH, "//div/div[@id='aod-offer'][7]")
    selected_laptop = (By.XPATH, "//span[@id='a-autoid-2-offer-5']//input[@name='submit.addToCart']")
    closed_button = (By.XPATH, "//div[@id='aod-close']/span")
    numb_ofItemsInCart = (By.XPATH, "//div/span[@id='nav-cart-count']")
    need_help_section = (By.XPATH, "//span[text()='Need help?']")
    next_page_button = (By.XPATH, "//a[contains(@href, 'pg_1')]")
    iphone_list = (By.XPATH, "//h2[@class='a-size-mini a-spacing-none a-color-base s-line-clamp-4']/a")
    addToCartButton = (By.XPATH, "//span/input[@id='add-to-cart-button']")
    option_cart = (By.XPATH, "//span[@id='attach-sidesheet-view-cart-button']")
    option2 = (By.XPATH, "//span/a[@href='/cart?ref_=sw_gtc']")

    def __init__(self, driver):
        self.driver = driver

    def add_miniValue(self):
        return self.driver.find_element(*Buying__Item__Page.miniValue)

    def add_maxValue(self):
        return self.driver.find_element(*Buying__Item__Page.maxValue)

    def click_goButton(self):
        return self.driver.find_element(*Buying__Item__Page.go_button)

    def items_found(self):
        # this returns a list of all items found in the page once that price range is inputted
        return self.driver.find_elements(*Buying__Item__Page.items_list)

    def click_filter_icon(self):
        return self.driver.find_element(*Buying__Item__Page.filter_icon)

    def option_New_Checkbox(self):
        return self.driver.find_element(*Buying__Item__Page.option_New)

    def laptop_pic_element(self):
        return self.driver.find_element(*Buying__Item__Page.laptop_pic)

    def third_option(self):
        return self.driver.find_element(*Buying__Item__Page.third_segment)

    def seventh_option(self):
        return self.driver.find_element(*Buying__Item__Page.seventh_segment)

    def click_selected_laptop(self):
        return self.driver.find_element(*Buying__Item__Page.selected_laptop)

    def click_close_button(self):
        return self.driver.find_element(*Buying__Item__Page.closed_button)

    def click_cartIcon(self):
        # clicks on the cart number on the cart icon so that we can land in the cart page
        self.driver.find_element(*Buying__Item__Page.numb_ofItemsInCart).click()
        cartItemPage = CartsPage(self.driver)
        return cartItemPage

    def scroll_to_needHelp(self):
        return self.driver.find_element(*Buying__Item__Page.need_help_section)

    def click_nextPage(self):
        return self.driver.find_element(*Buying__Item__Page.next_page_button)

    def list_of_Iphone(self):
        return self.driver.find_elements(*Buying__Item__Page.iphone_list)

    def click_on_add_to_cart(self):
        return self.driver.find_element(*Buying__Item__Page.addToCartButton)

    def select_cartIcon(self):
        return self.driver.find_element(*Buying__Item__Page.option_cart)

    def select_option2(self):
        return self.driver.find_element(*Buying__Item__Page.option2)