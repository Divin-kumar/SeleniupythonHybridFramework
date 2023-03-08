import time
import pytest
from selenium.webdriver.common.by import By
from pageobjects.HomePage import HomePage


@pytest.mark.usefixtures("set_up")
class TestRent:

    def test_one(self):
        rent_tab=HomePage(self.driver)
        rent_tab.click_rent_tab()
        time.sleep(2)
        self.driver.find_element(By.XPATH,
                            "//*[@id=\"commercialIndex\"]/header/section[2]/div/ul/li[2]/div/div/div[1]/ul/li[1]/a")

        self.driver.get(
            "https://www.magicbricks.com/property-for-rent/residential-real-estate?proptype=Multistorey-Apartment,"
            "Builder-Floor-Apartment,Penthouse,Studio-Apartment,Service-Apartment,Residential-House,Villa,"
            "Commercial-Office-Space,Office-ITPark-SEZ,Commercial-Shop,Commercial-Showroom,Commercial-Land,"
            "Industrial-Land,Warehouse/-Godown,Industrial-Building,Industrial-Shed&inputListings=I&cityName=Pune")
        time.sleep(3)

        self.driver.find_element(By.XPATH, "//*[@id=\"body\"]/div[1]/div/div[2]/div[1]/div/div[1]/div").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,
                            "//*[@id=\"body\"]/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div[2]/div[1]/label").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id=\"body\"]/div[1]/div/div[2]/div[1]/div/div[2]/div[2]").click()
        time.sleep(2)
        self.driver.get(
            "https://www.magicbricks.com/propertyDetails/1-BHK-500-Sq-ft-Builder-Floor-Apartment-FOR-Rent-Khadki-in"
            "-Pune-r1&id=4d423337393239333035")
        assert self.driver.find_element(By.XPATH,"//*[@id=\"contactRightInfo\"]/div[2]/div/div[2]/span[1]").is_displayed()
        time.sleep(10)
