from support import timer
from support.printer import printer, key_press
from pynput.keyboard import Key
from selenium.webdriver.common.by import By



def search_google(driver, query, num_result):
    driver.get("https://google.com")
    timer.sleep(1)
    text_box = driver.find_element(by=By.ID, value="APjFqb")
    driver.implicitly_wait(0.2)
    printer(query)
    key_press(Key.enter)
    timer.sleep(30)
    t = driver.find_elements(by=By.CSS_SELECTOR, value='h3')

    t[num_result-1].click()