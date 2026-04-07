from selenium.webdriver.common.by import By
from base_page import BasePage

class LoginPage(BasePage):
    
    def enter_username(self, username):
        self.driver.find_element(By.NAME, "username").send_keys(username)
        
    def enter_password(self, password):
        self.driver.find_element(By.NAME, "password").send_keys(password)
        
    def click_login(self):
        self.driver.find_element(By.XPATH, "//button").click()