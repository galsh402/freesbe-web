from imports import *


class Blog_Component:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    def home_page_locators(self):
        Articles_Component = self.driver.find_element(By.ID,"homepage-blog")
        Articles_button = self.driver.find_element(By.XPATH,"//*[@id=\"homepage-blog\"]/div[2]/a/button")
        return Articles_Component, Articles_button

    def navigate_to_blog_page(self):
        Articles_Component, Articles_button = self.home_page_locators()
        print('navigate_to_blog_page start')
        Base.long_waiting(self)
        Base.scrolling(self, Articles_Component)
        self.driver.implicitly_wait(15)
        Articles_button.click()
        self.driver.implicitly_wait(15)
        expected_articles_page = 'https://freesbe.com/blog'
        assert expected_articles_page in self.driver.current_url
        print('navigate_to_blog_page end')