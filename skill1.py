def all_odd(someList):
    myList = []
    for item in someList:
        if item % 2:
            myList.append(item)
    return myList

def all_even(someList):
    myList = []
    for item in someList:
        if not item % 2:
            myList.append(item)
    return myList

def long_words(wordList):
    myList = []
    for word in wordList:
        if len(word) >= 4:
            myList.append(word)
    return myList

def smallest(someList):
    if len(someList) == 0:
        return None
    smallest = someList[0]
    for item in someList:
        if item < smallest:
            smallest = item
    return smallest

def halvesies(someList):
    myList = []
    for item in someList:
        myList.append(item/2)
    return myList

def word_lengths(someList):
    myList = []
    for item in someList:
        myList.append(len(item))
    return myList

def main():
    print "all_odd", all_odd([1,2,3,4,5,5,67,8,9])
    print "all_odd", all_odd([1])
    print "all_odd", all_odd([0])
    print "all_even", all_even([1,2,3,4,5,5,67,8,9])
    print "all_even", all_even([1])
    print "all_even", all_even([0])
    print "long_words", long_words(["1234", "123", "3246526"])
    print "long_words", long_words(["1234"])
    print "long_words", long_words(["123"])
    print "smallest", smallest([1,2,3,4,5,5,67,8,9])
    print "smallest", smallest([1])
    print "smallest", smallest([])
    print "halvesies", halvesies([1,2,3,4,5,5,67,8,9])
    print "halvesies", halvesies([1])
    print "halvesies", halvesies([0])
    print "word_lengths", word_lengths(["1234", "123", "3246526"])
    print "word_lengths", word_lengths(["1234"])
    print "word_lengths", word_lengths(["123"])

main()