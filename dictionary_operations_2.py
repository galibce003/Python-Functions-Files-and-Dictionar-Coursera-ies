f = {'Apple':24,'Orrange':24,'Guava':24,'Water melon':24,'Cool':24}
print(f)


del f['Guava']           #Removing a key pair
print(f)


f['Guava'] = 90          #Adding a key pair
print(f)


x = len(f)
print(x)                 #Counting how many pairs


print(f['Guava'])        #Return the value of "Guava" key

for i in f:
    print(i,f[i])        #here i = keys, f[i] = values


l= list(f.values())      #.values will return a list of values
print(l)

li = list(f.items())     #.items will return a tuple
print(li)

print('Apple' in f)      #Boolean Expression



print(f.get('Apple'))    #=print(f['Apple'])
                         #if I index a key, which doesn't exist, it will give a runtime error.
                         #But .get will return a 'None'


#if the key isn't in the dict
#and we want a word or number instead of 'None'
print(f.get('Shosha',0))  #it returns 0
print(f.get('Shosha',"Sorry we don't have shosha"))  #it returns "Sorry we don't have shosha" 
