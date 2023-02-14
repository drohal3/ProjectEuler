#[17]
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters
# used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and
# 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

cisla = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
desiatky = ["","","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]

print(cisla[2])

def spocitaj():

    #for prvok in cisla:
        #sucet += len(prvok)
    #    print(prvok + " [" + str(len(prvok)) + "] " + " >> " + str(sucet))
    for k in range(20,100):
        cislo = desiatky[int(k//10)]
        cislo += cisla[k%10]

        cisla.append(cislo)



    for k in range(100, 1000):
        cislo = k % 100
        if (cislo == 0):
            cislo = cisla[k//100] + "Hundred"
            cisla.append(cislo)
        else:
            cislo = cisla[k//100] + "HundredAnd" + cisla[cislo]
            cisla.append(cislo)
    cisla.append("OneThousand")
    poradie = 0;
    sucet = 0
    for cis in cisla:
        sucet += len(cis)
        print(str(poradie) + " | " + cis + " [" + str(len(cis)) + "] " + " >> " + str(sucet))
        poradie += 1

    #for k in range(100, 1000):
     #   cislo = a
    # sucet *= 10 #10x sa vyskytuje postupnost
    # sucet += 900 * len("HundredAnd")
    # sucet -= 9 * len("and") # pri nasobkoch 100 sa and nevyskytuje
    # sucet += 100 * len("oneTwoThreeFourFiveSixSeveEightNine")
    # sucet += len("onethousand")

    print("....-->" + str(sucet))
spocitaj()