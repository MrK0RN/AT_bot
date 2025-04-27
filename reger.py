
from google_search import search_google
from auto_reg import auto_reg
from data_gen import gen

def main():
    import driver
    google = driver.Driver()
    google.driver_start()
    driver = google.driver
    driver.implicitly_wait(10)
    search_google(driver, "Author Today", 1)
    auto_reg(driver, gen())


while True:
    try:
        main()
    except Exception:
        pass
