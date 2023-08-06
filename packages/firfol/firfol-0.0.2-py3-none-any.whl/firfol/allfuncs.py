def makeGrammar(arr : list(str)):
    prods = {}
    for line in arr:
        l = line.strip().split("->")
        prods[l[0].strip()] = list(map(str.strip, l[1].split('|')))
    return prods
