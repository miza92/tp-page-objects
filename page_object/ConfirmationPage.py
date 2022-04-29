from selenium import webdriver
from selenium.webdriver.common.by import By


class ConfirmationPage:
    open_cart_selector = "a.a-button-text"

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def openCart(self):
        self.driver.find_element(By.CSS_SELECTOR, self.open_cart_selector).click()




