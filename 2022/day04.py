#!/bin/python3

from adventofcode import pokaż_wyniki, załaduj_dane, wynik1, wynik2

dane_dnia = załaduj_dane("04")

for linia in dane_dnia:
    linia = linia.strip("\n").split(',')
    początek1 = int(linia[0].split('-')[0])
    koniec1 = int(linia[0].split('-')[1])
    początek2 = int(linia[1].split('-')[0])
    koniec2 = int(linia[1].split('-')[1])

    # jedno w drugim
    if (
        (początek1 <= początek2 and koniec1 >= koniec2) or  # 2-8 3-7
        (początek1 >= początek2 and koniec1 <= koniec2)     # 6-6 4-6
    ):
        wynik1 += 1
        wynik2 += 1
        continue

    # styk na jednym
    elif (
        (koniec1 == początek2 or początek1 == koniec2)  # 5-7 7-9
    ):
        wynik2 += 1

    # ! ['12-91', '2-9']
    elif (
        początek1 > początek2 and początek1 <= koniec2
    ):
        wynik2 += 1

    elif (
        (koniec1 >= początek2 and
         koniec1 >= koniec1 and
         początek1 < koniec2)
    ):
        wynik2 += 1

    elif (
        (początek2 >= początek1 and koniec1 >= początek2)
    ):
        wynik2 += 1


pokaż_wyniki(wynik1, wynik2)
