modlist = [(3, "fizz"),(5,"buzz"),(7,"bang")] ##list for the normal things 
NUMBER = 0
OUTPUT = 1
for x in range(1,7736):
    out = ""
    for num in modlist: 
        if x%num[NUMBER] == 0: #divisible by the number part of the list
            if x%17 == 0: #other way around for 17
                out = num[OUTPUT] + out  #add word part of the list to output
            else:
                out += num[OUTPUT]
    if x%11 == 0:   #BINGBONG
        out = "bong"
    if x%13 == 0:
        if x%11 == 0 or x%7 == 0 or x%5 == 0:   #if div by 13 and any of the nums that give an output with a B in their word
            firstb = out.index("b") #find first occurence of B
            if x%17 ==0:    #might be wrong here
                out = out[firstb:] + "fezz" + out[:firstb] #add after first b
            else:
                out = out[:firstb] + "fezz" + out[firstb:]  #add before first b
        elif x%17 == 0: 
            out = "fezz" + out  #reverse
        else:
            out = out + "fezz" #for div by 3 or div by 13 case
    if out == "":
        print(x)
    else: print(out)




    