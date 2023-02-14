#[23] Dominik Rohal 12.11.2016
# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number
# that can be written as the sum of two abundant numbers is 24. By mathematical analysis,
# it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However,
# this upper limit cannot be reduced any further by analysis even though it is known that the greatest number
# that cannot be expressed as the sum of two abundant numbers is less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
#limit = 28123

#CELE ZLE!!!!!!
zoznam = set()
def isAbundantNumber(number):
    zoznamDelitelov = set()
    #if (number > 2):
    for k in range(1, (number//2) + 2):
        if (number % k == 0):
            zoznamDelitelov.add(k)
    if (sum(zoznamDelitelov) > number): return True
    else : return False

print(str(isAbundantNumber(158)))



def naplnZoznam():
    sucet = 0
    for k in range (2, 28123 + 1):
        if (isAbundantNumber(k)):
            zoznam.add(k)
            print("+ " + str(k))

def najdi():
    # sum = 0
    # for k in range (len(zoznam)):
    #     for l in range (k, len(zoznam)):
    #         if (zoznam[k] + zoznam[l] <= 28123):
    #             sum += zoznam[k] + zoznam[l]
    # return sum(range(28124)) - sum
    sum = 0
    for k in range(12, 28123):
        for prvok in zoznam:
            if prvok >= k and isAbundantNumber(k + prvok):
                sum += k
                print(str(k) + " -- " + str(sum))
    print(sum)



naplnZoznam()
najdi()
#print(str(najdi()))
395456967


