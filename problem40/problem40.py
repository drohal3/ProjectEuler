#[40] Dominik Rohal 27.11.2016

# An irrational decimal fraction is created by concatenating the positive integers:
#
# 0.123456789101112131415161718192021...
#
# It can be seen that the 12th digit of the fractional part is 1.
#
# If dn represents the nth digit of the fractional part, find the value of the following expression.
#
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

def spusti():
    cislo = " "
    c = 1
    while len(cislo) < 1000001:
        cislo += str(c)
        print("#" + str(len(cislo)))
        c += 1
    index = 1
    vrat = 1
    for k in range(7):
        vrat *= int(cislo[index])
        index *= 10
    return vrat
print("-->" + str(spusti()))