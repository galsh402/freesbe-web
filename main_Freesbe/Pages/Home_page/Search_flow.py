from imports import *


class Search_flow_Component:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    def Search_flow_locators(self):
        search_main_title = self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div[2]/div[2]/div[1]/h2")
        budget_button = self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div[2]/div[2]/div[2]/div[1]")
        accurateSearch_button = self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div[2]/div[2]/div[2]/div[2]")
        leave_details_button = self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div[2]/div[2]/div[2]/div[3]")
        general_Search_main_title = self.driver.find_element(By.XPATH,"//*[@id=\"__next\"]/div[2]/section[2]/div[2]/h2")
        general_Search_paragraph = self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div[2]/section[2]/div[2]/p")
        general_Search_button = self.driver.find_element(By.XPATH,"//*[@id=\"__next\"]/div[2]/section[2]/div[2]/button")
        return search_main_title, budget_button, accurateSearch_button, leave_details_button, general_Search_main_title, general_Search_paragraph, general_Search_button

    def Clicking_on_a_budget_button(self):
        search_main_title, budget_button, accurateSearch_button, leave_details_button, general_Search_main_title, general_Search_subtitle, general_Search_button = self.Search_flow_locators()
        print('Clicking_on_a_budget_button start')
        self.driver.implicitly_wait(10)
        Base.scrolling(self, budget_button)
        Base.long_waiting(self)
        budget_button.click()
        Base.long_waiting(self)
        expected_budget_page_url = 'https://freesbe.com/search-flow/budget?'
        assert expected_budget_page_url in self.driver.current_url
        self.driver.back()
        self.driver.implicitly_wait(10)
        print('Clicking_on_a_budget_button end')

    def Clicking_on_a_accurateSearch_button(self):
        search_main_title, budget_button, accurateSearch_button, leave_details_button, general_Search_main_title, general_Search_subtitle, general_Search_button = self.Search_flow_locators()
        print('Clicking_on_a_accurateSearch_button start')
        self.driver.implicitly_wait(10)
        Base.scrolling(self, accurateSearch_button)
        accurateSearch_button.click()
        Base.long_waiting(self)
        expected_accurateSearch_page_url = 'https://freesbe.com/search-flow/accurateSearch?'
        assert expected_accurateSearch_page_url in self.driver.current_url
        self.driver.back()
        self.driver.implicitly_wait(10)
        print('Clicking_on_a_Search_flow_component end')

    def Clicking_on_a_leave_details_button(self):
        search_main_title, budget_button, accurateSearch_button, leave_details_button, general_Search_main_title, general_Search_subtitle, general_Search_button = self.Search_flow_locators()
        print('Clicking_on_a_leave_details_button start')
        Base.scrolling(self,leave_details_button)
        leave_details_button.click()
        Base.long_waiting(self)
        expected_leave_details_page_url = 'https://freesbe.com/contact-us'
        assert expected_leave_details_page_url in self.driver.current_url
        self.driver.back()
        self.driver.implicitly_wait(10)
        print('Clicking_on_a_leave_details_button end')

    def Clicking_on_a_general_Search_button(self):
        search_main_title, budget_button, accurateSearch_button, leave_details_button, general_Search_main_title, general_Search_subtitle, general_Search_button = self.Search_flow_locators()
        print('Clicking_on_a_general_Search_button start')
        Base.scrolling(self,general_Search_button)
        general_Search_button.click()
        Base.long_waiting(self)
        expected_general_Search_page_url = 'https://freesbe.com/search-flow/generalSearch'
        assert expected_general_Search_page_url in self.driver.current_url
        self.driver.back()
        self.driver.implicitly_wait(10)
        print('Clicking_on_a_general_Search_button end')

    def Get_search_flow_texts_and_headers(self):
        search_main_title, budget_button, accurateSearch_button, leave_details_button, general_Search_main_title, general_Search_subtitle, general_Search_button = self.Search_flow_locators()
        print('Get_search_flow_texts_and_headers start')
        first_main_title_text = search_main_title.text
        first_main_title_font_size = search_main_title.value_of_css_property('font-size')
        first_title_color = search_main_title.value_of_css_property('color')
        second_main_title_text = general_Search_main_title.text
        second_main_title_font_size = general_Search_main_title.value_of_css_property('font-size')
        second_main_title_color = general_Search_main_title.value_of_css_property('color')
        paragraph_text = general_Search_subtitle.text
        paragraph_font_size = general_Search_subtitle.value_of_css_property('font-size')
        paragraph_color = general_Search_subtitle.value_of_css_property('color')
        print('Get_search_flow_texts_and_headers end')
        return first_main_title_text, first_main_title_font_size, first_title_color, second_main_title_text, second_main_title_font_size, second_main_title_color, paragraph_text, paragraph_font_size, paragraph_color