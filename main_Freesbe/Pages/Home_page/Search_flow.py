from imports import *


class Search_flow_Component:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    def Search_flow_locators(self):
        Search_flow_main_title = self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div[2]/div[2]/div[1]/h2")
        monthly_price = self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div[2]/div[2]/div[2]/div[1]/div")
        accurate_search = self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div[2]/div[2]/div[2]/div[2]")
        general_Search = self.driver.find_element(By.XPATH,"//*[@id=\"__next\"]/div[2]/div[2]/div[2]/div[3]")
        return Search_flow_main_title, monthly_price, accurate_search, general_Search

    def Clicking_on_a_monthly_price(self):
        Search_flow_main_title, monthly_price, accurate_search, general_Search = self.Search_flow_locators()
        print('Clicking_on_a_monthly_price start')
        self.driver.implicitly_wait(10)
        Base.scrolling(self, monthly_price)
        Base.long_waiting(self)
        monthly_price.click()
        Base.long_waiting(self)
        expected_budget_page_url = 'https://freesbe.com/search-flow/budget?'
        assert expected_budget_page_url in self.driver.current_url
        self.driver.back()
        self.driver.implicitly_wait(10)
        print('Clicking_on_a_budget_button end')

    def Clicking_on_a_accurate_Search(self):
        Search_flow_main_title, monthly_price, accurate_search, general_Search = self.Search_flow_locators()
        print('Clicking_on_a_accurateSearch_button start')
        self.driver.implicitly_wait(10)
        Base.scrolling(self, accurate_search)
        accurate_search.click()
        Base.long_waiting(self)
        expected_accurateSearch_page_url = 'https://freesbe.com/search-flow/accurateSearch?'
        assert expected_accurateSearch_page_url in self.driver.current_url
        self.driver.back()
        self.driver.implicitly_wait(10)
        print('Clicking_on_a_Search_flow_component end')

    def Clicking_on_a_general_Search(self):
        Search_flow_main_title, monthly_price, accurate_search, general_Search = self.Search_flow_locators()
        print('Clicking_on_a_general_Search start')
        Base.scrolling(self,general_Search)
        general_Search.click()
        Base.long_waiting(self)
        expected_leave_details_page_url = 'https://freesbe.com/search-flow/generalSearch?'
        assert expected_leave_details_page_url in self.driver.current_url
        self.driver.back()
        self.driver.implicitly_wait(10)
        print('Clicking_on_a_general_Search end')