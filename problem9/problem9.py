# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def najdi():
    max = 0
    for a in range(1001): # od 0 po 100 (101 cyklov)
        for b in range(a + 1, 1001 - a):
            c = 1000 - a - b
            print("<->" + str(a) + "x" + str(b) + "x" + str(c))

            if ((a*a) + (b*b) == (c*c) and c > b):
                print("-->" + str(a) + "x" + str(b) + "x" + str(c))
                return a*b*c

print(str(najdi()))