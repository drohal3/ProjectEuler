from setuptools.command.easy_install import easy_install
import math


def spusti(pocetCisel = 100):
    cislo1 = 0;
    cislo2 = 0;
    for k in  range(1, pocetCisel + 1):
        #print(str(k))
        cislo1 += k * k
        cislo2 += k;
    return (cislo2 * cislo2) - cislo1

print(str(spusti()))