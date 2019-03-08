from selenium import webdriver
from selenium.webdriver.support.select import Select
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
        elif type == "linktext":
            return driver.find_element_by_link_text(address)
        elif type == "css":
            return driver.find_element_by_css_selector(address)


def get_page_details(detail_type):
    value_to_be_returned = None
    if detail_type == "url":
        value_to_be_returned = driver.current_url
    return value_to_be_returned


def select_value_from_dropdown(element, select_by, value):
    select = Select(element)
    #sel = Select(driver.find_element_by_id("dropdown"))
    if select_by == 'index':
        select.select_by_index(int(value))
    elif select_by == 'value':
        select.select_by_value(value)
    elif select_by == 'visibletext':
        select.select_by_visible_text(value)


def switch_to_another_window(window_title):

    parent_handle = driver.current_window_handle
    handles = driver.window_handles
    print(type(handles))

    for handle in handles:
        if parent_handle != handle:
            driver.switch_to.window(handle)
            current_title = driver.title
            if current_title == window_title:
                break
            else:
                continue

def switch_to_another_frame():
    driver.switch_to.frame("frame-top")
    driver.switch_to.frame("frame-middle")
    driver.switch_to.frame("frame-top")



def perform_action(action_type, element, value=None):
    value_to_be_returned = None
    if action_type == "click":
        element.click()
    if action_type == 'gettext':
        value_to_be_returned = element.text

    return value_to_be_returned


def handle_alert_popup(action_type, value):
    alert_obj = driver.switch_to.alert
    if action_type == 'accept':
        alert_obj.accept()
    elif action_type == 'dismiss':
        alert_obj.dismiss()
    elif action_type == 'settext':
        alert_obj.send_keys(value)


def capture_screenshot(filename):
    driver.save_screenshot(filename)

