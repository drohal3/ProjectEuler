#[50]
#the prime 41, can be written as the sum of six consecutive primes:

#41 = 2 + 3 + 5 + 7 + 11 + 13
#This is the longest sum of consecutive primes that adds to a prime below one-hundred.

#The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

#Which prime, below one-million, can be written as the sum of the most consecutive primes?

import math



def jePrvocislo(cislo):
    if (cislo < 2):
        return False
    for k in range(1, int(math.sqrt(cislo)) + 1):
        if (k > 1 and cislo % k == 0 and cislo != k):
            return False
    return True


def najdiDalsiePrvocislo(min):
    cislo = min + 1
    while True:
        if (jePrvocislo(cislo)):
            return cislo
        else:
            cislo += 1


#def najdiMaxPrvZPrv(okno, hranica): #najde najvacsie prvocislo, ktore vzniklo scitanim daneho poctu prvocisel a nepresiahlo danu hranicu


print(str(jePrvocislo(10)))

def hladaj(hranica = 1000000):
    posunutie = 0;
    poslednePrvocislo = []
    posledneCislo = []

    cislo = 1
    while True:
        cislo = najdiDalsiePrvocislo(cislo)
        if (sum(posledneCislo) + cislo >= hranica):
            #return sum(poslednePrvocislo)

            break
        else:
            posledneCislo.append(cislo)
            if (jePrvocislo(sum(posledneCislo))):
                for k in range(len(poslednePrvocislo), len(posledneCislo)):
                    poslednePrvocislo.append(posledneCislo[k])

                print(str(sum(posledneCislo)) + " je prvocislo: || " + str(sum(poslednePrvocislo)))



    posunutie = 0
    while True:
        posunutie += 1
        posledneCislo.clear()
        for prvok in poslednePrvocislo:
            posledneCislo.append(prvok)
        for k in range (posunutie):
            del posledneCislo[0]

        if (sum(posledneCislo) + najdiDalsiePrvocislo(max(posledneCislo)) >= hranica):
            return sum(poslednePrvocislo)

        while True:
            cislo = najdiDalsiePrvocislo(max(posledneCislo))
            if (sum(posledneCislo) + cislo >= hranica):
                break

            posledneCislo.append(cislo)
            if (jePrvocislo(sum(posledneCislo)) and len(posledneCislo) > len(poslednePrvocislo)):
                poslednePrvocislo.clear()
                print(str(sum(posledneCislo)) + " je prvocislo: || uprava posunutim")
                for prvok in posledneCislo:
                    poslednePrvocislo.append(prvok)
                    posunutie = 0



#print(str(najdiDalsiePrvocislo(3)))
print("--->" + str(hladaj()))




