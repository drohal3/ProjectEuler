#[35] Dominik Rohal 27.11.2016


# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
#
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#
# How many circular primes are there below one million?

def jePrvocislo(cislo):
    for k in range(2, int(cislo ** (1 / 2)) + 1):
        if (cislo % k == 0):
            return False
    return True


def dajPrvocislo(vacsieAko):
    cislo = vacsieAko
    while True:
        cislo += 1
        if (jePrvocislo(cislo)): return cislo

#print(str(dajPrvocislo(20)))

def spusti():
    cirPrvocisla = set()

    prvocislo = dajPrvocislo(7)
    while (prvocislo < 1000000):
        prvoc = prvocislo
        #jeC = True
        prvocislaP = list()
        for k in range(len(str(prvocislo))):
            prvoc = int(str(prvoc%10) + str(prvoc//10))
            if (not jePrvocislo(prvoc)): break
            else:
                prvocislaP.append(prvoc)
                if (k == len(str(prvocislo)) - 1):
                    for p in prvocislaP:
                        cirPrvocisla.add(p)

        prvocislo = dajPrvocislo(prvocislo)
    return(len(cirPrvocisla) + 4) #4 jednociferne

print("-->" + str(spusti()))


