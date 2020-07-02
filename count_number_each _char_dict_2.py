#Count the number of each character in a txt file
x = open("../Python/gj.txt","r")
y = x.read()

d = {}
for i in y:
    if i not in d:
        d[i] = 0
    d[i]+=1

print(d)
