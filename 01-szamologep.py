sz1 = int(input("Első szám: "))
m = input("Művelet jel: ")
sz2 = int(input("Második szám: ")) 

if sz2 == 0 and m == "/":
    print("Nem lehet nullával osztani.")
else:
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
    print(f"{sz1} {m} {sz2} = {e}")