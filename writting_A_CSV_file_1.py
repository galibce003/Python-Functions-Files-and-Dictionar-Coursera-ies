#Writing a CSV file using fString
header = "Name, Age,  Roll : "
info = [("Galib",20,1700003),
        ("Tamim",19,1700002),
        ("Maruf",21,1700006),
        ("Sadid",24,1700007)]
output = open("../Python/info.csv","w")
output.write(header)
output.write("\n")

for i in info:
    x= "{},{},{}".format(i[0],i[1],i[2])
    output.write(x)
    output.write("\n")

output.close()





#Writing a CSV file using JOIN
header = "Name, Age,  Roll : "
info = [("Galib",20,1700003),
        ("Tamim",19,1700002),
        ("Maruf",21,1700006),
        ("Sadid",24,1700007)]
output = open("../Python/info_2.csv","w")
output.write(header)
output.write("\n")

for i in info:
    x= ",".join([i[0],str(i[1]),str(i[2])])  #join needs a list and int must be converted into STRING.
    output.write(x)
    output.write("\n")

output.close()




#Writing a CSV file using CONCATENATE
header = "Name, Age,  Roll : "
info = [("Galib",20,1700003),
        ("Tamim",19,1700002),
        ("Maruf",21,1700006),
        ("Sadid",24,1700007)]
output = open("../Python/info_2.csv","w")
output.write(header)
output.write("\n")

for i in info:
    x= i[0]+","+i[1]+","+i[2]
    output.write(x)
    output.write("\n")

output.close()



#If my value have "," in it
header = '"Name", "Age",  "Roll :"'
info = [("Galib,PhD",20,1700003),
        ("Tamim",19,1700002),
        ("Maruf",21,1700006),
        ("Sadid",24,1700007)]
output = open("../Python/info_2.csv","w")
output.write(header)
output.write("\n")

for i in info:
    x= '"{}","{}","{}"'.format(i[0],i[1],i[2])
    output.write(x)
    output.write("\n")

output.close()
