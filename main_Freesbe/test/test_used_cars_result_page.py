from main_Freesbe.Pages.Used_cars_result_page.Results_page import *

Used_car_result_page_url = "https://freesbe.com/used-car-for-sale/listings"


def test_car_count(driver):
    driver.get(Used_car_result_page_url)
    Used_car = Used_car_results_Component(driver)
    car_count = Used_car.get_car_count()
    if car_count < 1000:
        print(f" Test Failed: Found {car_count} cars, which is less than 1000")
    else:
        print(f"Test Passed: Found {car_count} cars, which is 1000 or more.")