import data.postgress
import selenium_mechanisms.login
from selenium_mechanisms.google_search import search_google
from selenium_mechanisms.auto_reg import auto_reg
from support import timer
from support.data_gen import gen
from support.data_operate import get_accounts


def main():
    from selenium_mechanisms import driver
    google = driver.Driver()
    google.driver_start()
    driver = google.driver
    driver.implicitly_wait(10)
    search_google(driver, "Author Today", 1)
    auto_reg(driver, gen())

def check_of_auth(login, password):
    print(1)
    from selenium_mechanisms import driver
    print("er2")
    driver = driver.Driver()
    driver.driver_start()
    driver = driver.driver
    driver.implicitly_wait(10)
    print(1)
    search_google(driver, "Author Today", 1)
    selenium_mechanisms.login.login(driver, (login, password))
    timer.sleep(100)

def check_auth():
    accs = get_accounts()
    for acc in accs:
        email, password = acc[2], acc[3]
        check_of_auth(email, password)
while True:
    check_auth()
