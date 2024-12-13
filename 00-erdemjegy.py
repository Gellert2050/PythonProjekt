o = int(input("Osztályzatod: "))

if o == 1:
    e = "Rossz"
elif o == 2:
    e = "Hanyag"
elif o == 3:
    e = "Változó"
elif o == 4:
    e = "Jó"
elif o == 5:
    e = "Példás"
else:
    e = "Ismeretlen"

print(f"Érdemjegyed: {e}!")