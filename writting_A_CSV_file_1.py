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
    
