from imports import *


class Additional_services_Component:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    def Additional_services_gallery_locators(self):
        Insurance_page = self.driver.find_element(By.XPATH,"//*[@id=\"__next\"]/div[2]/section[2]/div[2]/div[1]/div[1]/a")
        Funding_page = self.driver.find_element(By.XPATH,"//*[@id=\"__next\"]/div[2]/section[2]/div[2]/div[1]/div[2]/a")
        Charging_solutions_page = self.driver.find_element(By.XPATH,"//*[@id=\"__next\"]/div[2]/section[2]/div[2]/div[1]/div[3]/a")
        Business_leasing_page = self.driver.find_element(By.XPATH,"//*[@id=\"__next\"]/div[2]/section[2]/div[2]/div[1]/div[4]/a")
        return Insurance_page,Funding_page,Charging_solutions_page,Business_leasing_page

    def Clicking_on_a_insurance_button(self):
        Insurance_page, Funding_page, Charging_solutions_page, Business_leasing_page = self.Additional_services_gallery_locators()
        print('Clicking_on_a_insurance_button start')
        Base.long_waiting(self)
        Base.scrolling(self, Insurance_page)
        Insurance_page.click()
        Base.long_waiting(self)
        expected_Insurance_page_url = 'https://freesbe.com/insurance-page'
        assert expected_Insurance_page_url in self.driver.current_url
        self.driver.back()
        self.driver.implicitly_wait(10)
        print('Clicking_on_a_insurance_button end')

    def Clicking_on_a_Funding_button(self):
        Insurance_page, Funding_page, Charging_solutions_page, Business_leasing_page = self.Additional_services_gallery_locators()
        print('Clicking_on_a_Funding_button start')
        Base.long_waiting(self)
        Base.scrolling(self, Funding_page)
        Funding_page.click()
        Base.long_waiting(self)
        expected_Funding_page_url = 'https://freesbe.com/finance'
        assert expected_Funding_page_url in self.driver.current_url
        self.driver.back()
        self.driver.implicitly_wait(10)
        print('Clicking_on_a_Funding_button end')

    def Clicking_on_a_Charging_solutions_button(self):
        Insurance_page, Funding_page, Charging_solutions_page, Business_leasing_page = self.Additional_services_gallery_locators()
        print('Clicking_on_a_Charging_solutions_button start')
        Base.long_waiting(self)
        Base.scrolling(self, Charging_solutions_page)
        Charging_solutions_page.click()
        Base.long_waiting(self)
        expected_Charging_solutions_page_url = 'https://freesbe.com/charging-solutions'
        assert expected_Charging_solutions_page_url in self.driver.current_url
        self.driver.back()
        self.driver.implicitly_wait(10)
        print('Clicking_on_a_Charging_solutions_button end')

    def Clicking_on_a_Business_leasing_button(self):
        Insurance_page, Funding_page, Charging_solutions_page, Business_leasing_page = self.Additional_services_gallery_locators()
        print('Clicking_on_a_Business_leasing_button start')
        Base.long_waiting(self)
        Base.scrolling(self, Business_leasing_page)
        Business_leasing_page.click()
        Base.long_waiting(self)
        expected_Business_leasing_page = "https://freesbe.com/business-leasing"
        assert expected_Business_leasing_page in self.driver.current_url
        self.driver.back()
        self.driver.implicitly_wait(10)
        print("Clicking_on_a_Business_leasing_button end")