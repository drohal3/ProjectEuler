#[12]
# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# Let us list the factors of the first seven triangle numbers:
#
#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.
#
# What is the value of the first triangle number to have over five hundred divisors?

def pocetDelitelov(cislo):
    pocet = 1
    delitel = 2
    medziv = 0
    cisl = cislo
    while True:
        if (cisl % delitel == 0):
            medziv += 1
            cisl /= delitel
        else:
            delitel += 1
            pocet *= (medziv + 1)
            medziv = 0
            if (cisl == 1):
                break
    # pocet = 1 # lebo aj same sebou
    # for k in range(1, cislo // 2 + 1):
    #     if(cislo % k == 0):
    #         pocet += 1
    print(str(cislo) + " |==| " + str(pocet))
    return pocet

print(str(pocetDelitelov(28)))

def hladaj():

    tNumber = 1
    cislo = 2
    while True:
        if (pocetDelitelov(tNumber) > 500):
            return tNumber
        tNumber += cislo
        cislo += 1

print(int(hladaj()))


