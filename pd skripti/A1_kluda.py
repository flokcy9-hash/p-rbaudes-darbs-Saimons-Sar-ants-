with open("sistema.log", "r", encoding="utf-8") as fails:
    rindas = fails.readlines()
    skaits = 0
    for rindas in rindas:
        if "CRITICAL" in rindas:
            skaits += 1

    print("CRITICAL rindas:", skaits)
