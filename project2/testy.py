


#print(dictionary)

f = open("PROJ2-HNS.txt", "r")
for item in f:
    print(item)
f.close()


dictionary = {}
with open("PROJ2-DNSTS1.txt", "r") as f:
    for line in f:
        splitLine = line.split()
        dictionary[(splitLine[0])] = ",".join(splitLine[1:])

searchstring = "AMaZon.com"

for key, value in dictionary.items():
    if searchstring.lower() in dictionary:
        #print(dictionary[searchstring])
        d2 = key  + " " + dictionary[searchstring.lower()]
        d3 = d2.replace(",", " ")
        #d3 = d3 + " IN"    do this in ls
        # change top part maybe? it has 1 ,
        print(d3)
        # send response here with cs.send(d2.encode())
        break
    else:
        break
