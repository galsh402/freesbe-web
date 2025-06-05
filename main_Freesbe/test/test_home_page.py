from main_Freesbe.Pages.Home_page.Hero import *
#from main_Freesbe.Pages.Home_page.Banner_gallery import *
from main_Freesbe.Pages.Home_page.Search_flow import *
from main_Freesbe.Pages.Home_page.Additional_services import *
from main_Freesbe.Pages.Home_page.Contact_us import *
from main_Freesbe.Pages.Home_page.Blog import *

Homepage_url = "https://freesbe.com/"

#Sanity test (move between lobby pages)

def test_hero(driver):
    driver.get(Homepage_url)
    Hero = Hero_Component(driver)
    Hero.Clicking_on_a_New_lobby_button()
    driver.implicitly_wait(2)
    Hero.Clicking_on_a_private_leasing_lobby_button()
    driver.implicitly_wait(2)
    Hero.Clicking_on_a_Used_lobby_button()
    driver.implicitly_wait(2)
    Hero.Move_to_rental_web()

#Sanity test (Verify the banner gallery)

#def test_banner_gallery(driver):
#    driver.get(Homepage_url)
#    Gallery = Banner_gallery_Component(driver)
#    Gallery.verify_Banner_carousel()
#    Base.Short_waiting(driver)


#Sanity test (scroll and move to search flow pages)

def test_Search_flow(driver):
    driver.get(Homepage_url)
    Search = Search_flow_Component(driver)
    driver.implicitly_wait(2)
    Search.Clicking_on_a_monthly_price()
    driver.implicitly_wait(2)
    Search.Clicking_on_a_accurate_Search()
    driver.implicitly_wait(2)
    Search.Clicking_on_a_general_Search()

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

#Sanity test (scroll to contact us component and verify text & phone number)

def test_component_contact_us(driver):
    driver.get(Homepage_url)
    Contact_us = Contact_Us_Component(driver)
    Contact_us.Clicking_on_a_contact_us_button()

#Sanity test (scroll dwon and open the blog page)

#def test_blog_component(driver):
#    driver.get(Homepage_url)
#    Blog_page = Blog_Component(driver)
#    Blog_page.navigate_to_blog_page()
#    driver.implicitly_wait(2)