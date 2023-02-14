#[46] Dominik Rohal 27. 11. 2016
#https://projecteuler.net/problem=46

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

def spusti():
    cislo = 9
    while True:
        if (not jePrvocislo(cislo)):
            prvoc = 2
            while True:
                if (float(((cislo - prvoc)/2)**(1/2)).is_integer()):
                    print("#" + str(cislo) + " |X|")
                    break
                prvoc = dajPrvocislo(prvoc)
                if (prvoc>cislo): return cislo
        cislo += 2

print("-->" + str(spusti()))