#[14]
# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

def zistiDlzku(zaciatok):
    cisl = zaciatok
    dlzka = 1
    while cisl > 1:
        if (cisl % 2 == 0):
            cisl /= 2
            dlzka += 1
        else:
            cisl *= 3
            cisl += 1
            dlzka +=  1
    return dlzka

print(str(zistiDlzku(13)))

def zisti():
    maxC = 0
    maxD = 0
    akt = 2
    while akt < 1000000:
        dlz = zistiDlzku(akt)
        if (dlz > maxD):
            print(str(maxC) + " (--) " + str(maxD))
            maxD = dlz
            maxC = akt
        akt += 1
    return maxC

print(str(zisti()))