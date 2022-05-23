from heapq import merge
import re
from xml.etree.ElementTree import ElementTree

offSet =["101", "011", "111"]
onSet = ["000", "100", "010", "001"]
dcSet = ["110"]

# pass in one element(1st argument) and check if it can be reduced from the set(2nd argument)
def check_validity(item, checkSet, num):
    print(item)
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
    print(count)
    item = item.replace("*", ".") 
        
    return check_validity(item, mergeSet, pow(2, count)) 
           

def remove_covered_implicants(item, set1):
    
    temp = item
    item = item.replace("*", ".") 

    e  = re.compile(item)
    setToDelete = list(filter(e.match, set1))

    output = [temp]
    for i in set1:
        if i not in setToDelete:
            output.append(i)
    
    return output


item = expand("000", onSet, dcSet)
newS = remove_covered_implicants("**0", onSet)
print("updated")
print(newS)