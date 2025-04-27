from selenium.webdriver.common.by import By

from selenium_mechanisms.clcker import clicker

from support import timer
from support.printer import printer


def auto_reg(driver, nmp):
    name, mail, password = nmp
    clicker(driver, by=By.LINK_TEXT, value='Войти', wait=2)
    clicker(driver, by=By.LINK_TEXT, value='Зарегистрироваться', wait=2)
    timer.sleep(25)
    clicker(driver, by=By.NAME, value='FIO', wait=0.6, input=name)
    clicker(driver, by=By.NAME, value='Email', wait=0.6, input=mail)
    clicker(driver, by=By.NAME, value='Password', wait=0.6, input=password)
    clicker(driver, by=By.XPATH, value=r"/html/body/div[1]/div/section/div/div/div/div[2]/form[1]/button", wait=0.6)

    timer.sleep(4)
    driver.driver_quit()