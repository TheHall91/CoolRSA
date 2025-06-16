import random
import math

def testIsPrime(temp1):
    #Return false if less than one
    if temp1 <= 1:
        return False
    if temp1 % 2 == 0:
        return temp1 == 2
    max_div = math.floor(math.sqrt(temp1))
    #Starting at three, increment by two
    for i in range(3, 1 + max_div, 2):
        if temp1 % i == 0:
            return False
    return True


def primeTestFermat(temp1):
    temp1 = random.getrandbits(100)
    print(math.floor(random.random()*1000))

def selectPQ():
    temp1 = random.getrandbits(512)
    temp1 = temp1 | 1
    flag = False
    while ~flag:
        print(temp1)
        if (testIsPrime(temp1)==True):
            flag = True
        else:
            temp1+=2

    return temp1

    
    