from selenium import webdriver
from selenium.webdriver.common.by import By


class ProductPage:
    add_to_cart_selector = "input#add-to-cart-button"

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def addToCart(self):
        self.driver.find_element(By.CSS_SELECTOR, self.add_to_cart_selector).click()
