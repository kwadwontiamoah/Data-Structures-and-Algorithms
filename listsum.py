import time

def listsum(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i
    return theSum

print(listsum([1,3,5,7,9,11,13,15,17,19,21]))


def listsum(numList):
   if len(numList) == 1:
       return numList[0]
   else:
       return numList[0] + listsum(numList[1:])
       
##print(listsum([1,3,5,7,9]))
