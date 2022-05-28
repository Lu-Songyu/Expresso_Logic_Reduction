from pickle import FALSE, TRUE


def compareStringLogic(x, y):
    for i in range(0, len(x)):
        if x[i] == y[i]:
            continue
        else:
            if x[i] == '.' or y[i] == '.':
                continue
            else: 
                return False
    return True



            
print("TEST")
print(compareStringLogic("001", "010"))
print(compareStringLogic("000", "0.0"))
print(compareStringLogic("00.", "..0"))
