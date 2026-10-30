from pathlib import Path
import re

path = Path(__file__).parent / "data.txt"

with path.open() as f:
    platnaHesla = 0
    platnaHesla2 = 0
    for line in f:

        """
        min = int(line[0])
        if line[3].isdigit():
            max = line[2] + line[3]
            max = int(max)
            znak = line[5]
        else:
            max = int(line[2])
            znak = line[4]
        """
        """
        casti_radku = line.split()
        min = int(casti_radku[0].split("-")[0])
        max = int(casti_radku[0].split("-")[1])
        znak = casti_radku[1][0]
        """

        casti_radku = re.split(r'\W+', line.strip())
        #print(casti_radku)

        min = int(casti_radku[0])
        max = int(casti_radku[1])
        znak = casti_radku[2]
        heslo = casti_radku[3]

        print(min, max, znak)
        #heslo = line.split()[2]
        print (znak, heslo)

        if heslo.count(znak) >= min and heslo.count(znak) <= max:
            platnaHesla += 1

        if heslo[min - 1] == znak and heslo[max - 1] != znak:
            platnaHesla2 += 1
        elif heslo[min - 1] != znak and heslo[max - 1] == znak:
            platnaHesla2 += 1


    print(platnaHesla)
    print(platnaHesla2)