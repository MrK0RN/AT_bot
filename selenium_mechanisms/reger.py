import data.postgress
import selenium_mechanisms.login
from selenium_mechanisms.google_search import search_google
from selenium_mechanisms.auto_reg import auto_reg
from support import timer
from support.data_gen import gen

def main():
    from selenium_mechanisms import driver
    google = driver.Driver()
    google.driver_start()
    driver = google.driver
    driver.implicitly_wait(10)
    search_google(driver, "Author Today", 1)
    auto_reg(driver, gen())

def check_of_auth(login, password):
    from selenium_mechanisms import driver
    driver = driver.Driver()
    driver.driver_start()
    driver = driver.driver
    driver.implicitly_wait(10)
    search_google(driver, "Author Today", 1)
    selenium_mechanisms.login.login(driver, (login, password))
    timer.sleep(100)


while True:
    try:
        check_of_auth()
    except Exception:
        pass
