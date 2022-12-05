#!/bin/python3

from adventofcode import pokaż_wyniki, załaduj_dane
import pprint

dane_dnia = załaduj_dane("05")


def pokaż_słupki(słupki):
    poziom = 0
    print("-----------------------------------------")
    while True:
        for słupek in słupki:
            try:
                print(f" {słupki[słupek][poziom]} ", end='')
            except:
                print("   ", end='')
        print("")
        poziom += 1
        if poziom > 3:
            print("-----------------------------------------")
            break


wynik2 = ""

ile_słupków = 0
słupki = {}
już_ruchy = False

for linia in dane_dnia:

    if not ile_słupków:
        ile_słupków = int(len(linia) / 4)
        for słupek in range(1, 1 + ile_słupków):
            słupki[słupek] = []

    if linia.startswith(" 1 "):
        już_ruchy = True
        for słupek in range(1, 1 + ile_słupków):
            słupki[słupek].reverse()
            słupki[słupek] = list(filter(str.strip, słupki[słupek]))
        continue

    if not już_ruchy:
        for słupek in range(1, 1 + ile_słupków):
            potencjalna_litera = linia[1 + (słupek - 1) * 4: -2 + słupek * 4]
            słupki[słupek].append(potencjalna_litera)
    elif linia.startswith("\n"):
        continue
    else:
        linia = linia.strip("\n").split(' ')
        ile = int(linia[1])
        z = int(linia[3])
        do = int(linia[5])

        dźwig = []
        for ruch in range(0, ile):
            dźwig.append(słupki[z].pop())

        dźwig.reverse()

        for znak in dźwig:
            słupki[do].append(znak)

        pokaż_słupki(słupki)

for słupek in słupki:
    wynik2 += słupki[słupek].pop()
pokaż_wyniki('', wynik2)
