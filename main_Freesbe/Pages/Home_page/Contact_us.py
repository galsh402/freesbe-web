from imports import *


class Contact_Us_Component:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    def Contact_Us_locators(self):
        Phone_button = self.driver.find_element(By.XPATH,"//*[@id=\"__next\"]/div[2]/section[3]/div/div[2]/button[1]")
        WhatsApp_button = self.driver.find_element(By.XPATH,"//*[@id=\"__next\"]/div[2]/section[3]/div/div[2]/button[2]")
        phone_number = self.driver.find_element(By.XPATH,"//*[@id=\"__next\"]/div[2]/section[3]/div/div[2]/button[1]/p")
        return Phone_button,  WhatsApp_button, phone_number

    def Clicking_on_a_contact_us_button(self):
        Phone_button,  WhatsApp_button, phone_number = self.Contact_Us_locators()
        print('Clicking_on_a_contact_us_button start')
        self.driver.implicitly_wait(10)
        Base.scrolling(self, Phone_button)
        Phone_button.click()
        Base.Short_waiting(self)
        expected_phone_number = '077-8040834'
        assert expected_phone_number == phone_number
        Base.Short_waiting(self)
        WhatsApp_button.click()
        expected_WhatsApp_button_url = "https://api.whatsapp.com/send/?phone=972502807648&text=%D7%90%D7%A9%D7%9E%D7%97+%D7%9C%D7%A9%D7%9E%D7%95%D7%A2+%D7%A4%D7%A8%D7%98%D7%99%D7%9D+%D7%9E%D7%A0%D7%A6%D7%99%D7%92+freesbe&type=phone_number&app_absent=0"
        assert expected_WhatsApp_button_url in self.driver.current_url
        print('Clicking_on_a_contact_us_button end')