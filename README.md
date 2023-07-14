# Test_Automation_Framework_For_Amazon_E-Commerce_Website
Developed an end-to-end automated testing Framework for Amazon E-commerce website. I utilized selenium test automation Framework in Python and page object optimization to achieve this. Created and executed several test cases to validate the functionality and performance of the web-based e-commerce platform. Utilizing pytest, I performed logging of test case execution stages. The pytest logs generated are then integrated into a HTML report and in case of test failures, a screenshot of the web page where a test failure occurred is captured and attached to the html report generated at the end of the test. Further integrated the test automation framework into Jenkins for continuous integration (CI). 

I attached two videos where I tested this automation framework. The first Video shows where the test is run on my local MAC and the other video shows where the test is run in my JENKINS account.

## Things to do before running the Framework
Create an account at https://www.amazon.com/

This is to provide you with the email address and password to access the website while the test is executed

Add this email and password in line 72 and 76 of the test_e2e.py file inside the "tests" folder
