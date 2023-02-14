from setuptools.command.easy_install import easy_install

#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

def spusti(hranica = 1000):
    sucet = 0
    for k in range(3, hranica):
        if (k % 3 == 0 or k % 5 == 0):
            print(str(k))
            sucet += k

    return sucet

print(str(spusti()))