# Write a function that takes an iterable (something you can loop through, ie: string, list, or tuple) and produces a dictionary with all distinct elements as the keys, and the number of each element as the value
def count_unique(some_iterable):
    myDict = {}

    for item in some_iterable:
        freq = myDict.get(item, None)
        if freq:
            myDict[item] = freq+1
        else:
            myDict[item] = 1
    return myDict

# Given two lists, (without using the keyword 'in' or the method 'index') return a list of all common items shared between both lists
def common_items(list1, list2):
    myList = []
    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                myList.append(item1)
                break;
    return myList

# Given two lists, (without using the keyword 'in' or the method 'index') return a list of all common items shared between both lists. This time, use a dictionary as part of your solution.
def common_items2(list1, list2):
    myDict = {}
    myList = []
    for item in list1:
        myDict[item] = 1
    for item in list2:
        if myDict.get(item):
            myList.append(item)
    return myList

def main():
    print "count_unique", count_unique(["1234", "1234", "123", "12", "1", "1", "1"])
    print "common_items", common_items(["1234", "1", "123", "356", "346", "436"],
        ["345", "57", "3246", "1", "324", "12", "123"])
    print "common_items2", common_items2(["1234", "1", "123", "356", "346", "436"],
        ["345", "57", "3246", "1", "324", "12", "123"])

main()