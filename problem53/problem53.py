#[53]Dominik Rohal 27.11.2016

def faktorial(cislo):
    cisl = cislo
    vrat = 1
    while cisl > 0:
        vrat*= cisl
        cisl -= 1
    return vrat

def spusti():
    pocet = 0
    for n in range (3,100 + 1):
        for r in range (3, n + 1):
            if (faktorial(n)/(faktorial(r)*faktorial(n-r)) > 1000000): pocet += 1
    return pocet

print("-->" + str(spusti()))