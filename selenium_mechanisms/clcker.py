from support import timer
from support.printer import printer

def clicker(driver, by, value, wait, input=None):
    t = driver.find_elements(by=by, value=value)
    timer.sleep(wait)
    if len(t):
        t[0].click()
    else:
        print("Такого элемента не найдено!!")
    if input:
        printer()