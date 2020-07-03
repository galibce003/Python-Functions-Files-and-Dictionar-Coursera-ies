l = [1,-2,5,90,-4]

def abs(x):
    if x>0:
        return x
    else:
        return -x

l1 = sorted(l, key = abs)
print(l1)





l = [1,-2,5,90,-4]

def abs(x):
    if x>0:
        return x
    else:
        return -x

l1 = sorted(l, key = lambda x: abs(x))
print(l1)
