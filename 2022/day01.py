#/bin/python3

kalorie = {}

with open("day01.data") as dane:
    kalorie = dane.readlines()

najwięcej = 0
aktualny = 0
który_elf = 1
najwięcej_elf = 0
elfie_kalorie_odwrotnie = {}

for jedzonko in kalorie:
    if jedzonko == "\n":
        elfie_kalorie_odwrotnie[aktualny] = który_elf
        aktualny = 0
        który_elf += 1
        continue
    else:
        aktualny += int(jedzonko)

    if najwięcej < aktualny:
        najwięcej = aktualny
        najwięcej_elf = który_elf

print(f"{najwięcej_elf} ma {najwięcej} kalorii")

trzy_elfy_kalorie = 0
for kalorii in sorted(elfie_kalorie_odwrotnie.keys(), reverse=True)[:3]:
    trzy_elfy_kalorie += kalorii

print(trzy_elfy_kalorie)
