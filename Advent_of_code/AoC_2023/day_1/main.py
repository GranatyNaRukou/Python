from pathlib import Path

path = Path(__file__).parent / "data.txt"
cisla = []

with open(path, encoding="utf-8") as file:
    for radek in file:
        cislice = "".join(znak for znak in radek if znak.isdigit())
        if cislice:
            cisla.append(int(cislice))

print(cisla)
