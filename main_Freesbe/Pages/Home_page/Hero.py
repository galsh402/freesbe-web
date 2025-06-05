from imports import *


class Hero_Component:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    def Hero_locators(self):
        New_car_lobby = self.driver.find_element(By.ID, "main-content")
        Leasing_car_lobby = self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div[2]/section[1]/div[3]/div/a[3]")
        Used_car_lobby = self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div[2]/section[1]/div[3]/div/a[2]")
        rental_web = self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div[2]/section[1]/div[3]/a")
        return New_car_lobby, Leasing_car_lobby, Used_car_lobby, rental_web

    def Clicking_on_a_New_lobby_button(self):
        New_car_lobby, Leasing_car_lobby, Used_car_lobby, rental_web = self.Hero_locators()
        print(' Clicking_on_a_New_lobby_button start')
        self.driver.implicitly_wait(10)
        New_car_lobby.click()
        Base.long_waiting(self)
        expected_new_lobby_url = "https://freesbe.com/new-car-for-sale"
        assert expected_new_lobby_url in self.driver.current_url
        self.driver.back()
        self.driver.implicitly_wait(10)
        print(' Clicking_on_a_New_lobby_button end')

    def Clicking_on_a_private_leasing_lobby_button(self):
        New_car_lobby, Leasing_car_lobby, Used_car_lobby, rental_web = self.Hero_locators()
        print('Clicking_on_a_private_leasing_lobby_button start')
        self.driver.implicitly_wait(10)
        Leasing_car_lobby.click()
        Base.long_waiting(self)
        expected_private_leasing_lobby_url = "https://freesbe.com/private-leasing"
        assert expected_private_leasing_lobby_url in self.driver.current_url
        self.driver.back()
        self.driver.implicitly_wait(10)
        print('Clicking_on_a_private_leasing_lobby_button end')

    def Clicking_on_a_Used_lobby_button(self):
        New_car_lobby, Leasing_car_lobby, Used_car_lobby, rental_web = self.Hero_locators()
        print('Clicking_on_a_Used_lobby_button start')
        self.driver.implicitly_wait(10)
        Used_car_lobby.click()
        Base.long_waiting(self)
        expected_Used_lobby_url = "https://freesbe.com/used-car-for-sale"
        assert expected_Used_lobby_url in self.driver.current_url
        self.driver.back()
        self.driver.implicitly_wait(10)
        print('Clicking_on_a_Used_lobby_button end')

    def Move_to_rental_web(self):
        New_car_lobby, Leasing_car_lobby, Used_car_lobby, rental_web = self.Hero_locators()
        print('Move_to_rental_web start')
        self.driver.implicitly_wait(10)
        rental_web.click()
        Base.long_waiting(self)
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[1])
        expected_rental_web = "https://rental.freesbe.com/?utm_source=freesbe&utm_medium=referral"
        assert expected_rental_web in self.driver.current_url
        self.driver.close()
        self.driver.switch_to.window(tabs[0])
        print('Move_to_rental_web end')
