from selenium import webdriver


def test_amazon1():
    driver = webdriver.Chrome()
    driver.get("http://www.amazon.fr/")
    driver.maximize_window()
    driver.quit()