def makeGrammar(arr):
    prods = {}
    for line in arr:
        l = line.strip().split("->")
        prods[l[0].strip()] = list(map(str.strip, l[1].split('|')))
    return prods

def fillfirst(symbol, firsts, grammar):
    prods  = grammar
    nonterminals = set(prods.keys())
    if len(firsts[symbol])!=0:
        return
    prodcases = prods[symbol]
    anslist = set()
    for case in prodcases:
        if case=='eps':
            anslist.add('eps')
            continue
        while case!='':
            if case[0] in nonterminals:
                fillfirst(case[0], firsts, grammar)
                anslist = anslist.union(firsts[case[0]])
                if 'eps' in prods[case[0]]:
                    case = case[1:]
                else:
                    case = ''
            else:
                anslist.add(case[0])
                case = ''
    firsts[symbol]=anslist

def findFirsts(grammar):
    nonterminals = set(grammar.keys())
    firsts = {k:set() for k in nonterminals}
    for symbol in nonterminals:
        fillfirst(symbol, firsts, grammar)
    return firsts

def findFollows(grammar, start):
    firsts  = findFirsts(grammar)
    prods = grammar
    nonterminals = set(prods.keys())
    follows = {k:set() for k in nonterminals}
    for key in prods.keys():
        anslist = set()
        for symbol in prods.keys():
            prodcases = prods[symbol]
            for case in prodcases:
                if key not in case:
                    continue
                if case.find(key)==len(case)-1:
                    anslist = anslist.union(follows[symbol])
                else:
                    rem = case[case.find(key)+1:]
                    while rem!="":
                        nextsym = rem[0]
                        if nextsym in nonterminals:
                            anslist = anslist.union(firsts[nextsym])
                            if 'eps' in firsts[nextsym]:
                                rem = rem[1:]
                                continue
                        else:
                            anslist.add(nextsym)
                            break
                    if rem=="":
                        anslist = anslist.union(follows[symbol])
        if 'eps' in anslist:
            anslist.remove('eps')
        if key==start:
            anslist.add('$')
        follows[key] = anslist
    return follows
