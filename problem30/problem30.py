#[30] Dominik Rohal 18.11.2016
#Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

# 1634 = 14 + 64 + 34 + 44
# 8208 = 84 + 24 + 04 + 84
# 9474 = 94 + 44 + 74 + 44
# As 1 = 14 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.


def spusti():
    cislo = 1
    sum = 0
    while True:
        cislo += 1
        if(cislo > 300000): return sum

        cisloS = str(cislo)
        msum = 0
        for k in range (len(cisloS)):
            msum += int(cisloS[k])**5
            if (msum > cislo): break
        if (msum == cislo):
            sum += msum
            print("+" + str(msum) + " = " + str(sum))


#print(str(80025)[3])
print("-->" + str(spusti()))
