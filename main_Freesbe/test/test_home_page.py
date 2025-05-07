from main_Freesbe.Pages.Home_page.Hero import *
from main_Freesbe.Pages.Home_page.Banner_gallery import *
from main_Freesbe.Pages.Home_page.Search_flow import *
from main_Freesbe.Pages.Home_page.Additional_services import *
from main_Freesbe.Pages.Home_page.Contact_us import *
from main_Freesbe.Pages.Home_page.Blog import *

Homepage_url = "https://freesbe.com/"

#UI test + Sanity test (move between lobby pages)

def test_hero(driver):
    driver.get(Homepage_url)
    Hero = Hero_Component(driver)
    Hero.Clicking_on_a_New_lobby_button()
    Base.long_waiting(driver)
    Hero.Clicking_on_a_private_leasing_lobby_button()
    Base.long_waiting(driver)
    Hero.Clicking_on_a_Used_lobby_button()
    Base.long_waiting(driver)
    Hero.Move_to_rental_web()
    font_size_H1, H1_color, font_size_H2, H2_color, rental_link_font_size, rental_link_color, main_title, subtitle, rental_link_text = Hero.Get_hero_texts_and_headers()
    expected_font_size_h1 = '60px'
    assert expected_font_size_h1 == font_size_H1
    expected_H1_color = 'rgba(0, 0, 0, 1)'
    assert expected_H1_color == H1_color
    expected_font_size_h2 = '24px'
    assert expected_font_size_h2 == expected_font_size_h2
    expected_H2_color = 'rgba(38, 38, 38, 1)'
    assert expected_H2_color == H2_color
    expected_H1_text = "כל מה שרכב, רק תבחרו"
    assert expected_H1_text == main_title
    expected_H2_text = "היי, אנחנו freesbe ואצלנו יש הכל: רכבים חדשים, יד שנייה, ליסינג, השכרה, מימון, ביטוח וחיוך. אז איזה רכב מתאים לך?"
    assert expected_H2_text == subtitle
    expected_rental_link_font_size = '18px'
    assert expected_rental_link_font_size == rental_link_font_size
    expected_rental_link_color = 'rgba(0, 0, 238, 1)'
    assert expected_rental_link_color == rental_link_color
    expected_rental_link_text = 'מחפשים רכב להשכרה'
    assert expected_rental_link_text == rental_link_text
    print(f'The UI of the main title: {font_size_H1, H1_color, main_title}')
    print(f'the UI of the second main title is: {font_size_H2, H2_color, subtitle}')
    print(f'the rental link UI is: {rental_link_font_size, rental_link_color, rental_link_text}')


#Sanity test (Verify the banner gallery)

def test_banner_gallery(driver):
    driver.get(Homepage_url)
    Gallery = Banner_gallery_Component(driver)
    Gallery.verify_Banner_carousel()
    Base.Short_waiting(driver)


#UI test + Sanity test (scroll and move to search flow pages)

def test_Search_flow(driver):
    driver.get(Homepage_url)
    Search = Search_flow_Component(driver)
    driver.implicitly_wait(2)
    Search.Clicking_on_a_budget_button()
    driver.implicitly_wait(2)
    Search.Clicking_on_a_accurateSearch_button()
    driver.implicitly_wait(2)
    Search.Clicking_on_a_leave_details_button()
    driver.implicitly_wait(2)
    Search.Clicking_on_a_general_Search_button()
    first_main_title_text, first_main_title_font_size, first_title_color, second_main_title_text, second_main_title_font_size, second_main_title_color, paragraph_text, paragraph_font_size, paragraph_color = Search.Get_search_flow_texts_and_headers()
    expected_first_main_title_text = 'חפשו איך שנוח'
    assert first_main_title_text == expected_first_main_title_text
    expected_first_main_title_font_size = '40px'
    assert first_main_title_font_size == expected_first_main_title_font_size
    expected_first_title_color = 'rgba(0, 0, 0, 1)'
    assert first_title_color == expected_first_title_color
    expected_second_main_title_text = 'מתלבטים מה לקנות?'
    assert second_main_title_text == expected_second_main_title_text
    expected_second_main_title_font_size = '40px'
    assert second_main_title_font_size == expected_second_main_title_font_size
    expected_second_main_title_color = 'rgba(38, 38, 38, 1)'
    assert second_main_title_color == expected_second_main_title_color
    expected_paragraph_text = 'ענו על 3 שאלות זריזות ואנחנו נמצא לכם רכבים שיכולים להתאים'
    assert paragraph_text == expected_paragraph_text
    expected_paragraph_font_size = '18px'
    assert paragraph_font_size == expected_paragraph_font_size
    expected_paragraph_color = 'rgba(38, 38, 38, 1)'
    assert paragraph_color == expected_paragraph_color
    print(f'The UI of the main title:{first_main_title_text, first_main_title_font_size, first_title_color}')
    print(f'the UI of the second main title is:{second_main_title_text, second_main_title_font_size, second_main_title_color}')
    print(f'the UI of the paragraph is:{paragraph_text, paragraph_font_size, paragraph_color}')


#UI test + Sanity test (scroll and move to additional services pages)

def test_Additional_services(driver):
    driver.get(Homepage_url)
    Additional_pages = Additional_services_Component(driver)
    Additional_pages.Clicking_on_a_insurance_button()
    driver.implicitly_wait(2)
    Additional_pages.Clicking_on_a_Funding_button()
    driver.implicitly_wait(2)
    Additional_pages.Clicking_on_a_Charging_solutions_button()
    driver.implicitly_wait(2)
    Additional_pages.Clicking_on_a_Business_leasing_button()


def test_Get_additional_services_UI(driver):
    driver.get(Homepage_url)
    Additional_UI = Additional_services_Component(driver)
    Additional_UI.Get_additional_services_texts_and_headers()


#Sanity test (scroll to contact us component and verify text & phone number)

def test_component_contact_us(driver):
    driver.get(Homepage_url)
    Contact_us = Contact_Us_Component(driver)
    Contact_us.Clicking_on_a_contact_us_button()
    main_title_text, main_title_font_size, main_title_color, paragraph_text, paragraph_font_size, paragraph_color = Contact_us.get_contact_us_texts_and_headers()
    expected_Contact_us_main_title_text = 'צריכים עזרה? דברו איתנו'
    assert expected_Contact_us_main_title_text == main_title_text
    expected_Contact_us_main_title_font_size = '24px'
    assert expected_Contact_us_main_title_font_size == main_title_font_size
    expected_Contact_us_main_title_color = 'rgba(38, 38, 38, 1)'
    assert expected_Contact_us_main_title_color == main_title_color
    expected_Contact_us_paragraph_text = 'רוצים לדעת עוד? עקבו אחרי הטיפים שלנו באתר ואל תתביישו ליצור איתנו קשר'
    assert expected_Contact_us_paragraph_text == paragraph_text
    expected_Contact_us_paragraph_font_size = '16px'
    assert expected_Contact_us_paragraph_font_size == paragraph_font_size
    expected_Contact_us_paragraph_color = 'rgba(38, 38, 38, 1)'
    assert expected_Contact_us_paragraph_color == paragraph_color
    print(f'The UI of the main title:{main_title_text, main_title_font_size, main_title_color}')
    print(f'the UI of the paragraph is{paragraph_text, paragraph_font_size, paragraph_color}')


#Sanity test (scroll dwon and open the blog page)

def test_blog_component(driver):
    driver.get(Homepage_url)
    Blog_page = Blog_Component(driver)
    Blog_page.navigate_to_blog_page()
    driver.implicitly_wait(2)