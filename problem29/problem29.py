#[29] Dominik Rohal 22.11.2016
#https://projecteuler.net/problem=29

def spusti():
    setR = set()
    for k in range(2, 100 + 1):
        for l in range(2, 100 + 1):
            setR.add(k**l)
    return len(setR)

print("-->" + str(spusti()))