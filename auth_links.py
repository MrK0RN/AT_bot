import time

import driver
import read_mail

g = read_mail.get_links()
driver = driver.Driver()
driver.driver_start()
for i in g:
    print(i)
    driver.driver.get(i)
    time.sleep(10)