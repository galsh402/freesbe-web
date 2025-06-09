from main_Freesbe.Pages.Generic_pages.Header import *

Homepage_url = "https://freesbe.com/"

#Sanity test (move between pages in the Header)

def test_header(driver):
    driver.get(Homepage_url)
    Header = Header_Component(driver)
    Header.Clicking_on_a_New_lobby_button()
    driver.implicitly_wait(2)
    Header.Clicking_on_a_private_leasing_lobby_button()
    driver.implicitly_wait(2)
    Header.Clicking_on_a_Used_lobby_button()
    driver.implicitly_wait(2)
    Header.Move_to_rental_web()
    driver.implicitly_wait(2)
    Header.Clicking_on_a_charging_solutions_button()
    driver.implicitly_wait(2)
    Header.Clicking_on_contact_us_button()
    driver.implicitly_wait(2)
    Header.Clicking_on_wishlist_page()
