import random

alph = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"


def gen(length):
    passw = ""
    for _ in range(length - 2):
        passw += alph[int(len(alph) * random.random())]
    passw += str(int(10 ** random.random()))
    passw += str(int(10 ** random.random()))
    return passw
