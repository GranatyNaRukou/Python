from pathlib import Path

file = open(Path(__file__).parent / "data.txt")

list = []
with open(Path(__file__).parent / "data.txt") as file:
    for radek in file:
        list.append(int(radek))

    #print(list)


for i,v in enumerate(list):
    #print(v)
    for j,w in enumerate(list[i+1:]):
        if (v + w) == 2020:
            print(f"prvni cast: = {v * w}")
        for k in list[i+j+1:]:
            if (v + w + k) == 2020:
                print(f"druha cast: = {v * w * k}")
                break

        
#print(1255*765)
#print(282*883*855)
