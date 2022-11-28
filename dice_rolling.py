import random
import time as t
tc = ["testa", "croce"]
tc2 = ["la moneta sta girando...", "la moneta sta atterrando dallo spazio...", "è una moneta quella?", "una moneta infuocata!!!w"]
while True:
    print("")
    print("premi P per lanciare il dado! o T per testa o croce")
    choose = input().lower()

    if choose == "p":
        ac = random.randint(1,6)
        print("è uscito",ac)
    elif choose == "t":
        ac2 = random.choice(tc)
        ac3 = random.choice(tc2)
        print(ac3)
        t.sleep(2)
        print("è uscito:",ac2)
    else:
        print("scrivi P per lanciare il dado! o T per testa o croce")
        continue