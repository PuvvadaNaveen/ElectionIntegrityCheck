s = open("sorted.txt","r")  # open file, read-only mode 
r = open("reducedData.txt", "w")  # open file, read and write mode 

key = "" # initializing the key with the null
value = 0 # initialzing the value with 0


for line in s:
    data = line.strip().split('\t') # splits the data and formats
    settlement_name, registered_voters = data # gets the required data into the data variable
    if settlement_name != key: # Checking and verifying whether the settlement name and the key value is same or not 
        if key:
            r.write(key + ',' + str(value)+'\n') ## write the required data into the reducedData file

        key = settlement_name
        value = 0
    value += int(registered_voters) # value variable contains all the total of the registered_voters
    