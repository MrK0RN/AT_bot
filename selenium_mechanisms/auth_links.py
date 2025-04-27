import login
import support.data_operate
from data import read_mail
from support import timer

def save_links():
    g = read_mail.get_links()

    print("ready")
    support.data_operate.load_links(g)

#save_links()
def auth_links():
    import driver
    driver = driver.Driver()
    driver.driver_start()
    g = support.data_operate.parse_links()
    for i in g:
        driver.driver.get(g[i][1])
        timer.sleep(1)
        z = support.data_operate.parse_links(g[i][0])
        login.clear_login(driver.driver, (i, z[1]), mail=True)
        timer.sleep(1)

