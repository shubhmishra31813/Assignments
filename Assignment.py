import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.mark.parametrize("login_input,password_input",[("standard_user","secret_sauce")])
def test_TestCase_1(login_input,password_input):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.saucedemo.com/")
    print("after wait1")
    driver.maximize_window()
    driver.implicitly_wait(20)
    print("after wait")
    driver.find_element_by_id("user-name").send_keys(login_input)
    print("after urser name")
    driver.find_element_by_id("password").send_keys(password_input)
    print("after password")
    driver.find_element_by_id("login-button").click()