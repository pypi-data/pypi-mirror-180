def makeGrammar(arr):
    prods = {}
    for line in arr:
        l = line.strip().split("->")
        prods[l[0].strip()] = list(map(str.strip, l[1].split('|')))
    return prods

def fillfirst(symbol, firsts):
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
        fillfirst(case[0])
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
    firsts = {k:[] for k in nonterminals}
    for symbol in nonterminals:
        fillfirst(symbol, firsts)
    return firsts
