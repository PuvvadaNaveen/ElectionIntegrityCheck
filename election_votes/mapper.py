f = open("data.txt","r")  # open file, read-only raw data
o = open("output.txt", "w") # open file, write - just our key, value pairs
for line in f:  
    data = line.strip().split(",") 
    if len(data) == 40:
        settlement_name,settlement_code,settlement_name_english,booth_number,registered_voters,votes,bad_votes,proper_votes,Ale_Yarok,Am_Shalem,Balad,Brit_Olam,Daam_Workers_Party,Eretz_Hadasha,Green_Party,Hadash,Haim_Bekavod,Hatnua,Hope_Change,HaYisraelim,Kadima,Kalkala,Koah_LeHashpia,The_Jewish_Home,Labour_Party,Leader,Likud_Beitenu,Meretz,Moreshet_Avot,Na_Nach,Or,Otzma_LeYisrael,Pirate_Party,Raam_Taal,Senior_Citizens_Party,Shas,Social_Justice,United_Torah_Judaism,We_Brothers,Yesh_Atid = data
        o.write("{0}\t{1}\n".format(settlement_name_english, votes))

f.close()
o.close()

n = open("output.txt","r")  # open file, read-only
s = open("sorted.txt", "w") # open file, write
lines = n.readlines()
lines.sort()

for line in lines:
	s.write(line)
n.close()
s.close()
