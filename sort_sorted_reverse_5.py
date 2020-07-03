l = [2,67,8,9,0,-2,5,7]
l.sort()   #Sort change the order of existing list
print(l)



ls = sorted(l)   #Sorted create a new list with order.
print(ls)
#Output : [-2, 0, 2, 5, 7, 8, 9, 67]


print(l)         #Existing list remains unchanged with sorted
#Output : [2, 67, 8, 9, 0, -2, 5, 7]


print(sorted("Apple"))
#Output : ['A', 'e', 'l', 'p', 'p']


print(sorted("14567"))
#Output : ['1', '4', '5', '6', '7']


print(sorted("Apple",reverse = True))
#Output : ['p', 'p', 'l', 'e', 'A']



