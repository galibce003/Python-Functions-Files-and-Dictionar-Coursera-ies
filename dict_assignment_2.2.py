#Sum of each value of the dict
Junior = {'SI 206':4, 'SI 310':4, 'BL 300':3, 'TO 313':3, 'BCOM 350':1, 'MO 300':3}
credits = 0

for i in Junior:
    credits+=Junior[i]




#dict displaying each char with it's number
str1 = "peter piper picked a peck of pickled peppers"
freq = {}

for i in str1:
    if i not in freq:
        freq[i] = 0
    freq[i]+=1
    
print(freq)




#dict displaying each char with it's number
s1 = "hello"
counts = {}
for i in s1:
    if i not in counts:
        counts[i] = 0
    counts [i]+=1
    
print(counts)





#dict displaying each word with it's number
str1 = "I wish I wish with all my heart to fly with dragons in a land apart"
s = str1.split()
freq_words = {}

for i in s:
    if i not in freq_words:
        freq_words[i] = 0
    freq_words[i]+=1
    
print(freq_words)




#dict displaying each word with it's number
sent = "Singing in the rain and playing in the rain are two entirely different situations but both can be good"

s = sent.split()
wrd_d = {}

for i in s:
    if i not in wrd_d:
        wrd_d[i] = 0
    wrd_d[i]+=1
    
print(wrd_d)





#Determine the max char
sally = "sally sells sea shells by the sea shore"

characters = {}

for i in sally:
    if i not in characters:
        characters[i] = 0
    characters[i]+=1
print(characters)

l = list(characters.keys())
best_char = l[0]
for j in l:
    if characters[j] > characters[best_char]:
        best_char = j
        
print(best_char)





#Determine the min char
sally = "sally sells sea shells by the sea shore and by the road"

characters = {}

for i in sally:
    if i not in characters:
        characters[i] = 0
    characters[i]+=1
print(characters)

l = list(characters.keys())
worst_char = l[0]
for j in l:
    if characters[j] < characters[worst_char]:
        worst_char = j
        
print(worst_char)





#Create A dict
#Count the number of all chars
#But Upper case & lower case can't be separated
#All char should be lower case
string1 = "There is a tide in the affairs of men, Which taken at the flood, leads on to fortune. Omitted, all the voyage of their life is bound in shallows and in miseries. On such a full sea are we now afloat. And we must take the current when it serves, or lose our ventures."
l = string1.lower()   #Convert all chars in lower case

letter_counts = {}

for i in l:
    if i not in letter_counts:
        letter_counts[i] = 0
    letter_counts[i]+=1
    
print(letter_counts)





#Create A dict
#Count the number of all chars
#But Upper case & lower case can't be separated
#All char should be lower case
p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."
l = p.lower()

low_d = {}

for i in l:
    if i not in low_d:
        low_d[i] = 0
    low_d[i]+=1
    
print(low_d)
