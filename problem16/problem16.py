#[16]
#2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

#What is the sum of the digits of the number 2^1000?

def power(x, y):
    vrat = x;
    for k in range(y - 1):
        vrat *= x
    return vrat

def digSuc(cislo):
    a = cislo
    suc = 0
    while True:
        suc += a % 10
        a //= 10
        if (a == 0):
            return suc

print(str(digSuc(power(2,1000))))