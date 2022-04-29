from selenium import webdriver
from selenium.webdriver.common.by import By


class BooksPage:
    first_book_nouveautes_selector = "div.a-section.octopus-pc-item-hue-shield.octopus-pc-item-image-background-v3"

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def selectFirstBookNouveautes(self):
        self.driver.find_element(By.CSS_SELECTOR, self.first_book_nouveautes_selector).click()
