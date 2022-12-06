#!/bin/python3

from adventofcode import pokaż_wyniki, załaduj_dane, wynik1, wynik2

dane_dnia = załaduj_dane("06")

pakiet = dane_dnia[0]

for indeks in range(0, len(pakiet) - 4):
    czy_marker = pakiet[indeks:indeks + 4]

    poprzedni_znak = ""
    były_powtórki = False

    for znak in sorted(czy_marker):
        if znak != poprzedni_znak:
            poprzedni_znak = znak
        else:
            były_powtórki = True
            break

    if not były_powtórki:
        wynik1 = indeks + 4
        break

for indeks in range(0, len(pakiet) - 14):
    czy_message = pakiet[indeks:indeks + 14]

    poprzedni_znak = ""
    były_powtórki = False

    for znak in sorted(czy_message):
        if znak != poprzedni_znak:
            poprzedni_znak = znak
        else:
            były_powtórki = True
            break

    if not były_powtórki:
        wynik2 = indeks + 14
        break

pokaż_wyniki(wynik1, wynik2)
