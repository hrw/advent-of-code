
def załaduj_dane(day):

    dane_dnia = {}

    with open(f"day{day}.data") as dane:
        dane_dnia = dane.readlines()

    return dane_dnia


def pokaż_wyniki(wynik1, wynik2):
    print(f"{wynik1}\n{wynik2}")


wynik1 = 0
wynik2 = 0
