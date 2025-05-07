from imports import *


class New_car_results:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    def get_car_count(self) -> int:
        print('get_car_count start')
        Base.long_waiting(self)
        car_count_element = self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div[2]/div[4]/div[1]/div/h2")
        full_text = car_count_element.text
        car_count = int(full_text.split()[1].replace(',', ''))
        print('get_car_count end')
        return car_count

    def main_filters_locators(self):
        manufacturer_filter = self.driver.find_element(By.XPATH, "//*[@id=\"filters\"]/div[1]/div/div[1]/div[1]/div[1]")
        model_filter = self.driver.find_element(By.XPATH, "//*[@id=\"filters\"]/div[1]/div/div/div[1]/div[2]")
        price_filter = self.driver.find_element(By.XPATH, "//*[@id=\"filters\"]/div[1]/div/div/div[1]/div[3]")
        load_more_filters_button = self.driver.find_element(By.ID, "additoinal-filters-cta")
        return manufacturer_filter, model_filter, price_filter, load_more_filters_button

    def click_and_verify_manufacturers_filter(self):
        manufacturer_filter, model_filter, price_filter, load_more_filters_button = self.main_filters_locators()
        print('click_and_verify_manufacturer_filter start')
        Base.Short_waiting(self)
        manufacturer_filter.click()
        self.driver.implicitly_wait(10)
        xpeng = self.driver.find_element(By.XPATH,"//*[@id=\"filters\"]/div[1]/div/div/div[1]/div[1]/div[2]/div/div[3]/li[1]/span[1]/input")
        xpeng.click()
        self.driver.implicitly_wait(10)
        expected_page_url = "https://freesbe.com/new-car-for-sale/listings/xpeng?brands=XPENG"
        assert expected_page_url in self.driver.current_url
        xpeng.click()
        evesy = self.driver.find_element(By.XPATH,"//*[@id=\"filters\"]/div[1]/div/div/div[1]/div[1]/div[2]/div/div[3]/li[2]/span[1]/input")
        evesy.click()
        self.driver.implicitly_wait(10)
        expected_page_url = "https://freesbe.com/new-car-for-sale/listings/eveasy?brands=%D7%90%D7%99%D7%91%D7%99%D7%96%D7%99"
        assert expected_page_url in self.driver.current_url
        evesy.click()
        infiniti = self.driver.find_element(By.XPATH,"//*[@id=\"filters\"]/div[1]/div/div/div[1]/div[1]/div[2]/div/div[3]/li[3]/span[1]/input")
        infiniti.click()
        self.driver.implicitly_wait(10)
        expected_page_url = "https://freesbe.com/new-car-for-sale/listings/infiniti?brands=%D7%90%D7%99%D7%A0%D7%A4%D7%99%D7%A0%D7%99%D7%98%D7%99"
        assert expected_page_url in self.driver.current_url
        infiniti.click()
        dacia = self.driver.find_element(By.XPATH,"//*[@id=\"filters\"]/div[1]/div/div/div[1]/div[1]/div[2]/div/div[3]/li[4]/span[1]/input")
        dacia.click()
        self.driver.implicitly_wait(10)
        expected_page_url = "https://freesbe.com/new-car-for-sale/listings/dacia?brands=%D7%93%D7%90%D7%A6%27%D7%99%D7%94"
        assert expected_page_url in self.driver.current_url
        dacia.click()
        nissan = self.driver.find_element(By.XPATH,"//*[@id=\"filters\"]/div[1]/div/div/div[1]/div[1]/div[2]/div/div[3]/li[5]/span[1]/input")
        Base.scrolling(self, nissan)
        self.driver.implicitly_wait(10)
        nissan.click()
        self.driver.implicitly_wait(10)
        expected_page_url = "https://freesbe.com/new-car-for-sale/listings/nissan?brands=%D7%A0%D7%99%D7%A1%D7%90%D7%9F"
        assert expected_page_url in self.driver.current_url
        nissan.click()
        chery = self.driver.find_element(By.XPATH,"//*[@id=\"filters\"]/div[1]/div/div/div[1]/div[1]/div[2]/div/div[3]/li[6]/span[1]/input")
        chery.click()
        self.driver.implicitly_wait(10)
        expected_page_url = "https://freesbe.com/new-car-for-sale/listings/chery?brands=%D7%A6%27%D7%A8%D7%99"
        assert expected_page_url in self.driver.current_url
        chery.click()
        renault = self.driver.find_element(By.XPATH,"//*[@id=\"filters\"]/div[1]/div/div/div[1]/div[1]/div[2]/div/div[3]/li[7]/span[1]/input")
        renault.click()
        self.driver.implicitly_wait(10)
        expected_page_url = "https://freesbe.com/new-car-for-sale/listings/renault?brands=%D7%A8%D7%A0%D7%95"
        assert expected_page_url in self.driver.current_url
        renault.click()
        print("click_and_verify_manufacturer_filter end")
