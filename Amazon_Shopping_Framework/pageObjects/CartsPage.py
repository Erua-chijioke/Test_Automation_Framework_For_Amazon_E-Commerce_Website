from selenium.webdriver.common.by import By


from pageObjects.CheckOutPage import checkOutPage


class CartsPage:

    filterOptions = (By.XPATH, "//div[@id='nav-search-dropdown-card']/div")
    deeperFilter = (By.XPATH, "//select[@title='Search in']/option")
    search_box = (By.XPATH, "//input[@id='twotabsearchtextbox']")
    search_icon = (By.XPATH, "//span[@aria-label='Go']")
    proceedCheckoutButton = (By.XPATH, "//input[@name='proceedToRetailCheckout']")

    def __init__(self, driver):
        self.driver = driver

    def click_on_allOption(self):
        return self.driver.find_element(*CartsPage.filterOptions)

    def filter_options(self):
        return self.driver.find_elements(*CartsPage.deeperFilter)

    def fillIn_searchBox(self):
        return self.driver.find_element(*CartsPage.search_box)

    def click_searchIcon(self):
        from pageObjects.BuyingItemPage import Buying__Item__Page
        self.driver.find_element(*CartsPage.search_icon).click()
        items_buying = Buying__Item__Page(self.driver)
        return items_buying


    def click_proceedCheckOut(self):
        self.driver.find_element(*CartsPage.proceedCheckoutButton).click()
        checkoutpage = checkOutPage(self.driver)
        return checkoutpage