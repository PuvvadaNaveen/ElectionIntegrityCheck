s = open("sorted.txt","r")   
r = open("reducedData.txt", "w")   

thisKey = ""
thisValue = 0.0
count_list = []
minValue = 0
maxValue = 0


for line in s:
    data = line.strip().split('\t')
    settlement_name, votes = data
    if settlement_name != thisKey:
        if thisKey and thisKey!="": 
            r.write(thisKey + '\t' + min(num_list)+ '\n')
            print thisKey+'\t'+'Minumum: ' +min(num_list)
        thisKey = settlement_name # initializing key and value to default again
        thisValue = 0.0 
        num_list = [] # empty the list each and every time it is a new key value
    num_list.append(votes) # list to store the values of each settelement

s.close()
r.close()