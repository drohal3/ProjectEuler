#[206]
# cisloPole = [1,0,2,0,3,0,4,0,5,0,6,0,7,0,8,0,9,0,0]
#
# def krok():
#
#     index = 17
#     while True:
#         cisloPole[index] = (cisloPole[index] + 1) % 10
#         if (not cisloPole[index] == 0 or index == 1): break
#         index -= 2
#
# # for k in range(1000000000):
# #     if (k % 10000000 == 0):
# #         print(str(cisloPole))
# #     krok()
#
# def spusti():
#     while True:
#         cisloS = ""
#         for k in range(19):
#             cisloS+=cisloPole[k]
#         if (int(cisloS))
import math
def spusti():
    cislo = int(math.sqrt(19293949596979899)) #max. vydelene 10
    #print (str(cislo))
    while True:
        cis = str(cislo**2)
        k = len(cis) - 1 #-1 lebo zacinam od nuly
        h = 9#10
        while True:
            #dalsi = True
            if (not cis[k] == str(h % 10)):
                #dalsi = False
                break
            if (h == 1): return cislo * 10 #lebo bolo zmensene pre urychlenie
            k -= 2
            h -= 1
        cislo -= 1


print("-->" + str(spusti()))