sz1 = int(input("Első szám: "))
m = str(input("Művelet jel: "))
sz2 = int(input("Második szám: "))

if m == "+":
    e = sz1+sz2
elif m == "-":
    e = sz1-sz2
elif m == "*":
    e = sz1*sz2
elif m == "/":
    e = sz1/sz2
else:
    e = "ismeretlen"

print(f"{esz} {m} {msz} = {e}")