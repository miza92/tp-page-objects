from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as wait

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class CartPage:
    quantity_select = "select[name='quantity']"
    result_quantity = "#span.a - dropdown - prompt"
    result_quantity = "#quantity > option:nth-child(3)"

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver


    def changeQuantity(self, arg):
        quantity_select_element = Select(
            wait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.quantity_select)))
        )
        quantity_select_element.select_by_value(arg)


    def getQuantity(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.result_quantity).text


