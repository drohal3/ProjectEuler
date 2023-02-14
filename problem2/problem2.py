from setuptools.command.easy_install import easy_install

def spusti():
    predposlednyClen = 0
    poslednyClen = 1
    sucet = 0

    while True:
        if (poslednyClen > 4000000):
            return sucet
        if (poslednyClen % 2 == 0):
            sucet = sucet + poslednyClen
        pom = predposlednyClen + poslednyClen
        predposlednyClen = poslednyClen
        poslednyClen = pom

print(str(spusti()))