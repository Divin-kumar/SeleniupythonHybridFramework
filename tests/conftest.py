import time

import pytest
from selenium import webdriver

from utilities.ReadProperties import ReadProperties

driver=None


@pytest.fixture()
def set_up(request):
    global driver
    browser=ReadProperties.get_browser()
    if browser=="Chrome":
        driver = webdriver.Chrome()
    elif browser=="Edge":
        driver = webdriver.Edge()
    driver.maximize_window()
    url=ReadProperties.get_url()
    driver.get(url)
    time.sleep(2)
    request.cls.driver=driver
    yield
    driver.quit()