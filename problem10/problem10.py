from setuptools.command.easy_install import easy_install
import math

def jePrvocislo(cislo):

    for k in range (2, int(math.sqrt(cislo)) + 1):
        if (cislo % k == 0 and cislo != k and cislo != 1):
            return False
    print(str(cislo) + " je prvocislo")
    return True

def spusti(hranica = 2000000):
    sucet = 0
    a = 1
    while True:
        a += 1
        if (a >= hranica):
            return sucet
        if jePrvocislo(a):
            sucet += a

print(str(spusti()))


