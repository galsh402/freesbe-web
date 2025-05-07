from imports import *


class Leasing_car_results_Component:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    #Fetches the number of cars from the results page
    def get_car_count(self) -> int:
        print('get_car_count start')
        Base.long_waiting(self)
        car_count_element = self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div[2]/div[4]/div[1]/div/h2")
        full_text = car_count_element.text
        car_count = int(full_text.split()[1].replace(',', ''))
        print('get_car_count end')
        return car_count

