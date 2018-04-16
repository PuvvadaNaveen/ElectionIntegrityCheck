f = open("data.txt","r")  # open file, read-only raw data
o = open("outputRegVotes.txt", "w") # open file, in writable mode 
for line in f:  
    data = line.strip().split(",") # splits the data where is ','and formats
    if len(data) == 40: #Checking and verifying if the length of the data has 40 columns
        settlement_name,settlement_code,settlement_name_english,booth_number,registered_voters,votes,bad_votes,proper_votes,Ale_Yarok,Am_Shalem,Balad,Brit_Olam,Daam_Workers_Party,Eretz_Hadasha,Green_Party,Hadash,Haim_Bekavod,Hatnua,Hope_Change,HaYisraelim,Kadima,Kalkala,Koah_LeHashpia,The_Jewish_Home,Labour_Party,Leader,Likud_Beitenu,Meretz,Moreshet_Avot,Na_Nach,Or,Otzma_LeYisrael,Pirate_Party,Raam_Taal,Senior_Citizens_Party,Shas,Social_Justice,United_Torah_Judaism,We_Brothers,Yesh_Atid = data
        o.write("{0}\t{1}\n".format(settlement_name_english, registered_voters)) # write the required data into the outputRegVotes file

f.close()#closes the opened data txt file.
o.close() #closes the output txt file.


n = open("outputRegVotes.txt","r")  # open file, read-only
s = open("sorted.txt", "w") # open file, write mode
lines = n.readlines() # reads all the lines in the files
lines.sort() # all the lines are sort using sort() method

for line in lines:
	s.write(line) # write the sorted data into the sorted.txt using the open()
n.close()
s.close()