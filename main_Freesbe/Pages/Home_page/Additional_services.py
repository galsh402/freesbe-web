from imports import *


class Additional_services_Component:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    def Additional_services_gallery_locators(self):
        Insurance_page = self.driver.find_element(By.XPATH,"//*[@id=\"__next\"]/div[2]/section[3]/div[2]/div[1]/div[1]")
        Funding_page = self.driver.find_element(By.XPATH,"//*[@id=\"__next\"]/div[2]/section[3]/div[2]/div[1]/div[2]")
        Charging_solutions_page = self.driver.find_element(By.XPATH,"//*[@id=\"__next\"]/div[2]/section[3]/div[2]/div[1]/div[3]")
        Business_leasing_page = self.driver.find_element(By.XPATH,"//*[@id=\"__next\"]/div[2]/section[3]/div[2]/div[1]/div[4]")
        return Insurance_page,Funding_page,Charging_solutions_page,Business_leasing_page

    def Get_text_and_header_locators(self):
        Additional_services_main_title = self.driver.find_element(By.XPATH,"//*[@id=\"__next\"]/div[2]/section[3]/div[1]/h2")
        Insurance_main_title = self.driver.find_element(By.XPATH,"//*[@id=\"__next\"]/div[2]/section[3]/div[2]/div[1]/div[1]/a/div[2]/h4")
        Insurance_paragraph = self.driver.find_element(By.XPATH,"//*[@id=\"__next\"]/div[2]/section[3]/div[2]/div[1]/div[1]/a/div[2]/p")
        Funding_main_title = self.driver.find_element(By.XPATH,"//*[@id=\"__next\"]/div[2]/section[3]/div[2]/div[1]/div[2]/a/div[2]/h4")
        Funding_paragraph = self.driver.find_element(By.XPATH,"//*[@id=\"__next\"]/div[2]/section[3]/div[2]/div[1]/div[2]/a/div[2]/p")
        Charging_solutions_main_title = self.driver.find_element(By.XPATH,"//*[@id=\"__next\"]/div[2]/section[3]/div[2]/div[1]/div[3]/a/div[2]/h4")
        Charging_solutions_paragraph = self.driver.find_element(By.XPATH,"//*[@id=\"__next\"]/div[2]/section[3]/div[2]/div[1]/div[3]/a/div[2]/p")
        Business_leasing_main_title = self.driver.find_element(By.XPATH,"//*[@id=\"__next\"]/div[2]/section[3]/div[2]/div[1]/div[4]/a/div[2]/h4")
        Business_leasing_paragraph = self.driver.find_element(By.XPATH,"//*[@id=\"__next\"]/div[2]/section[3]/div[2]/div[1]/div[4]/a/div[2]/p")
        return Additional_services_main_title,Insurance_main_title,Insurance_paragraph,Funding_main_title,Funding_paragraph,Charging_solutions_main_title,Charging_solutions_paragraph,Business_leasing_main_title,Business_leasing_paragraph

    def Clicking_on_a_insurance_button(self):
        Insurance_page, Funding_page, Charging_solutions_page, Business_leasing_page = self.Additional_services_gallery_locators()
        print('Clicking_on_a_insurance_button start')
        self.driver.implicitly_wait(10)
        Base.scrolling(self, Insurance_page)
        Insurance_page.click()
        Base.long_waiting(self)
        expected_Insurance_page_url = 'https://freesbe.com/insurance-page'
        assert expected_Insurance_page_url in self.driver.current_url
        self.driver.back()
        self.driver.implicitly_wait(10)
        print('Clicking_on_a_insurance_button end')

    def Clicking_on_a_Funding_button(self):
        Insurance_page, Funding_page, Charging_solutions_page, Business_leasing_page = self.Additional_services_gallery_locators()
        print('Clicking_on_a_Funding_button start')
        self.driver.implicitly_wait(10)
        Base.scrolling(self, Funding_page)
        Funding_page.click()
        Base.long_waiting(self)
        expected_Funding_page_url = 'https://freesbe.com/finance'
        assert expected_Funding_page_url in self.driver.current_url
        self.driver.back()
        self.driver.implicitly_wait(10)
        print('Clicking_on_a_Funding_button end')

    def Clicking_on_a_Charging_solutions_button(self):
        Insurance_page, Funding_page, Charging_solutions_page, Business_leasing_page = self.Additional_services_gallery_locators()
        print('Clicking_on_a_Charging_solutions_button start')
        self.driver.implicitly_wait(10)
        Base.scrolling(self, Charging_solutions_page)
        Charging_solutions_page.click()
        Base.long_waiting(self)
        expected_Charging_solutions_page_url = 'https://freesbe.com/charging-solutions'
        assert expected_Charging_solutions_page_url in self.driver.current_url
        self.driver.back()
        self.driver.implicitly_wait(10)
        print('Clicking_on_a_Charging_solutions_button end')

    def Clicking_on_a_Business_leasing_button(self):
        Insurance_page, Funding_page, Charging_solutions_page, Business_leasing_page = self.Additional_services_gallery_locators()
        print('Clicking_on_a_Business_leasing_button start')
        self.driver.implicitly_wait(10)
        Base.scrolling(self, Business_leasing_page)
        Business_leasing_page.click()
        Base.long_waiting(self)
        expected_Business_leasing_page = "https://freesbe.com/business-leasing"
        assert expected_Business_leasing_page in self.driver.current_url
        self.driver.back()
        self.driver.implicitly_wait(10)
        print("Clicking_on_a_Business_leasing_button end")

    def Get_additional_services_texts_and_headers(self):
        Additional_services_main_title, Insurance_main_title, Insurance_paragraph, Funding_main_title, Funding_paragraph, Charging_solutions_main_title, Charging_solutions_paragraph, Business_leasing_main_title, Business_leasing_paragraph = self.Get_text_and_header_locators()
        print('Get_additional_services_texts_and_headers start')
        Base.scrolling(self, Additional_services_main_title)
        Main_title_text = Additional_services_main_title.text
        Main_title_font_size = Additional_services_main_title.value_of_css_property('font-size')
        Main_title_color = Additional_services_main_title.value_of_css_property('color')
        expected_main_title_text = 'שירותים נוספים'
        expected_main_title_font_size = '40px'
        expected_main_color = 'rgba(0, 0, 0, 1)'
        assert Main_title_text == expected_main_title_text
        assert Main_title_font_size == expected_main_title_font_size
        assert Main_title_color == expected_main_color
        Insurance_title_text = Insurance_main_title.text
        Insurance_title_font_size = Insurance_main_title.value_of_css_property('font-size')
        Insurance_title_color = Insurance_main_title.value_of_css_property('color')
        expected_insurance_title_text = 'ביטוח'
        expected_insurance_title_font_size = '24px'
        expected_insurance_title_color = 'rgba(0, 0, 0, 1)'
        assert Insurance_title_text == expected_insurance_title_text
        assert Insurance_title_font_size == expected_insurance_title_font_size
        assert Insurance_title_color == expected_insurance_title_color
        Insurance_paragraph_text = Insurance_paragraph.text
        Insurance_paragraph_font_size = Insurance_paragraph.value_of_css_property('font-size')
        Insurance_paragraph_color = Insurance_paragraph.value_of_css_property('color')
        expected_insurance_paragraph_text = 'לא צריך ללכת רחוק, נשווה נבדוק ונתאים את תכנית הביטוח הנכונה עבורך.'
        expected_insurance_paragraph_font_size = '18px'
        expected_insurance_paragraph_color = 'rgba(38, 38, 38, 1)'
        assert Insurance_paragraph_text == expected_insurance_paragraph_text
        assert Insurance_paragraph_font_size == expected_insurance_paragraph_font_size
        assert Insurance_paragraph_color == expected_insurance_paragraph_color
        Funding_title_text = Funding_main_title.text
        Funding_title_font_size = Funding_main_title.value_of_css_property('font-size')
        Funding_title_color = Funding_main_title.value_of_css_property('color')
        expected_funding_title_text = 'מימון וטרייד-אין'
        expected_funding_title_font_size = '24px'
        expected_funding_title_color = 'rgba(0, 0, 0, 1)'
        assert Funding_title_text == expected_funding_title_text
        assert Funding_title_font_size == expected_funding_title_font_size
        assert Funding_title_color == expected_funding_title_color
        Funding_paragraph_text = Funding_paragraph.text
        Funding_paragraph_font_size = Funding_paragraph.value_of_css_property('font-size')
        Funding_paragraph_color = Funding_paragraph.value_of_css_property('color')
        expected_funding_paragraph_text = 'מימון מותאם אישית, טרייד אין או גם וגם - נרכיב לך את המסלול הכי נוח.'
        expected_funding_paragraph_font_size = '18px'
        expected_funding_paragraph_color = 'rgba(38, 38, 38, 1)'
        assert Funding_paragraph_text == expected_funding_paragraph_text
        assert Funding_paragraph_font_size == expected_funding_paragraph_font_size
        assert Funding_paragraph_color == expected_funding_paragraph_color
        Charging_solutions_text = Charging_solutions_main_title.text
        Charging_solutions_font_size = Charging_solutions_main_title.value_of_css_property('font-size')
        Charging_solutions_color = Charging_solutions_main_title.value_of_css_property('color')
        expected_charging_solutions_text = 'פתרונות טעינה'
        expected_charging_solutions_font_size = '24px'
        expected_charging_solutions_color = 'rgba(0, 0, 0, 1)'
        assert Charging_solutions_text == expected_charging_solutions_text
        assert Charging_solutions_font_size == expected_charging_solutions_font_size
        assert Charging_solutions_color == expected_charging_solutions_color
        Charging_solutions_paragraph_text = Charging_solutions_paragraph.text
        Charging_solutions_paragraph_font_size = Charging_solutions_paragraph.value_of_css_property('font-size')
        Charging_solutions_paragraph_color = Charging_solutions_paragraph.value_of_css_property('color')
        expected_charging_solutions_paragraph_text = 'אנחנו בפריסבי כאן לעזור לך עם הרכב החשמלי. מגוון פתרונות טעינה במיוחד בשבילך.'
        expected_charging_solutions_paragraph_font_size = '18px'
        expected_charging_solutions_paragraph_color = 'rgba(38, 38, 38, 1)'
        assert Charging_solutions_paragraph_text == expected_charging_solutions_paragraph_text
        assert Charging_solutions_paragraph_font_size == expected_charging_solutions_paragraph_font_size
        assert Charging_solutions_paragraph_color == expected_charging_solutions_paragraph_color
        Business_leasing_title_text = Business_leasing_main_title.text
        Business_leasing_title_font_size = Business_leasing_main_title.value_of_css_property('font-size')
        Business_leasing_title_color = Business_leasing_main_title.value_of_css_property('color')
        expected_business_leasing_title_text = 'ליסינג עסקי'
        expected_business_leasing_title_font_size = '24px'
        expected_business_leasing_title_color = 'rgba(0, 0, 0, 1)'
        assert Business_leasing_title_text == expected_business_leasing_title_text
        assert Business_leasing_title_font_size == expected_business_leasing_title_font_size
        assert Business_leasing_title_color == expected_business_leasing_title_color
        Business_leasing_paragraph_text = Business_leasing_paragraph.text
        Business_leasing_paragraph_font_size = Business_leasing_paragraph.value_of_css_property('font-size')
        Business_leasing_paragraph_color = Business_leasing_paragraph.value_of_css_property('color')
        expected_business_leasing_paragraph_text = 'ליסינג תפעולי לעסק שלך הכולל חבילות טיפולים ותיקונים, רכב חליפי ועוד.'
        expected_business_leasing_paragraph_font_size = '18px'
        expected_business_leasing_paragraph_color = 'rgba(38, 38, 38, 1)'
        assert Business_leasing_paragraph_text == expected_business_leasing_paragraph_text
        assert Business_leasing_paragraph_font_size == expected_business_leasing_paragraph_font_size
        assert Business_leasing_paragraph_color == expected_business_leasing_paragraph_color
        print(f'{Main_title_text,Main_title_font_size,Main_title_color}')
        print(f'{Insurance_title_text,Insurance_title_font_size,Insurance_title_color,Insurance_paragraph_text,Insurance_paragraph_font_size,Insurance_paragraph_color}')
        print(f'{Funding_title_text,Funding_title_font_size,Funding_title_color,Funding_paragraph_text,Funding_paragraph_font_size,Funding_paragraph_color}')
        print(f'{Charging_solutions_text,Charging_solutions_font_size,Charging_solutions_color,Charging_solutions_paragraph_text,Charging_solutions_paragraph_font_size,Charging_solutions_paragraph_color}')
        print(f'{Business_leasing_title_text,Business_leasing_title_font_size,Business_leasing_title_color,Business_leasing_paragraph_text,Business_leasing_paragraph_font_size,Business_leasing_paragraph_color}')
        return Main_title_text,Main_title_font_size,Main_title_color,Insurance_title_text,Insurance_title_font_size,Insurance_title_color,Insurance_paragraph_text,Insurance_paragraph_font_size,Insurance_paragraph_color,Funding_title_text,Funding_title_font_size,Funding_title_color,Funding_paragraph_text,Funding_paragraph_font_size,Funding_paragraph_color,Charging_solutions_text,Charging_solutions_font_size,Charging_solutions_color,Charging_solutions_paragraph_text,Charging_solutions_paragraph_font_size,Charging_solutions_paragraph_color,Business_leasing_title_text,Business_leasing_title_font_size,Business_leasing_title_color,Business_leasing_paragraph_text,Business_leasing_paragraph_font_size,Business_leasing_paragraph_color