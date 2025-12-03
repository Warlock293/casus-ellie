# Code van huiswerk vraag 2

a = 2
b = 4
c = 10
d = 12


def mijn_functie_1():
    global a
    a = a * a
    print (a)
    global b
    b = b * b
    print (b)
    global c 
    c = c * c
    print (c)
    global d
    d = d * d
    print (d)

mijn_functie_1()

# Code van huiswerk vraag 3

waarde_1 = 12 + 3, 12 - 3, 12 * 3, 12 / 3
waarde_2 = 12 + 2, 12 - 2, 12 * 2, 12 / 2
waarde_3 = 10 + 5, 10 - 5, 10 * 5, 10 / 5
waarde_4 = 100 + 20, 100 - 20, 100 * 20, 100 / 20

def mijn_functie_2():
    uitvoer_lijst = []
    uitvoer_lijst.append (waarde_1)
    print (waarde_1)
    uitvoer_lijst.append (waarde_2)
    print (waarde_2)
    uitvoer_lijst.append (waarde_3)
    print (waarde_3)
    uitvoer_lijst.append (waarde_4) 
    print (waarde_4)
    return uitvoer_lijst

mijn_functie_2()