
from csv import reader
from collections import defaultdict
from itertools import chain, combinations


def subsets(arr):
    """ Returns non empty subsets of arr"""
    return chain(*[combinations(arr, i + 1) for i, a in enumerate(arr)])


def returnItemsWithMinSupport(itemSet, transactionList, minSupport, freqSet):
    """calculates the support for items in the itemSet and returns a subset
    of the itemSet each of whose elements satisfies the minimum support"""
    _itemSet = set()
    localSet = defaultdict(int)

    for item in itemSet:
        for transaction in transactionList:
            if item.issubset(transaction):
                freqSet[item] += 1
                localSet[item] += 1

    for item, count in localSet.items():
        support = float(count) / len(transactionList)

        if support >= minSupport:
            _itemSet.add(item)

    return _itemSet


def joinSet(itemSet, length):
    """Join a set with itself and returns the n-element itemsets"""
    return set(
        [i.union(j) for i in itemSet for j in itemSet if len(i.union(j)) == length]
    )


def getItemSetTransactionList(data_iterator):
    transactionList = list()
    itemSet = set()
    for record in data_iterator:
        transaction = frozenset(record)
        transactionList.append(transaction)
        for item in transaction:
            itemSet.add(frozenset([item]))
    return itemSet, transactionList

def printResults(items, rules, minS, minC):

    print(f'==Frequent itemsets (min_sup={minS*100}%)')
    for item, support in sorted(items, reverse=True, key=lambda x: x[1]):
        print(f'{str(item)} , {support*100:.2f}%')
    
    print(f'==High-confidence association rules (min_conf={minC*100}%)')
    for rule, confidence, support in sorted(rules, reverse=True, key=lambda x: x[1]):
        pre, post = rule
        print(f'{str(pre)} => {str(post)}, (Conf: {confidence*100:.2f}%, Supp: {support*100:.2f}%')


def to_str_results(items, rules):

    i, r = [], []
    for item, support in sorted(items, reverse=True, key=lambda x: x[1]):
        x = f'{str(item)} , {support*100:.2f}%'
        i.append(x)

    for rule, confidence, support in sorted(rules, reverse=True, key=lambda x: x[1]):
        pre, post = rule
        x = f'{str(pre)} => {str(post)}, (Conf: {confidence*100:.2f}%, Supp: {support*100:.2f}%'
        r.append(x)

    return i, r


def saveResults(items, rules, minS, minC):

    items, rules = to_str_results(items, rules)
    with open('output.txt', 'w') as f:
        f.write(f"==Frequent itemsets (min_sup={minS*100}%)\n")
        for item in items:
            f.write(f'{item}\n')

        f.write(f'==High-confidence association rules (min_conf={minC*100}%)\n')
        for rule in rules:
            f.write(f'{rule}\n')

        


def pruning(candidateSet, prevFreqSet, length):
    tempCandidateSet = candidateSet.copy()
    for item in candidateSet:
        subsets = combinations(item, length)
        for subset in subsets:
            # if the subset is not in previous K-frequent get, then remove the set
            if(frozenset(subset) not in prevFreqSet):
                tempCandidateSet.remove(item)
                break
    return tempCandidateSet


def dataFromFile(fname):

    with open(fname, 'r') as file:
        csv_reader = reader(file)
        for i, line in enumerate(csv_reader):
            record = frozenset(line)
            yield record


def powerset(s):
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s)))


def associationRule(freqItemSet, itemSetWithSup, minConf, lenTL):
    rules = []
    for k, itemSet in freqItemSet.items():
        for item in itemSet:
            subsets = powerset(item)
            for s in subsets:
                support = float(itemSetWithSup[item] / lenTL)
                confidence = float(
                    itemSetWithSup[item] / itemSetWithSup[frozenset(s)])
                if(confidence > minConf):
                    rules.append(((list(s), list(item.difference(s))), confidence, support))
    return rules

