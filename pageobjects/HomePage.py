from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self,driver):
        self.driver=driver

    def rent_tab(self):
        return self.driver.find_element(By.XPATH, "//*[@id=\"rentheading\"]")

    def click_rent_tab(self):
        self.rent_tab().click()