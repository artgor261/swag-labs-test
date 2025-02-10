from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure
        
@pytest.fixture()
@allure.title("Get driver object fixture")
def get_driver():
    drivers = {
        'chrome': (webdriver.ChromeOptions, webdriver.Chrome),
        'edge': (webdriver.EdgeOptions, webdriver.Edge),
        'firefox': (webdriver.FirefoxOptions, webdriver.Firefox),
        'safari': (webdriver.SafariOptions, webdriver.Safari)
    }
    
    driver_name = input('Print browser name: ').lower()
    version = input('Print browser version (stable recommended): ').lower()

    options = drivers[driver_name][0]()
    options.browser_version = version

    with allure.step("Checking browser's name and version"):
        assert options.capabilities['browserVersion'] == version
        assert options.capabilities['browserName'] == driver_name

    driver = drivers[driver_name][1](options=options)
    
    yield driver

    driver.quit()

@pytest.fixture()
@allure.title("Log in fixture")
def login(get_driver):
    driver = get_driver
    driver.get("https://www.saucedemo.com/")

    with allure.step("Checking page's loading"):
        assert driver.find_element(By.CLASS_NAME, value="login_logo").text == "Swag Labs"

    username = driver.find_element(By.NAME, value="user-name")
    password = driver.find_element(By.NAME, value="password")
    submit_button = driver.find_element(By.NAME, value="login-button")


    username.clear()
    password.clear()

    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    submit_button.click()

    return driver

def sign_in(login):
    driver = login
    
    logo = driver.find_element(By.CLASS_NAME, value="app_logo").text
    
    return logo

def sign_out(login):
    driver = login
    driver.find_element(By.ID, value="react-burger-menu-btn").click()
    
    driver.implicitly_wait(5)
    
    logout = driver.find_element(By.LINK_TEXT, value="Logout")
    logout.click()
    
    driver.implicitly_wait(5)

    logo = driver.find_element(
        By.XPATH,
        value="//div[text()='Swag Labs' and @class='login_logo']"
        ).text
    
    return logo