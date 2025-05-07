from imports import *


@pytest.fixture(scope="session", autouse=True)
def driver():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()
