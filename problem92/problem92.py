#[92] Dominik Rohal 26.11.2016
#pole = list([False]*3403) #(9^2)*7

#A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

# For example,
#
# 44 → 32 → 13 → 10 → 1 → 1
# 85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89
#
# Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.
#
# How many starting numbers below ten million will arrive at 89?

def spusti():
    cislo = 0
    pocet = 0
    while cislo < 10000000:
        sq = cislo
        pole = list([False] * 3403)  # (9^2)*7 //nikdy nevyleziem z pola stacilo *6

        while True:
            cis = sq
            sq = 0
            while cis > 0:
                x = cis % 10
                cis //= 10
                sq += x**2
            if (sq == 89):
                pocet += 1
                print("(" + str(pocet) + ") " + str(cislo))
                break
            if (pole[sq]): break
            else:
                pole[sq] = True

        cislo += 1
    return pocet

print("-->" + str(spusti()))