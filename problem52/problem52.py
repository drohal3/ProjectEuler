#[52] Dominik Rohal 26.11.2016

# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
#
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

def spusti():
    cislo = 100
    while True:
        dalsie = True
        if (len(str(1*cislo)) == len(str(2*cislo)) and len(str(2*cislo)) == len(str(3*cislo)) and len(str(3*cislo)) == len(str(4*cislo)) and len(str(4*cislo)) == len(str(5*cislo)) and len(str(5*cislo)) == len(str(6*cislo))):
            #cislice = list()
            cisl = cislo #index je cislica, hodnota je vyskyt
            cislice = list([0] * 10)
            while cisl > 0:
                cislice[cisl%10] = cislice[cisl%10] + 1
                cisl //= 10
            for k in range(2,6+1):
                cisliceP = list([0] * 10)
                cisl = cislo * k

                while cisl > 0:
                    cisliceP[cisl % 10] = cisliceP[cisl % 10] + 1
                    if(cisliceP[cisl % 10] > cislice[cisl%10]):
                        dalsie = False
                        break
                    cisl //= 10
                if (not dalsie): break
            if (k == 6 and dalsie): return cislo
        cislo += 1
        print("#" + str(cislo))

print("-->" + str(spusti()))