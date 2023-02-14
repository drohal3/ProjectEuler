

L1 = "75"
L2 = "95 64"
L3 = "17 47 82"
L4 = "18 35 87 10"
L5 = "20 04 82 47 65"
L6 = "19 01 23 75 03 34"
L7 = "88 02 77 73 07 63 67"
L8 = "99 65 04 28 06 16 70 92"
L9 = "41 41 26 56 83 40 80 70 33"
L10 = "41 48 72 33 47 32 37 16 94 29"
L11 = "53 71 44 65 25 43 91 52 97 51 14"
L12 = "70 11 33 28 77 73 17 78 39 68 17 57"
L13 = "91 71 52 38 17 14 91 43 58 50 27 29 48"
L14 = "63 66 04 68 89 53 67 30 73 16 69 87 40 31"
L15 = "04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"
L = [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13, L14, L15]

print(str(L))

for k in range(len(L)):
    L[k] = L[k].split()
    for l in range(len(L[k])):
        L[k][l] = [int(L[k][l]), 0]

    print(str(L[k]))
L[0][0][1] = L[0][0][0]

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





