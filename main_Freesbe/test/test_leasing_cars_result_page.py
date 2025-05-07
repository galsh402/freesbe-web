from main_Freesbe.Pages.Leasing_cars_result_page.Results_page import *

Leasing_car_result_page_url = "https://freesbe.com/private-leasing/listings"


def test_car_count(driver):
    driver.get(Leasing_car_result_page_url)
    Used_car = Leasing_car_results_Component(driver)
    car_count = Used_car.get_car_count()
    if car_count < 20:
        print(f" Test Failed: Found {car_count} cars, which is less than 20")
    else:
        print(f"Test Passed: Found {car_count} cars, which is 30 or more.")