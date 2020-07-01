#Count the character
x = open("travel_plans.txt","r")
y = x.read()
num= len(y)
print(num)



#Count the words
num_words = 0
x = "emotion_words.txt"

with open(x, 'r') as file:
    for line in file:
        num_words += len(line.split())

print(num_words)



#Count the lines
x = open("school_prompt.txt","r")
y = x.readlines()
num_lines= len(y)
print(num_lines)




#Assign first 30 chars
x = open("school_prompt.txt","r")
y = x.read()
beginning_chars = y[:30]
print(beginning_chars)




#Create a list of 3rd word of each lines
x = open("school_prompt.txt","r")
y = x.readlines()

three = []

for i in y:
    s = i.split()
    w = s[2]
    three.append(w)
    
print(three)




#Create a list of 1st word of each lines
x = open("emotion_words.txt","r")
y = x.readlines()

emotions = []

for i in y:
    s = i.split()
    w = s[0]
    emotions.append(w)
    
print(emotions)




#Assign 1st 33 chars
x = open("travel_plans.txt","r")
y = x.read()

first_chars = y[:33]
print(first_chars)




#Create a list of words containing "p"
x = open("school_prompt.txt","r")
y = x.read()
s = y.split()

p_words = []

for i in s:
    if "p" in i:
        p_words.append(i)
        
print(p_words)



