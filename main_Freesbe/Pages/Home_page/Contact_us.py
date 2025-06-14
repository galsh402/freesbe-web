from imports import *


class Contact_Us_Component:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    def Contact_Us_locators(self):
        Phone_button = self.driver.find_element(By.XPATH,"//*[@id=\"__next\"]/div[2]/section[3]/div/div[2]/button[1]/p")
        phone_number = self.driver.find_element(By.XPATH,"//*[@id=\"__next\"]/div[2]/section[3]/div/div[2]/button[1]/p")
        return Phone_button, phone_number

    def Clicking_on_a_contact_us_buttons(self):
        Phone_button, phone_number = self.Contact_Us_locators()
        print('Clicking_on_a_contact_us_button start')
        Base.long_waiting(self)
        Base.scrolling(self, Phone_button)
        Phone_button.click()
        Base.long_waiting(self)
        expected_phone_number = '077-8040834'
        assert expected_phone_number == phone_number
        print('Clicking_on_a_contact_us_button end')