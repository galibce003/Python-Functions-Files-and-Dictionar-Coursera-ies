#Function - 01
def longer_than_five(list_of_names):
    for name in list_of_names:
        if len(name) > 5:
            return "greater than 5"
    return "Less than Four"

list = ['Galib','Tamim','Shohag']
print(longer_than_five(list))




#Function - 02 (Sum of a list of nums)
def tot(lst):
    total = 0
    for i in lst:
        total+=i
    return total

u = tot([1,4,9])
print(u)




#Function in a Function
def square(num):
    y = num*num
    return y

def sum(x,y,z):
    a = square(x)
    b = square(y)
    c = square(z)
    return a+b+c

c = sum(3,2,10)
print(c)
