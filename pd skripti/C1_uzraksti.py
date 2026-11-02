import sys

if len(sys.argv) < 2:
    print("noradi srvisa nosaukumu!")
    sys.exit()

nosaukums = sys.argv[1]
kludas = []

with open("sistema.log", encoding="utf-8") as f:
    for rinda in f:
        if nosaukums in rinda and "ERROR" in rinda:
            kludas.append(rinda)
print("ERROR rindu skaits:", len(kludas))

for rinda in kludas[:2]:
    print(rinda.strip())
