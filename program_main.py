#take in a set of 3 numbers
#print second largest
import re

def printSecondLargest(inputSet):
    if(len(inputSet) == 3):
        result = inputSet.sort()
        print(inputSet[1])
    else:
        print("Incorrect input")

# sampleSet = [500,369,21]
# printSecondLargest(sampleSet)

#given string of alpahnumerics, print sum of all digits
def printSumDigits(N, testCases):
    for x in testCases:
        result = 0
        placehold = re.findall("[0-9]", x)
        for y in placehold:
            result += int(y)
        print(result)

# submit = ["abc1231", "45gh", "12gh93"]
# printSumDigits(3,submit)

