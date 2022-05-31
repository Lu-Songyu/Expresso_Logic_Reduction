import re

from pkg_resources import empty_provider

offSet =["101", "011", "111"]
onSet = ["000", "100", "010", "001"]
dcSet = ["110"]

# pass in one element(1st argument) and check if it can be reduced from the set(2nd/3rd argument)
def check_validity(item, checkSet, num):
    count = 0
    for x in checkSet:
        if type(x) == list:
            for y in x:
                if compareS(y, item):
                    if y == "000":
                        count = count + 1
        if compareS(x, item):
            count = count + 1
    return count==num 

# compare two logic input index by index
def compareS(x, y):
    for i in range(0, len(x)):
        if x[i] == y[i]:
            continue
        else:
            if x[i] == '.' or y[i] == '.':
                continue
            else: 
                return False
    return True


def expand(item, set1, dcSet):
    mergeSet = set1 + dcSet
    # pass in 00*
    count = 0
    for x in item: 
        if x == '.':
            count = count + 1
    #print("before check validity " + str(item))
    
    return check_validity(item, mergeSet, pow(2, count)) 


def union(item, set1):
    u = [item]
    for x in set1:
        if type(x) == list:
            # 00. comapre ['..0', '000', '100', '010']
             continue
        else:
            if compareS(x, item):
                u.append(x)
    
    return u

def remove_covered_implicants(item, set1):
    un = union(item, set1)
    output = []
    output.append(un)
    for x in set1:
        if x not in un:
            output.append(x)
    return output

# find all possible way to start
def differentStartingIndex(item):
    combo = []
    for x in range(0, len(item)):
        temp = item[0:x] + "." + item[x+1:]
        combo.append(temp)
    return combo


# help find the max * can be padded from starting index
def maxReduce(x, s1, s2):
    # x could be *00, 0*0, 00*
    i = 0
    #print("start test here: original value: " + str(x))
    prev = ""
    legit = expand(x, s1, s2)
    while expand(x, s1, s2):
        i = i + 1
        prev = x[i:i+1]
        x = x[0:i] + "." + x[i+1:]
        #print("mod" + str(i) + " "  + prev) 
        #print(x)
    
    #print("before if " + str(x) + " i: " + str(i))
    if legit: 
        x = x[0:i] + prev + x[i+1:]
    if not legit: 
        x = "NNN"
    
    #print("to return: " + str(x))
    return x

# use func differentStarting index and func maxReduce 
# to find the best use of * for remove implicants
def reduce(item):
    l= differentStartingIndex(item)
    print(l)
    best = ""
    count = 0
    for le in l:
        lr = maxReduce(le, onSet, dcSet)
        occur = lr.count(".")
        #print(str(occur) + " " + str(count))
        if occur > count:
            best = lr
            count = occur
        #print(best)
    return best 
    

if __name__ == "__main__":
             
    reSet = []

    count = 0
    while type(onSet[-1]) != list:

        print(" ")
        print("CYCLE: " + str(count))
        er = reduce(onSet[count])
        tempL = remove_covered_implicants(er, onSet)
        onSet = tempL
        count = count + 1
        print(onSet)

    print("END OF OP")
    print("--------------")
    print(" ")
    print(" ")

    reducedLogic = []

    for x in onSet:
        reducedLogic.append(x[0])
    print("RESULT: ")
    print(reducedLogic)

    