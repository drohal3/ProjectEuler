from setuptools.command.easy_install import easy_install
import math

def minPrvocislo(cislo):
    assert cislo > 2
    for k in range (2, int(math.sqrt(cislo)) + 1):
        if (cislo % k == 0):
            return k

    return cislo


def najdi(n=600851475143):
    n2 = n

    while True:
        prvocislo = minPrvocislo(n2)
        if prvocislo < n2:
            n2 = n2 // prvocislo
        else:
            return n2

print("Vysledkom je: " + str(najdi()))
