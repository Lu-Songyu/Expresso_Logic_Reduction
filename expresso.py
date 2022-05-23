from heapq import merge
from operator import truediv
import re
from xml.etree.ElementTree import ElementTree

offSet =["101", "011", "111"]
onSet = ["000", "100", "010", "001"]
dcSet = ["110"]

# pass in one element(1st argument) and check if it can be reduced from the set(2nd/3rd argument)
def check_validity(item, checkSet, num):
    r = re.compile(item)
    newList = list(filter(r.match, checkSet))
    #print("reg list: ")
    #print(newList)
    #print(len(newList)==num)
    return len(newList)==num 

    

def expand(item, set1, dcSet):
    mergeSet = set1 + dcSet
    # pass in *01
    count = 0
    for x in item: 
        if x == '*':
            count = count + 1
    item = item.replace("*", ".") 
        
    return check_validity(item, mergeSet, pow(2, count)) 
           

def remove_covered_implicants(item, set1):
    temp = item
    item = item.replace("*", ".") 

    e  = re.compile(item)
    setToDelete = list(filter(e.match, set1))

    print(onSet)
    print(setToDelete)

    output = [temp]
    for i in set1:
        if i not in setToDelete:
            print(i)
            output.append(i)
    
    return output

# help find the max * can be padded from starting index
def maxReduce(x, s1, s2):
    size = len(x)
    start = 0
    index = 1
    t = x[index+start:]
    txt = t.rjust(size, "*")
    while expand(txt, s1, s2):
        index = index + 1
        t = x[index+start:]
        txt = t.rjust(size, "*")


    t = x[index-1:]
    txt = t.rjust(size, "*")
    return txt

if __name__ == "__main__":
    print(onSet)
    size = 3

    er1 = maxReduce(onSet[0], onSet, dcSet)
    #print(e1)
    tempL = remove_covered_implicants(er1, onSet)
    #print(tempL)
    onSet = tempL
    #print(onSet)

    er2 = maxReduce(onSet[1], onSet, dcSet) # should come out as 00*
    tempL2 = remove_covered_implicants("00*", onSet)
    onSet = tempL2

    print(onSet)