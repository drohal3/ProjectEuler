from setuptools.command.easy_install import easy_install
def zistiDelitelnost(cislo):
    for k in range (19):
        if(cislo % (k + 2) != 0): # +2 lebo nulou sa nedeli a 1 nema vyznam skusat
            return 0 #false
    return 1    #true

def najdi():
    cislo = 285 #nasobok 19
    najdenych = 0

    while (najdenych == 0):
        delitenlost = zistiDelitelnost(cislo)
        if (delitenlost == 1):
            najdenych = najdenych + 1
        else:
            cislo = cislo + 19 #19 je najvacsie prvocislo < 20
    return cislo

print("Najmensie cislo delitlne 1 az 20 je:" + str(najdi()))