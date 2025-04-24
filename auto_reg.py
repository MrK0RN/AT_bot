import time

from selenium.webdriver.common.by import By

import timer
from printer import printer


def auto_reg(driver, nmp):
    name, mail, password = nmp
    timer.sleep(2)
    t = driver.find_elements(by=By.LINK_TEXT, value='Войти')
    timer.sleep(1)
    t[0].click()
    timer.sleep(1)
    t = driver.find_elements(by=By.LINK_TEXT, value='Зарегистрироваться')
    timer.sleep(1)
    t[0].click()
    timer.sleep(10)
    driver.find_elements(by=By.NAME, value='FIO')[0].click()
    printer(name)
    timer.sleep(0.6)
    driver.find_elements(by=By.NAME, value='Email')[0].click()
    printer(mail)
    timer.sleep(0.6)
    driver.find_elements(by=By.NAME, value='Password')[0].click()
    printer(password)
    timer.sleep(0.6)
    driver.find_elements(by=By.XPATH, value=r"/html/body/div[1]/div/section/div/div/div/div[2]/form[1]/button")[0].click()
    timer.sleep(4)
    driver.driver_quit()