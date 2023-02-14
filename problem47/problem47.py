#[47]
# The first two consecutive numbers to have two distinct prime factors are:
#
# 14 = 2 × 7
# 15 = 3 × 5
#
# The first three consecutive numbers to have three distinct prime factors are:
#
# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.
#
# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
import math
import primes

def jePrvocislo(cislo):
    for k in range(2, int(math.sqrt(cislo)) + 1):
        if (cislo % k == 0):
            return False
    return True

def dalsiePrvocislo(vacsieAko):
    nadejne = vacsieAko
    while True:
        nadejne += 1
        if (jePrvocislo(nadejne)):
            return nadejne


#print(str(dalsiePrvocislo(5)))
F = primes.RangeFactor(150000)
S = primes.Sieve(150000)

def pocetPrvocDelitelov(cislo):
    # cisl = cislo
    # prvocislo = 2
    # delitele = set()
    # while True:
    #     if (cisl % prvocislo == 0):
    #         cisl /= prvocislo
    #         delitele.add(prvocislo)
    #     else:
    #         prvocislo = dalsiePrvocislo(prvocislo)
    #         if (cisl == 1):
    #             print(str(cislo) + " {==} " + str(delitele))
    #             return len(delitele)

    delitele = F.factors[cislo]
    #print(str(delitele))
    pocet = 0
    for delitel in delitele:
        if (jePrvocislo(delitel)): pocet += 1
    return pocet


print("#" + str(pocetPrvocDelitelov(15)))

def najdi():
    pocet = 0
    #cislo = 134000
    cislo = 2*3*5*7
    posledne = 0
    while True:
        if (pocetPrvocDelitelov(cislo) == 4):
            pocet += 1
            if (pocet == 4):
                return posledne
            if (pocet == 1): # malo pri 0, ale uz som 1 pridal
                posledne = cislo
        else:
            pocet = 0

        cislo += 1

print("-->" + str(najdi()))
