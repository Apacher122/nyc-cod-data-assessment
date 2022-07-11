
from collections import defaultdict
from optparse import OptionParser

from utils import *



def Apriori(input_file, minSupport, minConfidence):

    inFile = dataFromFile(input_file)
    itemSet, transactionList = getItemSetTransactionList(inFile)

    globalItemSetWithSup = defaultdict(int)
    globalFreqItemSet = dict()

    oneCSet = returnItemsWithMinSupport(itemSet, transactionList, minSupport, globalItemSetWithSup)

    currentLSet = oneCSet

    k = 2

    while currentLSet != set([]):

        globalFreqItemSet[k - 1] = currentLSet
        candidateSet = joinSet(currentLSet, k)
        candidateSet = pruning(candidateSet, currentLSet, k-1)
        currentLSet = returnItemsWithMinSupport(
            candidateSet, transactionList, minSupport, globalItemSetWithSup
        )
        k = k + 1

    def getSupport(item):
        return float(globalItemSetWithSup[item]) / len(transactionList)

    items = []
    for key, value in globalFreqItemSet.items():
        items.extend([(list(item), getSupport(item)) for item in value])

    rules = associationRule(globalFreqItemSet, globalItemSetWithSup, minConfidence, len(transactionList))

    return items, rules



if __name__ == "__main__":

    optparser = OptionParser()
    optparser.add_option(
        "-f", "--inputFile", dest="input", help="filename containing csv", default=None
    )
    optparser.add_option(
        '-s',
        '--minSupport',
        dest='minS',
        help='minimum support value',
        default=0.01,
        type='float',
    )
    optparser.add_option(
        '-c',
        '--minConfidence',
        dest='minC',
        help='minimum confidence value',
        default=0.5,
        type='float',
    )

    (options, args) = optparser.parse_args()

    items, rules = Apriori(options.input, options.minS, options.minC)

    printResults(items, rules, options.minS, options.minC)

    saveResults(items, rules, options.minS, options.minC)
    
