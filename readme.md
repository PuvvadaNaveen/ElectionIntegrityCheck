# Election Integrity Check
# Design Data Intensive Systems - Section 02
# Project Group - 2B
  ## Pair 2-3:
  Sandeep Kumar Dara
  Akshay Reddy Vontari
  ## Pair 2-4:
  Naveen Kumar Puvvada
  Raghavender Jarupati
# Links:
Link for repository: https://bitbucket.org/RaghavenderJarupati/electionintegritycheck/overview
link for Issue Tracker:
# Introduction:
The Israeli election dataset contains over 10,000 entries in each year i.e., 2013 and 2015. The data also provides the results by voting booths but not with the settlement and the number of registered voters polled for a party at particular booth. The first seven column contains the details of each booth and settlement and remaining has the number of votes received by the party at each polling booth.
# DataSource:
  Our data source contains the information about elctions in Israel in the years 2013 and 2015. The size of the data source is 2.08 MB. It contains 21,000 records abnd about seven coloums in each csv files. It is structured dataset. The dataset includes setlement_code, setlement_name_english, booth_number, registered_voters, votes, bad_votes, proper_votes, Ale Yarok, Am Shalem, Balad, Brit Olam, Daam Workers Party, Eretz Hadasha, Green Party, Hadash, Haim Bekavod, Hatnua, Hope for Change, HaYisraelim, Kadima, Kalkala, Koah LeHashpi'a, The Jewish Home, Labour Party, Leader, Likud Beitenu, Meretz, Moreshet Avot, Na Nach, Or, Otzma LeYisrael, Pirate Party, Raam-Taal, Senior Citizens Party, Shas, Social Justice, United Torah Judaism, We're Brothers, Yesh Atid.
# DataSource Link:
Link: https://www.kaggle.com/itamarmushkin/israeli-elections-2015-2013/data
# The Challenge:
  ## Volume: the volume of israeli election integrity data is of over 10,000 entries for each year i.e 2013 and 2015. the sources for the volume is from various polling booths from the country.
  ## Variety: The israeli election integrity data is structured as it is relational table which contains rows and columns with contents like booth number, proper votes, bad votes..etc
  ## Velocity: the velocity of election data is low because the election data generation taken place for every two years where the processing is slow.
  ## Veracity: the data provided look trustworthy with the genuine and accurate figures.
  ## Value: With the provided data we can analyze who has got highest number of votes and the lowest number of numbers with that we extract the objectives of the election.
# Big Data Question:
 1. Highest number of registered_votes in a settlement_name?
 2. Average number of votes for a settlement_name?
 # Big Data Solution:
 1.àáå â'ååééòã (ùáè	967	ABU JUWEI'ID	1	690	118	8	110	0	0	3	0	0	0	0	0	0	1	0	0	0	0	0	1	0	0	5	0	0	0	0	0	0	94	1	3	0	0	0	2
 2. BU JUWEI'ID  690
 3. Average :  20
 4. python
 5. Bar Chart