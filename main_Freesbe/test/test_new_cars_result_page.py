from main_Freesbe.Pages.New_cars_result_page.Results_page import *

New_car_result_page_url = "https://freesbe.com/new-car-for-sale/listings"


def test_car_count(driver):
    driver.get(New_car_result_page_url)
    Used_car = New_car_results(driver)
    car_count = Used_car.get_car_count()
    if car_count < 10:
        print(f" Test Failed: Found {car_count} cars, which is less than 10")
    else:
        print(f"Test Passed: Found {car_count} cars, which is 19 or more.")


def test_filters(driver):
    driver.get(New_car_result_page_url)
    Search_filters = New_car_results(driver)
    Search_filters.click_and_verify_manufacturers_filter()