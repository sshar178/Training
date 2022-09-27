modlist = [(3, "fizz"),(5,"buzz"),(7,"bang")]

for x in range(1,1106):
    out = ""
    for num in modlist:
        if x%num[0] == 0:
            if x%17 == 0:
                out = num[1] + out
            else:
                out += num[1]
    if x%11 == 0:
        out = "bong"
    if x%13 == 0:
        if x%11 == 0 or x%7 == 0 or x%5 == 0:
            firstb = out.index("b")
            if x%17 ==0:
                out = out[firstb:] + "fezz" + out[:firstb]
            else:
                out = out[:firstb] + "fezz" + out[firstb:]
        elif x%17 == 0: 
            out = "fezz" + out
        else:
            out = out+ "fezz"
    if out == "":
        print(x)
    else: print(out)




    