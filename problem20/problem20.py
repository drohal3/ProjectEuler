#[20]
# n! means n × (n − 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!

def faktorial(cislo):
    vysledok = 1
    for k in range(cislo):
        vysledok *= k+1
    return vysledok

def spocitaj():
    a = faktorial(100)

    vysledok = 0
    while True:
        vysledok += a % 10
        a //= 10
        if a == 0:
            return vysledok

print(str(spocitaj()))

