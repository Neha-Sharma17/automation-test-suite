import pytest
from driver_setup import get_driver
from login_page import LoginPage

def test_login():
    driver = get_driver()
    
    page = LoginPage(driver)
    page.open("https://the-internet.herokuapp.com/login")
    
    page.enter_username("tomsmith")
    page.enter_password("SuperSecretPassword!")
    page.click_login()
    
    assert "secure" in driver.current_url
    
    driver.quit()