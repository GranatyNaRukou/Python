from pathlib import Path

file = open(Path(__file__).parent / "data.txt")

list = []
with open(Path(__file__).parent / "data.txt") as file:
    for radek in file:
        list.append(int(radek))

    print(list)

"""
soucetRovnaSe2020 = False
for i,v in enumerate(list):
    #print(v)
    for j,w in enumerate(list[i:]):
        #print(j)
        for k in list[j:]:
            if (v + w + k) == 2020:
                soucetRovnaSe2020 = True
                print(k)
                break
        if soucetRovnaSe2020 == True:
            print(w)
            break
    if soucetRovnaSe2020 == True:
        print(v)
        break

print(1255*765)
print(282*883*855)
"""