from imports import *

class Header_Component:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    def Header_locators(self):
        New_car_lobby = self.driver.find_element(By.XPATH,"//*[@id=\"__next\"]/div[1]/div/div[2]/div[1]/div/nav/div[1]/div/a")
        Leasing_car_lobby = self.driver.find_element(By.XPATH,"//*[@id=\"__next\"]/div[1]/div/div[2]/div[1]/div/nav/div[2]/div/a")
        Used_car_lobby = self.driver.find_element(By.XPATH,"//*[@id=\"__next\"]/div[1]/div/div[2]/div[1]/div/nav/div[3]/div/a")
        Rental_web = self.driver.find_element(By.XPATH,"//*[@id=\"__next\"]/div[1]/div/div[2]/div[1]/div/nav/div[4]/div/a")
        Solutions_page = self.driver.find_element(By.XPATH,"//*[@id=\"__next\"]/div[1]/div/div[2]/div[1]/div/nav/div[5]/div/p")
        My_leasing_web = self.driver.find_element(By.XPATH,"//*[@id=\"__next\"]/div[1]/div/div[2]/div[1]/div/nav/div[6]/div/a")
        Contact_us_page = self.driver.find_element(By.XPATH,"//*[@id=\"__next\"]/div[1]/div/div[2]/div[1]/div/nav/div[7]")
        wishlist_page = self.driver.find_element(By.XPATH,"//*[@id=\"__next\"]/div[1]/div/div[2]/div[2]/a")
        return New_car_lobby, Leasing_car_lobby, Used_car_lobby, Rental_web, Solutions_page, My_leasing_web, Contact_us_page, wishlist_page

    def Clicking_on_a_New_lobby_button(self):
        New_car_lobby, Leasing_car_lobby, Used_car_lobby, Rental_web, Solutions_page, My_leasing_web, Contact_us_page, wishlist_page = self.Header_locators()
        Base.long_waiting(self)
        New_car_lobby.click()
        Base.long_waiting(self)
        expected_new_lobby_url = "https://freesbe.com/new-car-for-sale"
        assert expected_new_lobby_url in self.driver.current_url
        self.driver.back()
        self.driver.implicitly_wait(10)

    def Clicking_on_a_private_leasing_lobby_button(self):
        New_car_lobby, Leasing_car_lobby, Used_car_lobby, Rental_web, Solutions_page, My_leasing_web, Contact_us_page, wishlist_page = self.Header_locators()
        Base.long_waiting(self)
        Leasing_car_lobby.click()
        Base.long_waiting(self)
        expected_private_leasing_lobby_url = "https://freesbe.com/private-leasing"
        assert expected_private_leasing_lobby_url in self.driver.current_url
        self.driver.back()
        self.driver.implicitly_wait(10)

    def Clicking_on_a_Used_lobby_button(self):
        New_car_lobby, Leasing_car_lobby, Used_car_lobby, Rental_web, Solutions_page, My_leasing_web, Contact_us_page, wishlist_page = self.Header_locators()
        Base.long_waiting(self)
        Used_car_lobby.click()
        Base.long_waiting(self)
        expected_Used_lobby_url = "https://freesbe.com/used-car-for-sale"
        assert expected_Used_lobby_url in self.driver.current_url
        self.driver.back()
        self.driver.implicitly_wait(10)

    def Move_to_rental_web(self):
        New_car_lobby, Leasing_car_lobby, Used_car_lobby, Rental_web, Solutions_page, My_leasing_web, Contact_us_page, wishlist_page = self.Header_locators()
        Base.long_waiting(self)
        Rental_web.click()
        Base.long_waiting(self)
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[1])
        expected_rental_web = "https://rental.freesbe.com/?utm_source=freesbe&utm_medium=referral"
        assert expected_rental_web in self.driver.current_url
        self.driver.close()
        self.driver.switch_to.window(tabs[0])

    def Clicking_on_a_charging_solutions_button(self):
        New_car_lobby, Leasing_car_lobby, Used_car_lobby, Rental_web, Solutions_page, My_leasing_web, Contact_us_page, wishlist_page = self.Header_locators()
        Base.long_waiting(self)
        Base.Hovering(self,Solutions_page)
        Funding_page = self.driver.find_element(By.XPATH,"//*[@id=\"__next\"]/div[1]/div/div[2]/div[1]/div/nav/div[5]/div[2]/div[2]/nav/div[1]/div/a")
        Funding_page.click()
        Base.long_waiting(self)
        expected_funding_page_url = "https://freesbe.com/finance"
        assert expected_funding_page_url in self.driver.current_url
        self.driver.back()
        Base.Hovering(self,Solutions_page)
        Insurance_page = self.driver.find_element(By.XPATH,"//*[@id=\"__next\"]/div[1]/div/div[2]/div[1]/div/nav/div[5]/div[2]/div[2]/nav/div[2]/div/a")
        Insurance_page.click()
        Base.long_waiting(self)
        expected_Insurance_pag_url = "https://freesbe.com/insurance-page"
        assert expected_Insurance_pag_url in self.driver.current_url
        self.driver.back()
        Base.Hovering(self,Solutions_page)
        Charging_Solutions_page = self.driver.find_element(By.XPATH,"//*[@id=\"__next\"]/div[1]/div/div[2]/div[1]/div/nav/div[5]/div[2]/div[2]/nav/div[3]/div/a")
        Charging_Solutions_page.click()
        Base.long_waiting(self)
        expected_Charging_Solutions_page_url = "https://freesbe.com/charging-solutions"
        assert expected_Charging_Solutions_page_url in self.driver.current_url
        self.driver.back()
        Base.Hovering(self,Solutions_page)
        Business_leasing_page = self.driver.find_element(By.XPATH,"//*[@id=\"__next\"]/div[1]/div/div[2]/div[1]/div/nav/div[5]/div[2]/div[2]/nav/div[4]/div/a")
        Business_leasing_page.click()
        Base.long_waiting(self)
        expected_Business_leasing_page = "https://freesbe.com/business-leasing"
        assert expected_Business_leasing_page in self.driver.current_url
        self.driver.back()

    def Clicking_on_contact_us_button(self):
        New_car_lobby, Leasing_car_lobby, Used_car_lobby, Rental_web, Solutions_page, My_leasing_web, Contact_us_page, wishlist_page = self.Header_locators()
        Base.long_waiting(self)
        Base.Hovering(self,Contact_us_page)
        our_locations = self.driver.find_element(By.XPATH,"//*[@id=\"__next\"]/div[1]/div/div[2]/div[1]/div/nav/div[7]/div[2]/div[2]/nav/div[2]/div/a/p")
        our_locations.click()
        Base.long_waiting(self)
        expected_leave_details_page_url = 'https://freesbe.com/our'
        assert expected_leave_details_page_url in self.driver.current_url
        self.driver.back()
        Base.Hovering(self, Contact_us_page)
        leave_details_page = self.driver.find_element(By.XPATH,"//*[@id=\"__next\"]/div[1]/div/div[2]/div[1]/div/nav/div[7]/div[2]/div[2]/nav/div[1]/div/a/p")
        leave_details_page.click()
        Base.long_waiting(self)
        expected_our_locations_page_url = 'https://freesbe.com/contact'
        assert expected_our_locations_page_url in self.driver.current_url
        self.driver.back()
        Base.Hovering(self,Contact_us_page)
        service_web = self.driver.find_element(By.XPATH,"//*[@id=\"__next\"]/div[1]/div/div[2]/div[1]/div/nav/div[7]/div[2]/div[2]/nav/div[3]/div/a")
        service_web.click()
        Base.long_waiting(self)
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[1])
        expected_service_web_url = 'https://service.freesbe.com'
        assert expected_service_web_url in self.driver.current_url
        self.driver.close()
        self.driver.switch_to.window(tabs[0])

    def Clicking_on_wishlist_page(self):
        New_car_lobby, Leasing_car_lobby, Used_car_lobby, Rental_web, Solutions_page, My_leasing_web, Contact_us_page, wishlist_page = self.Header_locators()
        Base.long_waiting(self)
        wishlist_page.click()
        Base.long_waiting(self)
        expected_wishlist_page_url = 'https://freesbe.com/wishlist'
        assert expected_wishlist_page_url in self.driver.current_url
        self.driver.back()