#!/bin/python3

from adventofcode import pokaż_wyniki, załaduj_dane, wynik2

dane_dnia = załaduj_dane("05")

wynik1 = ""

ilość_słupków = 0
słupki = {}
już_ruchy = False

for linia in dane_dnia:

    if not ilość_słupków:
        ilość_słupków = int(len(linia) / 4)
        for słupek in range(1, 1 + ilość_słupków):
            słupki[słupek] = []

    if linia.startswith(" 1 "):
        już_ruchy = True
        for słupek in range(1, 1 + ilość_słupków):
            słupki[słupek].reverse()
            słupki[słupek] = list(filter(str.strip, słupki[słupek]))
        continue

    if not już_ruchy:
        for słupek in range(1, 1 + ilość_słupków):
            potencjalna_litera = linia[1 + (słupek - 1) * 4: -2 + słupek * 4]
            słupki[słupek].append(potencjalna_litera)
    elif linia.startswith("\n"):
        continue
    else:
        linia = linia.strip("\n").split(' ')
        ile = int(linia[1])
        z = int(linia[3])
        do = int(linia[5])
        for ruch in range(0, ile):
            a = słupki[z].pop()
            słupki[do].append(a)

for słupek in słupki:
    wynik1 += słupki[słupek].pop()

pokaż_wyniki(wynik1, wynik2)
