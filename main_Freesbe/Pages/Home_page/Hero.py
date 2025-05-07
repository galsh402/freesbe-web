from imports import *


class Hero_Component:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    def Hero_locators(self):
        H1_title = self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div[2]/section[1]/div[3]/h1/span[3]")
        H2_title = self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div[2]/section[1]/div[3]/p/span[3]")
        New_car_lobby = self.driver.find_element(By.ID, "main-content")
        Leasing_car_lobby = self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div[2]/section[1]/div[3]/div/a[3]")
        Used_car_lobby = self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div[2]/section[1]/div[3]/div/a[2]")
        rental_web = self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div[2]/section[1]/div[3]/a")
        return H1_title, H2_title, New_car_lobby, Leasing_car_lobby, Used_car_lobby, rental_web

    def Clicking_on_a_New_lobby_button(self):
        H1_title, H2_title, New_car_lobby, Leasing_car_lobby, Used_car_lobby, rental_web = self.Hero_locators()
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
        H1_title, H2_title, New_car_lobby, Leasing_car_lobby, Used_car_lobby, rental_web = self.Hero_locators()
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
        H1_title, H2_title, New_car_lobby, Leasing_car_lobby, Used_car_lobby, rental_web = self.Hero_locators()
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
        H1_title, H2_title, New_car_lobby, Leasing_car_lobby, Used_car_lobby, rental_web = self.Hero_locators()
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

    def Get_hero_texts_and_headers(self):
        H1_title, H2_title, New_car_lobby, Leasing_car_lobby, Used_car_lobby, rental_web = self.Hero_locators()
        print('Get_hero_texts_and_headers start')
        font_size_H1 = H1_title.value_of_css_property('font-size')
        H1_color = H1_title.value_of_css_property('color')
        font_size_H2 = H2_title.value_of_css_property('font-size')
        H2_color = H2_title.value_of_css_property('color')
        rental_link_font_size = rental_web.value_of_css_property('font-size')
        rental_link_color = rental_web.value_of_css_property('color')
        main_title = H1_title.text
        subtitle = H2_title.text
        rental_link_text = rental_web.text
        print('Get_hero_texts_and_headers end')
        return font_size_H1, H1_color, font_size_H2, H2_color, rental_link_font_size, rental_link_color, main_title, subtitle, rental_link_text