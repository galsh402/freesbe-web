from imports import *


class Contact_Us_Component:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    def Contact_Us_locators(self):
        Contact_us_main_title = self.driver.find_element(By.XPATH,"//*[@id=\"__next\"]/div[2]/section[4]/div/div[1]/p[1]")
        Contact_us_paragraph = self.driver.find_element(By.XPATH,"//*[@id=\"__next\"]/div[2]/section[4]/div/div[1]/p[2]")
        Call_button_text = self.driver.find_element(By.XPATH,"//*[@id=\"__next\"]/div[2]/section[4]/div/div[2]/button[1]")
        WhatsApp_button_text = self.driver.find_element(By.XPATH,"//*[@id=\"__next\"]/div[2]/section[4]/div/div[2]/button[2]")
        return Contact_us_main_title,Contact_us_paragraph,Call_button_text, WhatsApp_button_text

    def Clicking_on_a_contact_us_button(self):
        Contact_us_main_title,Contact_us_paragraph, Call_button_text, WhatsApp_button_text = self.Contact_Us_locators()
        print('Clicking_on_a_contact_us_button start')
        self.driver.implicitly_wait(10)
        Base.scrolling(self, Call_button_text)
        expected_call_button_text = 'חייגו אלינו'
        assert expected_call_button_text == Call_button_text.text
        Base.scrolling(self, WhatsApp_button_text)
        expected_whatsapp_button_text = 'לשליחת WhatsApp'
        assert expected_whatsapp_button_text == WhatsApp_button_text.text
        print(f'{Call_button_text.text, WhatsApp_button_text.text}')
        print('Clicking_on_a_contact_us_button end')

    def get_contact_us_texts_and_headers(self):
        Contact_us_main_title,Contact_us_paragraph, Call_button_text, WhatsApp_button_text = self.Contact_Us_locators()
        print('get_contact_us_texts_and_headers start')
        main_title_text = Contact_us_main_title.text
        main_title_font_size = Contact_us_main_title.value_of_css_property('font-size')
        main_title_color = Contact_us_main_title.value_of_css_property('color')
        paragraph_text = Contact_us_paragraph.text
        paragraph_font_size = Contact_us_paragraph.value_of_css_property('font-size')
        paragraph_color = Contact_us_paragraph.value_of_css_property('color')
        print('get_contact_us_texts_and_headers end')
        return main_title_text, main_title_font_size, main_title_color, paragraph_text, paragraph_font_size, paragraph_color