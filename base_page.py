from imports import *


class Base:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    def scrolling(self, element):
        self.driver.implicitly_wait(10)
        actions = ActionChains(self.driver)
        actions.scroll_to_element(element).perform()
        self.driver.implicitly_wait(15)

    def Hovering(self, element):
        self.driver.implicitly_wait(10)
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()
        self.driver.implicitly_wait(20)

    def long_waiting(self):
        time.sleep(4.5)

    def Short_waiting(self):
        time.sleep(1.5)