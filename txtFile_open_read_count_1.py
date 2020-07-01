x = open("C:/Users/Mehedi Hassan Galib/Desktop/Python/gf.txt","r")
y = x.read()   #Read just return the strings
print(y[:5])


x = open("C:/Users/Mehedi Hassan Galib/Desktop/Python/gf.txt","r")
y = x.readlines()  #readlines return a list
                   #each line will be the value of the list
print(y)



x = open("C:/Users/Mehedi Hassan Galib/Desktop/Python/gf.txt","r")
y = x.readlines()  #readlines return a list
                   #each line will be the value of the list
for i in y:        #In this time every line will be separated as like the txt file
    print(i.strip())  #Strip just remove the extra space between 2 lines.



x = open("C:/Users/Mehedi Hassan Galib/Desktop/Python/gf.txt","r")
for i in x:     #We can directly iterate from x. But here whole file will be iterated. No slicing allowed.
    print(i.strip())



#Count the characters
x = open("C:/Users/Mehedi Hassan Galib/Desktop/Python/gf.txt","r")  
y = x.read()
print(len(y))



#Count the lines
x = open("C:/Users/Mehedi Hassan Galib/Desktop/Python/gf.txt","r")
y = x.readlines()
print(len(y))
