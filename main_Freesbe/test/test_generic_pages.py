from main_Freesbe.Pages.Generic_pages.Header import *

Homepage_url = "https://freesbe.com/"

#Sanity test (move between pages in the Header)

def test_header(driver):
    driver.get(Homepage_url)
    Header = Header_Component(driver)
    Header.Clicking_on_a_New_lobby_button()
    Base.Short_waiting(driver)
    Header.Clicking_on_a_private_leasing_lobby_button()
    Base.Short_waiting(driver)
    Header.Clicking_on_a_Used_lobby_button()
    Base.Short_waiting(driver)
    Header.Move_to_rental_web()
    Base.Short_waiting(driver)
    Header.Clicking_on_a_charging_solutions_button()
    Base.Short_waiting(driver)
    Header.Clicking_on_contact_us_button()
    Base.Short_waiting(driver)
    Header.Clicking_on_wishlist_page()
