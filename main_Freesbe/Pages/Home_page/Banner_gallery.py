from imports import *


#class Banner_gallery_Component:
#    def __init__(self, driver):
#        self.driver: WebDriver = driver
#
#    def Banner_gallery_locators(self):
#        First_banner = self.driver.find_element(By.XPATH,"//*[@id=\"__next\"]/div[2]/div[1]/div/div[2]/div/div/div/div[5]/div/div/div/div")
#        return First_banner
#
#    def verify_Banner_carousel(self):
#        First_banner = self.Banner_gallery_locators()
#        print('verify_Banner_carousel start')
#       Base.long_waiting(self)
#        Base.scrolling(self, First_banner)
#        First_banner.click()
#        Base.long_waiting(self)
#        self.driver.back()
#        self.driver.implicitly_wait(10)
#        print('verify_Banner_carousel end')