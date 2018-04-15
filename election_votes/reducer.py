s = open("sorted.txt","r")   # open file, read-only
r = open("reducedData.txt", "w")  # open file, write

key = "" # Initially assigning null value to the key
value = 0 # Intially assigning '0' to value
count = 0 # Intially assigning '0' to count

for line in s:
    data = line.strip().split('\t') # Takes the data from sorted text and splits the data with tab dilimitator.
    settlement_name, votes = data # In this step i am taking my desired columns from the sorted data.
    if settlement_name != key: # Checking whether the settlement name and the key value is same or not 
        if key:
            r.write(key + ',' + str(averagevalue)+'\n') #If the key and settlement_name doesnot match then the average value is written into the reduceddata file and the next settlement comes in.

        key = settlement_name 
        value = 0
        count = 0
    value += int(votes) # adds the votes scored by settlements.
    count+=1 # increases the count 
    averagevalue = value/count #This statement here is useful for calculating average votes in a settlement(Total number of votes a settlement has scored divided by the number of times settlement has appeared in the count).
    

