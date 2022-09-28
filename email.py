import re
import operator

def main():
    with open("sample.txt", encoding="utf-8") as f:
        read_data = f.read()
        uni,dom = unique(read_data)
        count = howmany(uni, dom)
        dict1 = makedict(dom,count)
        sortdict = order(dict1)
        out = dict(list(sortdict.items())[0: 10])
        print("the top 10 most used domains are: " + str(out))

def unique(data):
    uni = re.findall(r"[\w-]+@[a-z0-9\.\-+_]+\.[a-z]+",data)
    dom = re.findall(r"@[a-z0-9\.\-+_]+\.[a-z]+",data) #make @[a-z0-9\-+_]+ for stretch goal
    uni = list(dict.fromkeys(uni))
    dom = list(dict.fromkeys(dom))
    return uni, dom

def howmany(unique, domains):
    lenu = len(unique)
    lend = len(domains)
    count = [0] * lend
    for x in range(lenu):
        for y in range(lend):
            if domains[y] in unique[x]:
                count[y] +=1
    return count

def makedict(count,domains):
    newdict= {}
    values = count
    keys = domains
    for i in range(len(keys)):
        newdict[values[i]] = keys[i]
    return newdict
    
def order(dict1):
    sortedtuples = sorted(dict1.items(), key=operator.itemgetter(1), reverse = True)
    sorteddict = {k: v for k, v in sortedtuples}
    return(sorteddict)

if __name__ == "__main__":
    main()
