from setuptools.command.easy_install import easy_install
import math

def spusti(cislo = 1000):
    sucet = 0
    for k in range (1, cislo + 1):
        b = k
        for l in range(k - 1):
            b *= k
        sucet += b
        print(str(k) + " = " + str(sucet))
    return sucet


def vypisPoslednychDesat(cislo):
    print(str(cislo % 10000000000))

print("#" + str(spusti()) + "#")
vypisPoslednychDesat(spusti())