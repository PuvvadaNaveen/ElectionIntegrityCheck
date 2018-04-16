s = open("sorted.txt","r")   
r = open("reducedData.txt", "w")   

key = ""
value = 0
count = 0

for line in s:
    data = line.strip().split('\t') # splits the data and formats
    settlement_name, registered_voters = data # gets the required data into the data variable
    if settlement_name != key:
        if key:
            r.write(key + ',' + str(value)+'\n') ## write the required data into the reducedData file

        key = settlement_name
        value = 0
    value += int(registered_voters) # value variable contains all the total of the registered_voters
    