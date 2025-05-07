from imports import *


class Used_car_results_Component:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    def used_car_locators(self):
        car_count_element = self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div[2]/div[4]/div[1]/div/h2")
        car_cards = self.driver.find_elements(By.CLASS_NAME, "MuiGrid-root MuiGrid-item muirtl-ot8gxe")
        load_more_cars_button = self.driver.find_elements(By.XPATH, "//button[contains(text(), ' עוד מכוניות')]")
        return car_count_element, car_cards, load_more_cars_button

    #Fetches the number of cars from the results page
    def get_car_count(self) -> int:
        print('get_car_count start')
        car_count_element, car_cards, load_more_cars_button = self.used_car_locators()
        Base.long_waiting(self)
        full_text = car_count_element.text
        car_count = int(full_text.split()[1].replace(',', ''))
        print('get_car_count end')
        return car_count

    def scroll_and_load_all_cars(self):
        print('scroll_and_load_all_cars start')
        car_count_element, car_cards, load_more_cars_button = self.used_car_locators()
        while True:
            try:
                Base.scrolling(self, load_more_cars_button)
                load_more_cars_button.click()
                Base.long_waiting(self)

                # Check if the button is clickable
                is_clickable = False
                try:
                    WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'עוד מכוניות')]"))
                    )
                    is_clickable = True
                except Exception:
                    is_clickable = False

                if is_clickable:
                    load_more_cars_button = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'עוד מכוניות')]"))
                    )
                else:
                    break
            except Exception:
                print("No more 'Load More' button found.")
                break

    def get_all_car_cards(self):
        print('get_all_car_cards start')
        car_count_element, car_cards, load_more_cars_button = self.used_car_locators()
        Base.Short_waiting(self)
        print(car_cards)
        return car_cards

    def click_through_all_cars(self):
        car_cards = self.get_all_car_cards()
        for index, car_cards in enumerate(car_cards):
            print(f"Clicking car card {index + 1}...")
            self.driver.execute_script("arguments[0].scrollIntoView(true);", car_cards)
            car_cards.click()
            Base.long_waiting(self)
            current_url = self.driver.current_url
            assert "dealType" in current_url.lower()
            self.driver.back()
            self.driver.implicitly_wait(10)
