#[4]
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
# 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.
#def osekavac(velkost):
#    osekavac = '1'
#    for k in range(velkost):
#        osekavac += '0'
#    return int(osekavac)

def jePalindrom(cislo):
    cisl = cislo
    for k in range(len(str(cislo)) // 2):
        cisloS = str(cislo)
        dlzka = len(str(cislo))
        lava = cisloS[k]
        prava = cisloS[dlzka - k - 1]
        if (prava != lava):
            return False

    return True
print(str(jePalindrom(900099)))

def najdi():
    najvacsi = 0
    for k in range (100, 1000):
        for l in range (100, 1000):
            if (k*l > najvacsi and jePalindrom(k*l)):
                najvacsi = k*l
    return najvacsi

#print(str(len(str(245))))
print(str(najdi()))