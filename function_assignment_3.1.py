#take and integer
#return the same
def int_return(x):
    return x
y = int_return(3)
print(y)




#take and integer
#return with 2 added
def add(x):
    a = x+2
    return a
y = add(3)
print(y)





#Add to "Nice to meet you" to any string
def change(v):
    return v+'Nice to meet you!'

v=input("Enter the string: ")
change(v)





#Write a function, accum, that takes a list of integers as input and returns the sum of those integers.
def accum(lst):
    sum=0
    for i in lst:
        sum+=i
    return sum  

z = accum([1,2,3])
print(z)




#If length of the list >= 5, return "Longer than 5".
#If the length <5, return "Less than 5".
def length(x):
    if len(x) >= 5:
        return "Longer than 5"
    return "Less than 5"

c = length([1,2,3,8])





#divide function takes in any number and returns that same number divided by 2
#sum function take any number, divide it by 2, and add 6
def divide(x):
    y = x/2
    return y

def sum(x):
    f = (x/2)+6
    return f

v = sum(2)
print(v)
