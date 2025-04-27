import json

import driver
import login
from data import read_mail
from support import timer


def save_links():
    g = read_mail.get_links()
    print("ready")
    with open("../temp/autLinks.json", "w") as f:
        json.dump(g, f)

#save_links()

with open("../temp/autLinks.json", "r") as f:
    g = json.load(f)
    print(type(g))

print(g)
driver = driver.Driver()
driver.driver_start()
h = {}
with open("../temp/accs", "r") as f:
    lines = f.read().split("\n")
for i in lines:
    print(i)
    z = i.split("|")
    h[z[1]] = z[2]
for i in g:
    driver.driver.get(g[i])
    timer.sleep(1)
    login.clear_login(driver.driver, (i, h[i]), mail=True)
    timer.sleep(1)

