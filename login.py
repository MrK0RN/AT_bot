import time

from selenium.webdriver.common.by import By

from printer import printer
import timer

def clear_login(driver, nmp, mail):
    mail, password = nmp
    timer.sleep(2)
    driver.find_elements(by=By.NAME, value='Login')[0].click()
    timer.sleep(2)
    printer(mail)
    timer.sleep(0.5)
    driver.find_elements(by=By.NAME, value='Password')[0].click()
    timer.sleep(1)
    printer(password)
    timer.sleep(2)
    if mail:
        driver.find_elements(by=By.XPATH, value='/html/body/div[1]/div/section/div/div/div/div[2]/form/button')[0].click()
    else:
        driver.find_elements(by=By.XPATH, value='/ html / body / div[3] / div / div / div[2] / div / div / div / form[2] / button')[0].click()
    #/ html / body / div[3] / div / div / div[2] / div / div / div / form[2] / button
    #/html/body/div[1]/div/section/div/div/div/div[2]/form/button

def login(driver, nmp):
    mail, password = nmp
    timer.sleep(2)
    t = driver.find_elements(by=By.LINK_TEXT, value='Войти')
    timer.sleep(1)
    t[0].click()
    clear_login(driver, (mail, password), False)
