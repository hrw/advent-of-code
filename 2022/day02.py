#/bin/python3

dane_dnia = {}

with open("day02.data") as dane:
    dane_dnia = dane.readlines()

punktacja1 = {
    "A X": 1 + 3,  # Rock + Rock
    "A Y": 2 + 6,  # Rock + Paper
    "A Z": 3 + 0,  # Rock + Scissors
    "B X": 1 + 0,  # Paper + Rock
    "B Y": 2 + 3,  # Paper + Paper
    "B Z": 3 + 6,  # Paper + Scissors
    "C X": 1 + 6,  # Scissors + Rock
    "C Y": 2 + 0,  # Scissors + Paper
    "C Z": 3 + 3,  # Scissors + Scissors
}

punktacja2 = {
    "A X": 3 + 0,  # lose   Rock + Scissors
    "A Y": 1 + 3,  # draw   Rock + Rock
    "A Z": 2 + 6,  # win    Rock + Paper
    "B X": 1 + 0,  # lose   Paper + Rock
    "B Y": 2 + 3,  # draw   Paper + Paper
    "B Z": 3 + 6,  # win    Paper + Scissors
    "C X": 2 + 0,  # lose   Scissors + Paper
    "C Y": 3 + 3,  # draw   Scissors + Scissors
    "C Z": 1 + 6,  # win    Scissors + Rock
}

wynik1 = 0
wynik2 = 0

for linia in dane_dnia:
    wynik1 += punktacja1[linia.strip("\n")]
    wynik2 += punktacja2[linia.strip("\n")]

print(f"step 1: {wynik1}, step 2: {wynik2}")
