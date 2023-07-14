import time

from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.HomePage import Home__Page
from pageObjects.BuyingItemPage import Buying__Item__Page
from pageObjects.CartsPage import CartsPage
from pageObjects.SettingsPage import settings
from pageObjects.SignInPage import SignInPage
from tests.crop_out_image import selectImageSection
from utilities.BaseClass import BaseClass


# we called the parent class into the child class thus. see inside the parenthesis below
# the parent class called BaseClass with its properties will be inherited by the child class (TestOne) below
# the fixtures defined in BaseClass.py file will also be inherited by this child class
class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        # creating the driver object, which represents the driver u want to associate with the HomePage
        driver = self.driver
        # creating an instance of 'HomePage' by passing the 'driver' object as an argument to the constructor
        home_page = Home__Page(driver)
        # calling the method change_currency which will return object of your next class
        setttings = home_page.change_currency()
        log.info("clicked on the flag icon on the top navigation bar of the Homepage")
        # we will do the same for others as follows

        # setttings = setttings(self.driver)
        language = setttings.select_language().text
        log.info("Extracted default Language is " + language)
        # print("The selected Language in the site is ", language)

        if language != "English - EN":
            LANGUAGES = setttings.language_list()
            for language in LANGUAGES:
                if language.text == "English - EN":
                    language.click()

        # clicking on currency button
        setttings.click_currency_button().click()
        log.info("Clicked on the default selected currency")

        time.sleep(3)
        action = ActionChains(self.driver)
        currency = setttings.select_currency()
        action.scroll_to_element(currency)
        log.info("Scrolled down to Nigerian Naira")
        action.click(currency).perform()
        log.info("Selected Nigeria Naira as the Default Currency")

        # clicking the save button on the setttings page
        setttings.click_save_button().click()
        log.info("Clicked the Save Changes Button")

        time.sleep(5)

        # moved to homepage again
        action.move_to_element(home_page.hover_over_signin())
        log.info("Moved the cursor to the 'Hello Sign In... button' and hovers over it")
        action.perform()

        # sign in page
        # We first call the method that returns the object to use for the signin page
        sign_in = home_page.click_signin()
        log.info("Clicked on the 'Hello Sign In... button'")
        sign_in.input_username().send_keys("PUT YOUR EMAIL ADDRESS HERE")  # put ur amazon username here
        log.info("Entered the Email Address")
        sign_in.click_continue_button().click()
        log.info("Clicked on the Continue Button")
        sign_in.input_password().send_keys("PUT THE PASSWORD HERE")  # put ur amazon password here
        # check whether u can put the username and password as txt file somewhere else
        log.info("Entered the Password")
        sign_in.submit_button().click()
        log.info("Clicked the Sign In Button")

        # check whether cart is empty
        numb_of_itemsInCart = home_page.check_numberOfCartItems().text
        log.info("Extracted the number of items in the cart")
        if numb_of_itemsInCart != "0":
            log.error("Number of items in cart is not equal to zero")
        assert numb_of_itemsInCart == "0"
        log.info("Checked whether the number of items in the cart is '0'")

        # shopping actually starts here
        # clicking on hamburger menu
        home_page.click_hamburgerMenu().click()
        log.info("Clicked the Hamburger menu on the top LHS")
        time.sleep(6)

        # wait = WebDriverWait(driver, 10)
        # target = driver.find_elements(By.XPATH, "//div[@id='hmenu-content']/ul/li/a/i")
        # wait.until(EC.visibility_of_all_elements_located(target))

        # clicking computer section  and computersTablets on hamburger menu
        home_page.click_computerButton().click()
        log.info("Clicked on 'Computer'")
        time.sleep(4)
        # home_page.click_computersTablets().click()

        # Test cases§
        # login and check whether cart is empty
        # Add item to cart and delete it and assert that the item is deleted
        # After buying you sign out

        # adding the price range
        items_buying = home_page.click_computersTablets()
        log.info("Clicked on Computers & Tablets")
        items_buying.add_miniValue().send_keys(20000)
        log.info("Entered the minimum price range")
        items_buying.add_maxValue().send_keys(1000000)
        log.info("Entered the maximum price range")
        time.sleep(2)
        items_buying.click_goButton().click()
        log.info("Clicked on Go Button")
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.visibility_of_all_elements_located((By.XPATH, items_buying.contents_locator)))
        # we called the variable contents_locator from BuyingItemsPage as seen above

        items = items_buying.items_found()
        log.info("The length of items found in the page once that price range is inputted is {}".format(len(items)))
        # print(len(items))

        names_of_item = []

        for item in items:
            name = item.find_element(By.XPATH, "div[1]/h2").text
            # we used chaining above to chain two XPATHS together. the second part of the XPATH
            # is called from the BuyingItemsPage as seen inside the parenthesis above
            # print(name)
            names_of_item.append(name)
        # print(names_of_item)
        search = 'SAMSUNG Galaxy Tab A7 Lite 8.7'

        for i in names_of_item:
            if search in i:
                log.info(i)
                # print(i)

        for item in items:
            name = item.find_element(By.XPATH, "div[1]/h2").text
            if search in name:
                item.find_element(By.XPATH, "div[5]/div/span/a").click()

        log.info("Clicked on the number of SAMSUNG Galaxy in stock")
        # wait1 = WebDriverWait(driver, 30)
        # wait1.until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@id='aod-offer-list']/div")))

        # clicks on 'filter' icon
        items_buying.click_filter_icon().click()
        log.info("Clicked on the filter button")

        # checks whether the option 'New' is present in the filter and selects it
        new_option = items_buying.option_New_Checkbox()
        new_option.is_displayed()
        log.info("The New Option is displayed ")

        new_option.click()    # clicks on 'new' checkbox
        log.info("Clicked on the 'New' checkbox")
        time.sleep(3)

        # target3 = self.driver.find_element(By.XPATH, "//div[@id='pinned-image-id']")

        # moves cursor to the laptop image
        action.move_to_element(items_buying.laptop_pic_element())
        log.info("Moved to the SAMSUNG Galaxy picture")
        time.sleep(5)

        # scrolls to the 3rd and 7th segment of the page
        action.scroll_to_element(items_buying.third_option())
        log.info("Scrolled down to the third option")
        action.scroll_to_element(items_buying.seventh_option())
        log.info("Scrolled down to the seventh option")
        time.sleep(4)
        action.perform()

        # clicks on the selected laptop option
        items_buying.click_selected_laptop().click()
        log.info("Clicked on the selected SAMSUNG Galaxy option")
        time.sleep(4)

        # clicks on the close button
        items_buying.click_close_button().click()
        log.info("Clicked on the 'close' button represented by 'X'")

        # we call the method which returns the object of the class for the CartsPage
        cartItem_page = items_buying.click_cartIcon()
        log.info("Clicked on the 'cart icon' on the navigation bar")

        time.sleep(3)
        # return to buy more items: first click on the "All" option to put in the search filters
        cartItem_page.click_on_allOption().click()
        log.info("Clicked on the 'All Departments option' on the nav bar")

        # we check options inside the filter options.
        # Note how we called the fxn that returns the list of filter options
        for option in cartItem_page.filter_options():
            if option.text == "Electronics":
                time.sleep(2)
                option.click()
                log.info("Clicked on the 'Electronics' option from the drop down")

        # fills the search box with the item name
        cartItem_page.fillIn_searchBox().send_keys("apple iphone")
        log.info("Filled the search box with 'apple iphone'")
        # calling the method from CartsPage that returns object of the class in BuyingItemPage
        cartItem_page.click_searchIcon()
        log.info("Clicked on the search icon")

        # scrolls to need help section on the lower section of the page and then clicks the next page button
        action.scroll_to_element(items_buying.scroll_to_needHelp()).perform()
        log.info("Scrolled down to the 'Next page link' on the lower section of the page")
        time.sleep(5)
        items_buying.click_nextPage().click()
        log.info("Clicked on the 'Next page link'")
        time.sleep(5)

        # checks the length of the list of Iphones that came out after the nextPage is clicked
        log.info("The number of iphone elements on this page is {}".format(len(items_buying.list_of_Iphone())))
        # print(len(items_buying.list_of_Iphone()))

        # clicks on the third item on that list
        items_buying.list_of_Iphone()[3].click()
        log.info("Clicked on the 3rd item on that list")
        # iphone_list[3].click()

        time.sleep(2)
        # click on add to cart button
        items_buying.click_on_add_to_cart().click()
        log.info("Clicked on the 'add to cart' button")

        try:
            # click the first cart web element
            # x = self.driver.find_element(By.XPATH, "//span[@id='attach-sidesheet-view-cart-button']")
            # x.click()
            items_buying.select_cartIcon().click()
            log.info("Clicked on the first appeared web element")
        except NoSuchElementException:
            # y = self.driver.find_element(By.XPATH, "//span/a[@href='/cart?ref_=sw_gtc']")
            # if the first element is not found, locate and click the one below
            # y.click()
            # if the first element is not found, locate and click the one below
            items_buying.select_option2().click()
            log.info("Clicked on the second appeared web element")

        cartItem_page.click_proceedCheckOut()
        log.info("Clicked on Proceed to checkout")

        # get the full screenshot of the page
        driver.get_screenshot_as_file("screenshot.png")
        log.info("Captured the Checkoutpage")

        # we call the function to crop out the section of image we need
        selectImageSection()





