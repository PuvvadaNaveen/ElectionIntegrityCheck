s = open("sorted.txt","r")   
r = open("reducedData.txt", "w")   

key = ""
value = 0
count = 0

for line in s:
    data = line.strip().split('\t')
    settlement_name, votes = data
    if settlement_name != key:
        if key:
            r.write(key + '\t' + str(averagevalue)+'\n')

        key = settlement_name
        value = 0
        count = 0
    value += int(votes)
    count+=1
    averagevalue = value/count
    

