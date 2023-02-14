from setuptools.command.easy_install import easy_install

#Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.
#How many such routes are there through a 20×20 grid?

def faktorial(cislo):
    vysledok = 1
    for k in range(cislo):
        vysledok *= cislo - k
        print(str(cislo-k))
    #print(str(vysledok))
    return vysledok

def vyries(vpravo, dole):
    return (faktorial(vpravo + dole)/(faktorial(dole)*faktorial(vpravo)))

print(str(vyries(20, 20)))