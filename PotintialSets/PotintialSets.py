import string

def potintailSets():
    pass

def concatinateWords(lWord, rWord, listOfWords):
    # print "lWord = ", lWord
    # print "rWord = ", rWord
    charToDelete = 2
    if ( all(c in string.hexdigits for c in rWord) and all(c in string.hexdigits for c in lWord) ):
        charToDelete = 2

    # print lWord[charToDelete:]
    # print rWord[:-charToDelete]
    if lWord[charToDelete:] == rWord[:-charToDelete]:
        # print "True"
        # print "lWord = ", lWord
        # print "rWord = ", rWord
        print lWord[:charToDelete] + rWord
        listOfWords.add(lWord[:charToDelete] + rWord)
    else:
        pass
        # print "False"
    
if __name__ == "__main__":
    l = set()
    concatinateWords("Alex", "lexA", l)
    print l
    concatinateWords("Alex", "lexA", l)
    print l
    concatinateWords("Alx", "lexA", l)
    print l
    concatinateWords("am", "ma", l)
    print l
    a = "JFI"
    b = "FIF"
    aHex = a.encode("hex")
    bHex = b.encode("hex")
    print aHex, bHex
    concatinateWords(aHex, bHex, l)
    print l