#[34] Dominik Rohal 26.11.2016

#145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

def faktorial(cislo):
    cisl = cislo
    vrat = 1
    while cisl > 0:
        vrat*= cisl
        cisl -= 1
    return vrat

#print(str(faktorial(6)))

def spusti():
    cislo = 10
    pocet = 0
    sum = 0
    while cislo < 100000:
        cisl = cislo

        f = 0
        while cisl > 0:
            f += faktorial(cisl % 10)
            cisl //= 10
        if (f == cislo):
            pocet += 1
            sum += cislo
            print(str(pocet) + "|" + str(cislo) + " ==>" + str(sum))
        cislo += 1
    return sum
print("-->" + str(spusti()))