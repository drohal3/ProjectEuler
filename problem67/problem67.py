#[67] Dominik Rohal 19.11.2016
riadkyP = list()
with open("triangel.txt") as f:
    riadkyP = list(f)
    #lines = lines[1].split("\n")
    print(str(riadkyP))

L = []

print(str(type(L)))
for riadok in riadkyP:
    pom = riadok.split()
    pomR = []
    for prvok in pom:
        pomR.append([int(prvok), 0])
    L.append(pomR)
L[0][0][1] = L[0][0][0]
# for riadok in L:
#     for prvok in riadok:
#         prvok = int(prvok)

print(str(L))

# for k in range(len(L)):
#     L[k] = L[k].split()
#     for l in range(len(L[k])):
#         L[k][l] = [int(L[k][l]), 0]
#     L[0][0][1] = L[0][0][0]
#     print(str(L[k]))

def spusti():
    for riadok in range(len(L) - 1): #lebo z posledneho nemam kam ist
        for prvok in range(len(L[riadok])):
            if (L[riadok][prvok][1] + L[riadok + 1][prvok][0] > L[riadok + 1][prvok][1]):
                L[riadok + 1][prvok][1] = L[riadok][prvok][1] + L[riadok + 1][prvok][0]

            if (L[riadok][prvok][1] + L[riadok + 1][prvok + 1][0] > L[riadok + 1][prvok + 1][1]):
                L[riadok + 1][prvok + 1][1] = L[riadok][prvok][1] + L[riadok + 1][prvok + 1][0]
        print(str(L[riadok]))
    print(str(L[len(L) - 1]))
    maximum = 0
    for prvok in L[len(L) - 1]:
        if prvok[1] > maximum: maximum = prvok[1]
    return maximum


print("-->" + str(spusti()))


