
def findCheapestOp(unsantitizedNumber, listOfOps):
    dic = {}
    dic2 = {}

    number = ""
    #sanitize number
    for i in range(len(unsantitizedNumber)):
        if ord(unsantitizedNumber[i]) <= ord("9") and ord(unsantitizedNumber[i]) >= ord("0"):
            number += unsantitizedNumber[i]

    # save the data to the dictionaries
    for index, op in enumerate(listOfOps):
        for prefixAndPrice in op:
            # only update or add when there is a new entry or the price is smaller than the previous entry
            # since the number only accepts one prefix for its price, merging the ops (while keeping them tracked) is implemented
            if prefixAndPrice[0] not in dic or ( prefixAndPrice[0] in dic and prefixAndPrice[1] < dic[prefixAndPrice[0]] ):
                dic[prefixAndPrice[0]] = prefixAndPrice[1] 
                dic2[prefixAndPrice[0]] = index

    # list to keep track of the smallests
    opArr = [float('inf') for _ in listOfOps]
    while number:
        currentNumber = int(number)
        if currentNumber in dic and opArr[dic2[currentNumber]] == float('inf'):
            opArr[dic2[currentNumber]] = min(opArr[dic2[currentNumber]], dic[currentNumber])
        else:
            number = number[0:len(number)-1]
    if min(opArr) == float('inf'):
        return "Prefix not found"
    # The question said to return the op only, but I kept it as a string for readability
    return f"Operator: {opArr.index(min(opArr)) + 1}, Price/hr = {min(opArr)}, Number: {unsantitizedNumber}"


# Testing ground
opData = [[[1, 0.9], [268, 5.1], [46, 0.17], [4620,0.0], [468,0.15], [4631,0.15], [4673,0.9], [46732,1.1]],
                              [[1, 0.92], [44,0.5], [467,1.0], [48,1.2]]]

import unittest

class TestStringMethods(unittest.TestCase):

    def test_not_found(self):
        number = "+7777120937"
        self.assertEqual('Prefix not found', findCheapestOp(number, opData))

    def test_many_duplications(self):
        number = "123"
        self.assertEqual(f"Operator: 1, Price/hr = 0.9, Number: {number}", findCheapestOp(number, opData))

    def test_correct_cases_with_special_characters(self):
        number = "+46-73-212345"
        self.assertEqual(f"Operator: 2, Price/hr = 1.0, Number: {number}", findCheapestOp(number, opData))

if __name__ == '__main__':
    unittest.main()