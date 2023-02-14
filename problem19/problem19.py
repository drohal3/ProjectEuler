#[19] Dominik Rohal 13.11.2016
# You are given the following information, but you may prefer to do some research for yourself.
#
# *1 Jan 1900 was a Monday.
# *Thirty days has September,
# *April, June and November.
# *All the rest have thirty-one,
# *Saving February alone,
#  Which has twenty-eight, rain or shine.
# *And on leap years, twenty-nine.
# =*A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# || How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

mesiace = [31,0,31,30,31,30,31,31,30,31,30,31] # na inicializaciu
roky = []

def naplnRoky():
    for rok in range(1901, 2001):
        mes = []
        mes.append(rok)
        for mesiac in mesiace:
            if (mesiac == 0):
                if (rok % 4 == 0 and rok % 100 != 0):
                    mes.append(29)
                else:
                    if (rok % 400 == 0):
                        mes.append(29)
                    else:
                        mes.append(28)
            else: mes.append(mesiac)
        roky.append(mes)
        print(str(mes))
naplnRoky()

def spocitaj():
    pondelky = 0
    den = 2 #1901 zacinal utorkom
    for rok in roky:
        for mesiac in range(1, 12 + 1):
            for denM in range (1, rok[mesiac] + 1):
                if (denM == 1 and den % 7 == 0):
                    pondelky += 1
                    print("(" + str(pondelky) + ") rok: " + str(rok[0]) + " mesiac: " + str(mesiac) + " den: " + str(denM))
                den += 1
    return pondelky

print("-->" + str(spocitaj()))
