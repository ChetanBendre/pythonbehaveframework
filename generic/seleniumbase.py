from selenium import webdriver
import os


def launch_browser_app(browser_name, url):
    global driver
    driver_path = os.getcwd()
    if browser_name == "chrome":
        driver_path = driver_path + "/drivers/chromedriver.exe"
        driver = webdriver.Chrome(executable_path=driver_path)
    elif browser_name == "firefox":
        driver_path = driver_path + "/drivers/geckodriver.exe"
        driver = webdriver.Firefox(executable_path=driver_path)
    elif browser_name == "ie":
        driver = webdriver.Ie()
    else:
        print("Invalid input ")

    driver.maximize_window()
    driver.get(url)


def close_browser():
    driver.quit()


def identify_element(type, address, flag = False):
    if flag:
        if type == "id":
            return driver.find_elements_by_id(address)
        elif type == "name":
            return driver.find_elements_by_name(address)
        elif type == "tagname":
            return driver.find_elements_by_tag_name(address)
    else:
        if type == "id":
            return driver.find_element_by_id(address)
        elif type == "name":
            return driver.find_element_by_name(address)


def get_page_details(detail_type):
    value_to_be_returned = None
    if detail_type == "url":
        value_to_be_returned = driver.current_url
    return value_to_be_returned
