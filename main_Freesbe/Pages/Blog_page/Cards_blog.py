from imports import *


class Cards_Component:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    def blog_page_locators(self):
        Blog_cards = self.driver.find_elements(By.CLASS_NAME, "blog-card-cta")
        All_links = self.driver.find_elements(By.TAG_NAME, 'a')
        More_articles_button = self.driver.find_element(By.ID, "more-blog-content-cta")
        Scroll_up_button = self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div[6]/div/div/div/button/div/p")
        return Blog_cards, All_links, More_articles_button, Scroll_up_button

    def scroll_and_load_more_articles(self):
        Blog_cards, All_links, More_articles_button, Scroll_up_button = self.blog_page_locators()
        print('scroll_and_load_more_articles start')
        self.driver.implicitly_wait(10)
        for scroll in range(3):
            Base.scrolling(self, More_articles_button)
            Base.Short_waiting(self)
            More_articles_button.click()
            Base.Short_waiting(self)
        Base.scrolling(self, Scroll_up_button)
        Base.Short_waiting(self)
        Scroll_up_button.click()
        Base.Short_waiting(self)
        print('scroll_and_load_more_articles end')

    def click_and_verify_articles(self):
        Blog_cards, All_links, More_articles_button, Scroll_up_button = self.blog_page_locators()
        print('click_and_verify_articles start')
        Base.Short_waiting(self)
        for card in Blog_cards:
            try:
                card.click()
                Base.long_waiting(self)
                current_url = self.driver.current_url
                self.driver.back()
                print(f"Visited URL: {current_url}")
            except Exception as e:
                print(f"Error with card: {e}")
        print('click_and_verify_articles end')