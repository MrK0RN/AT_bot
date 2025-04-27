from selenium.webdriver.common.by import By

from selenium_mechanisms.clcker import clicker
from support.printer import printer
from support import timer


def clear_login(driver, nmp, mail):
    mail, password = nmp
    timer.sleep(2)
    driver.find_elements(by=By.NAME, value='Login')[0].click()
    clicker(driver, by=By.NAME, value='Login', wait=2, input=mail)
    clicker(driver, by=By.NAME, value='Password', wait=2, input=password)
    if mail:
        clicker(driver, by=By.XPATH, value='/html/body/div[1]/div/section/div/div/div/div[2]/form/button', wait=2)
    else:
        clicker(driver, by=By.XPATH, value='/html/body/div[3]/div/div/div[2]/div/div/div/form[2]/button', wait=2)

def login(driver, nmp):
    mail, password = nmp
    timer.sleep(2)
    clicker(driver, by=By.LINK_TEXT, value='Войти', wait=2)
    clear_login(driver, (mail, password), False)
