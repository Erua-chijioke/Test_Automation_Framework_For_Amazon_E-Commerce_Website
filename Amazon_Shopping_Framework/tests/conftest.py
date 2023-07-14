import pytest
from selenium import webdriver
import cv2

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope= "class")
def setup(request):

    global driver  # we are telling the code to use the driver we defined in line 3 above(driver = None)
    browser_name = request.config.getoption("browser_name")
    # the line above, extracts the browser name u wana use gotten from line 7 above
    # this browser name will be supplied by u on ur commandline
    # it goes ahead to perform the conditional statements below
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="/Users/eruachijioke/Downloads/chromedriver_mac64/chromedriver")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="/Users/eruachijioke/Downloads/geckodriver")
    elif browser_name == "InternetExplorer":
        print("IE driver")  # later put the IE driver path here

    driver.implicitly_wait(50)
    driver.get("https://www.amazon.com/")
    # driver.maximize_window()
    print(driver.title)
    assert "Spend less." in driver.title
    request.cls.driver = driver

    yield
    #driver.close()

    # we can delete all items in our cart, WE USE THAT AS A CLEAN UP MEACHANISM

    # The function below, attaches a screenshot of the page where the test failed to the log file generated after
    # the test. it names the screenshot with the name of the function/testcase inside which the failure occurred
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
            """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                        'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)


# You can check the documentation for this --it changes the title we see in the report
def pytest_html_report_title(report):
    report.title = "Amazon Shopping Automation Report"

# CHECK HOW TO ADD THIS LATER TO COLOUR YOUR LOG
