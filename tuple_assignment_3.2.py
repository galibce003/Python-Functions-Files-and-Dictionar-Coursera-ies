#Create a tuple called olympics with four elements: “Beijing”, “London”, “Rio”, “Tokyo”
#it will be tuple, even if we don't use ()
olympics = "Beijing", "London", "Rio", "Tokyo"



#Create a list of the second elements of each tuple
tuples_lst = [('Beijing', 'China', 2008), ('London', 'England', 2012), ('Rio', 'Brazil', 2016, 'Current'), ('Tokyo', 'Japan', 2020, 'Future')]
country = []

for i in tuples_lst:
    country.append(i[1])
    
print(country)




#assign the variables city, country, and year to the values of the tuple olymp.
olymp = ('Rio', 'Brazil', 2016)
city, country, year = olymp




#Define a function 'info' with five parameters: name, gender, age, bday_month, and hometown
def info(name, gender, age, bday_month, hometown):
    return name, gender, age, bday_month, hometown

info("A","Male",24,"June","Rar")




#Create a list containing het number of medals for each country.
#The .items() method provides a list of tuples
gold = {'USA':31, 'Great Britain':19, 'China':19, 'Germany':13, 'Russia':12, 'Japan':10, 'France':8, 'Italy':8}
num_medals = []

for i in gold.items():
    num_medals.append(i[1])
