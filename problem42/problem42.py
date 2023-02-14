#[42] Dominik Rohal 28.11.2016
tNumb = list([False] * 10000)
for k in range (1, 141):
    tNumb[int((k/2)*(k+1))] = True
print(str(tNumb))

def spusti():
    with open("names.txt") as f:
        menaP = list(f)

    mena = []
    men = False
    meno = ""
    for znak in menaP[0]:
        if (znak >= "A" and znak <= "Z"):
            #
            meno += znak
            men = True #na rozoznamie roznych mien
        # print(str(sc))
        else:
            if (men):
                mena.append(meno)
                meno = ""
                men = False
    pocet = 0
    for meno in mena:
        sc = 0
        for k in range(len(meno)):
            sc += ord(meno[k]) - ord("A") + 1
        if (tNumb[sc]) : pocet += 1
    return pocet

print("-->" + str(spusti()))