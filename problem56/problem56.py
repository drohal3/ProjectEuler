#[56]A googol (10100) is a massive number: one followed by one-hundred zeros;
# 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size,
# the sum of the digits in each number is only 1.
#Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?

def digSuc(cislo):
    a = cislo
    suc = 0
    while True:
        suc += a % 10
        a //= 10
        if (a == 0):
            return suc



def power(x, y):
    vrat = x;
    for k in range(y - 1):
        vrat *= x
    return vrat

#print(str(power(10,100)))

def najdi():
    maximum = 0
    maxX = 0
    maxY = 0

    for x in range(1, 100):
        for y in range(1, 100):
            if(digSuc(power(x, y)) > maximum):
                maximum = digSuc(power(x, y))
                maxX = x
                maxY = y


    print("X: " + str(maxX) + " | Y: " + str(maxY) + " digSum:= " + str(maximum))

najdi()