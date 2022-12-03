#!/bin/python3

from adventofcode import pokaż_wyniki, załaduj_dane, wynik1, wynik2

dane_dnia = załaduj_dane("03")


def priorytet(litera):
    if ord(litera) <= ord('Z'):
        priorytet = ord(litera) - 65 + 27
    else:
        priorytet = ord(litera) - 96

    return priorytet


def szukaj_badge(wspólny_plecak):
    for litera in wspólny_plecak[0]:
        if litera in wspólny_plecak[1] and litera in wspólny_plecak[2]:
            return litera


licznik_elfów = 1
plecak_grupy = []

for linia in dane_dnia:
    linia = linia.strip("\n")

    pół_długość = int(len(linia) / 2)
    połowa1 = linia[0:pół_długość]
    połowa2 = linia[pół_długość:]

    for litera in połowa1:
        if litera in połowa2:
            wynik1 += priorytet(litera)
            break

    plecak_grupy.append(linia)

    if licznik_elfów == 3:
        wynik2 += priorytet(szukaj_badge(plecak_grupy))
        licznik_elfów = 0
        plecak_grupy = []

    licznik_elfów += 1

pokaż_wyniki(wynik1, wynik2)
