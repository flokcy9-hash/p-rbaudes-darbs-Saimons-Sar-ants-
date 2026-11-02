skaiskaits = {}

with open("sistema.log", encoding="utf-8") as f:
    for rinda in f:
        limenis = rinda.split()[2]
        skaits[limenis] = skaits.get(limenis, 0) + 1

for limenis, skiats_rindu in sorted(skaits.limenis(), key=lambda x: x[1], reserve=True):
             print(limenis, skaits_rindu)
