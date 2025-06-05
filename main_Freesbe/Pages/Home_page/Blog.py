from imports import *


#class Blog_Component:
#    def __init__(self, driver):
#        self.driver: WebDriver = driver
#
#    def home_page_locators(self):
#        Articles_page = self.driver.find_element(By.XPATH, "//*[@id=\"homepage-blog\"]/div[2]/a")
#        return Articles_page
#
#    def navigate_to_blog_page(self):
#        Articles_page = self.home_page_locators()
#       print('navigate_to_blog_page start')
#        self.driver.implicitly_wait(10)
#        Base.scrolling(self, Articles_page)
#        self.driver.implicitly_wait(10)
#        Articles_page.click()
#        self.driver.implicitly_wait(10)
#        expected_articles_page = 'https://freesbe.com/blog'
#        assert expected_articles_page in self.driver.current_url
#        print('navigate_to_blog_page end')