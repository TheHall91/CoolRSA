import random
import math


def primeTestFermat(pVal):
    suc = 0
    fal = 0
    for i in range(1000):
        print(i)
        aVal = math.floor(random.randint(2, pVal-2))
        print("beforePower")
        aValP = aVal**(pVal-1)
        print("after")
        if (aValP % pVal) == 1:
            suc+=1
        else:
            fal+=1
    print(f"Success = {suc} Fail = {fal}")
    if suc>fal:
        return True
    return False




    


def selectPQ():
    temp1 = random.getrandbits(512)
    temp1 = temp1 | 1
    flag = False
    while ~flag:
        print(temp1)
        if (primeTestFermat(temp1)==True):
            flag = True
        else:
            temp1+=2

    return temp1


'''def oldTestIsPrime(temp1):
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
  '''
    