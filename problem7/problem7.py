from setuptools.command.easy_install import easy_install
import math

def jePrvocislo(cislo):
    assert cislo >= 2

    for k in range (2, int(math.sqrt(cislo)) + 2):
        #if (k == 2):
         #   print("rozsah je: " + str(int(math.sqrt(cislo))))


        if ((cislo % k) == 0 and cislo != k):
            return False
    return True

def najdiPrvocislo(poradie = 10001):
    cislo = 2
    pocet = 0
    while True:
        if (jePrvocislo(cislo)):
            pocet += 1
            print("prvocislo v poradi " + str(pocet) + "je: " + str(cislo))
            if (pocet == poradie):
                return cislo
            else:
                cislo += 1
        else:
            cislo += 1


print("vysledne prvocislo je: " + str(najdiPrvocislo()))