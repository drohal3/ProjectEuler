#[22] Dominik Rohal 21.11.16

with open("names.txt") as f:
    menaP = list(f)
mena = ""

def spusti():
    mena = []
    men = False
    meno = ""
    for znak in menaP[0]:
        if (znak  >= "A" and znak <="Z"):
            #
            meno += znak
            men = True
        #print(str(sc))
        else:
            if (men):

                mena.append(meno)
                meno = ""
                men = False
    mena.sort()
    print(str(mena))

    score = 0
    poz = 0
    for meno in mena:
        poz += 1
        sc = 0
        for k in range(len(meno)):
            sc += ord(meno[k]) - ord("A") + 1
        add = sc * poz
        score += add
        print(meno + "|" + str(sc) + "*" + str(poz) + "=" + str(add) + "==>" + str(score))

    return score
print("-->" + str(spusti()))
print((mena))