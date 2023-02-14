#[63] Dominik Rohal 26.11.2016 pozn. nie stastne riesenie
from math import log10

# def spusti():
#     cislo = 0
#     pocet = 0
#     while True:
#         dlzka = len(str(cislo))
#         zkl = cislo**(1/dlzka)
#         if (float(zkl).is_integer()):
#             pocet += 1
#             print("+ " + str(zkl) + "na" + str(dlzka) + " = " + str(cislo) + " == " + str(pocet))
#
#         cislo += 1
#


def spusti():
    pocet = 0
    for n in range(1, 10):
        pocet += int(1 / (1 - log10(n)))
    return pocet

print("vysledok =" + str(spusti()))
