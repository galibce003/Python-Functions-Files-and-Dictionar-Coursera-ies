#Count the number of each word in a txt file
x = open("../Python/gj.txt","r")
y = x.read()
s= y.split()

d = {}
for i in s:
    if i not in d:
        d[i] = 0
    d[i]+=1

print(d)
