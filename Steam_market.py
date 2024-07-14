from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
number = 1

driver.get(
    'https://steamcommunity.com/market/search?q=&category_570_Hero%5B%5D' +
    '=any&category_570_Slot%5B%5D=any&category_570_Type%5B%5D=any&category' +
    f'_570_Quality%5B%5D=tag_strange&appid=570#p{number}_popular_desc')
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)


def is_element_present_with_search(how, what):
    try:
        wait.until(
            EC.element_to_be_clickable((how, what))
        )
    except (BaseException):
        return False
    return True


def is_element_invisibility(how, what):
    try:
        wait.until(
            EC.invisibility_of_element_located((how, what))
        )
    except (BaseException):
        return False
    return True


inscribed_name = (
    'xpath', "//span[@class='market_listing_item_name']")
inscribed_price = (
    'xpath', "//span[@class='normal_price']")
names = driver.find_elements(
    'xpath', "//span[@class='market_listing_item_name']")
prices = driver.find_elements(
    'xpath', "//span[@class='normal_price']")
error = (
    'xpath', "//div[contains(text(), 'Ошибка поиска.')]")

name_items = []
price_items = []
result_list = []
name_items_2 = []
price_items_2 = []
result_list_2 = []


def check_page(name_items, price_items):
    try:
        assert is_element_invisibility(
            'xpath', "//div[contains(text(), 'Ошибка поиска.')]")
        assert is_element_present_with_search(*inscribed_price)
        if is_element_invisibility(*error) is not True:
            while is_element_invisibility(*error) is True:
                time.sleep(1)
                driver.refresh()
                is_element_invisibility(
                    'xpath', "//div[contains(text(), 'Ошибка поиска.')]")
        driver.find_element(
            'xpath', "//span[@id='result_0_name']")
        driver.find_element(
            'xpath', "//span[@id='result_0_name']")
        for i in range(len(names)):
            name_items.append(f'{names[i].text}')
            price_items.append(f'{prices[i].text}')
            name_items_2.append(name_items[i].replace('Inscribed ', ''))
            result_list.append(f'{names[i].text} СТОИТ {prices[i].text}')
        return name_items_2, result_list
    except (BaseException):
        print('Ошибка при считывании страницы')
        return False


def search_items(result_list, name_items_2, result_list_2):
    try:
        driver.get(
            'https://steamcommunity.com/market/search?category_570_' +
            'Hero%5B0%5D=any&category_570_Slot%5B0%5D=any&category_' +
            '570_Type%5B0%5D=any&appid=570')
        for i in range(len(name_items)):
            is_element_present_with_search(
                'xpath', "//input[@type='text']/..")
            search_field = driver.find_element(
                'xpath', "//input[@type='text']/..")
            search_field.click
            is_element_present_with_search(
                'xpath', "//input[@type='text']")
            input_field = driver.find_element(
                'xpath', "//input[@type='text']")
            input_field.click()
            input_field.send_keys(Keys.CONTROL + 'a')
            input_field.send_keys(Keys.DELETE)
            input_field.send_keys(name_items_2[i])
            input_field.send_keys(Keys.ENTER)
            if is_element_invisibility(*error) is not True:
                while is_element_invisibility(*error) is True:
                    input_field = driver.find_element(
                        'xpath', "//input[@type='text']")
                    input_field.send_keys(Keys.ENTER)
                    is_element_invisibility(
                        'xpath', "//div[contains(text(), 'Ошибка поиска.')]")
                    is_element_present_with_search(
                        'xpath', "//span[@id='result_0_name']")
            is_element_present_with_search(
                'xpath', "//span[@id='result_0_name']")
            is_element_present_with_search(
                'xpath', "//div[contains(@class, 'market_listing_right_cell" +
                " market_listing_their_price market_sortable_column')]")
            sort = driver.find_element(
                'xpath', "//div[contains(@class, 'market_listing_right_cell" +
                " market_listing_their_price market_sortable_column')]")
            sort.click()
            is_element_present_with_search(
                'xpath', "//span[@id='result_0_name']")
            prices_2 = driver.find_elements(
                'xpath', "//span[@class='normal_price']")
            price_items_2.append(f'{prices_2[0].text}')
            is_element_present_with_search(
                'xpath', "//span[@id='result_0_name']")
            result_list_2.append(f'ОБЫЧНЫЙ СТОИТ {prices_2[0].text}')
            print(f'{result_list[i]} {result_list_2[i]}')
        return result_list_2
    except (BaseException):
        print('Ошибка при поиске предметов')
        return result_list_2, False


def result(result_list_2, result_list):
    for i in range(len(result_list)):
        print(f'{result_list[i]} {result_list_2[i]}')


check_page(name_items, price_items)
search_items(result_list, name_items_2, result_list_2)
result(result_list_2, result_list)
