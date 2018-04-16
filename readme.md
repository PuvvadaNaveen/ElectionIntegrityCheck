# Election Integrity Check
### Course Number:44-564  
### Design Data Intensive Systems - Section 02
## Project Group - 2B
  * Pair 2-3:
  
  1. Sandeep Kumar Dara
     * Email: S528737@nwmissouri.edu
     * Semester:04
  
  2. Akshay Reddy Vontari
     * Email: S528772@nwmissouri.edu
     * Semester:04
  
  * Pair 2-4:
  
  1. Naveen Kumar Puvvada
     * Email: S530483@nwmissouri.edu
     * Semester:02
  2. Raghavender Jarupati
     * Email: S528738@nwmissouri.edu
     * Semester:04
## Links:
Link for repository: https://bitbucket.org/RaghavenderJarupati/electionintegritycheck/overview

links for Issue Tracker:

1. https://bitbucket.org/RaghavenderJarupati/electionintegritycheck/issues/1/issue-1
2. https://bitbucket.org/RaghavenderJarupati/electionintegritycheck/issues/2/issue-2
3. https://bitbucket.org/RaghavenderJarupati/electionintegritycheck/issues/3/issue-3
4. https://bitbucket.org/RaghavenderJarupati/electionintegritycheck/issues/4/issue-4

## Introduction:
The Israeli election dataset contains over 10,000 entries in each year i.e., 2013 and 2015. The data also provides the results by voting booths but not with the settlement and the number of registered voters polled for a party at particular booth. The first seven column contains the details of each booth and settlement and remaining has the number of votes received by the party at each polling booth.
## DataSource:
  Our data source contains the information about elctions in Israel in the years 2013 and 2015. The size of the data source is 2.08 MB. It contains 11,000 records abnd about seven coloums in each csv files. It is structured dataset. The dataset includes setlement_code, setlement_name_english, booth_number, registered_voters, votes, bad_votes, proper_votes, Ale Yarok, Am Shalem, Balad, Brit Olam, Daam Workers Party, Eretz Hadasha, Green Party, Hadash, Haim Bekavod, Hatnua, Hope for Change, HaYisraelim, Kadima, Kalkala, Koah LeHashpi'a, The Jewish Home, Labour Party, Leader, Likud Beitenu, Meretz, Moreshet Avot, Na Nach, Or, Otzma LeYisrael, Pirate Party, Raam-Taal, Senior Citizens Party, Shas, Social Justice, United Torah Judaism, We're Brothers, Yesh Atid.
## DataSource Link:
Link: https://www.kaggle.com/itamarmushkin/israeli-elections-2015-2013/data
## The Challenge:
  1. Volume: the volume of israeli election integrity data is of over 10,000 entries for each year i.e 2013 and 2015. the sources for the volume is from various polling booths from the country.
  2. Variety: The israeli election integrity data is structured as it is relational table which contains rows and columns with contents like booth number, proper votes, bad votes..etc
  3. Velocity: the velocity of election data is low because the election data generation taken place for every two years where the processing is slow.
  4. Veracity: the data provided look trustworthy with the genuine and accurate figures.
  5. Value: With the provided data we can analyze who has got highest number of votes and the lowest number of numbers with that we extract the objectives of the election.
## Big Data Question and Solutions:
  **1.For each settlement_name in 2013, what are the total registered_votes?**    
      1.Mapper Input:  
        àáå â'ååééòã (ùáè	967	ABU JUWEI'ID	1	425	66	5	61	0	4	0	0	0	0	49	0	1	2	0	0	0	0	0	0	0	0	0	0	0	0	1	0	4  
        àáå â'ååééòã (ùáè	967	ABU JUWEI'ID	2	638	145	1	144	0	2	0	0	0	0	120	0	0	1	1	0	1	0	0	0	0	2	0	0	0	1	0	0	16  
        àáå â'ååééòã (ùáè	967	ABU JUWEI'ID	3	547	102	1	101	0	2	0	0	0	0	73	0	0	0	7	0	0	0	0	0	0	0	0	0	0	0	0	0	19  
        ......    
      2.Mapper Output:    
        A'SAM	546  
        A'SAM	565  
        A'SAM	585  
        A'SAM	621....  
      3.Reducer Output:  
        total  number of registered_voters in each settlement in 2013 is  
        A'SAM	3611  
        ABBIRIM	162  
        ABU  ABDUN	106  
        ABU GHOSH	3889    
        ABU JUWEI'ID	1443...  
      4.Language: Python  
      5.Chart: Pie chart  
      ![Average Votes.png](https://bitbucket.org/repo/oLnnya5/images/1917096981-Average%20Votes.png)


  **2.For each settlement_name, what is the average number of votes ?**  
      1.Mapper Input: 
        àáå â'ååééòã (ùáè	967	ABU JUWEI'ID	1	690	118	8	110	0	0	3	0	0	0	0	0	0	1	0	0	0	0	0	1	0	0	5	0	0	0	0	0	0	94	1	3	0	0	0	2......  
      2.Mapper Output: 
        ABU JUWEI'ID	118  
        ABU JUWEI'ID	99....  
      3.Reducer Output: 
        ABU JUWEI'ID,108.....  
      4.Language: Python  
      5.Chart: Bar Chart  
      ![Registered_votes.png](https://bitbucket.org/repo/oLnnya5/images/1917096981-Registered20%votes.png)   
      
      
  **3.For each settlement_name in 2013, calculate lowest number of votes?**  
      1.Mapper Input:  
        àáå âåù	472	ABU GHOSH	1	725	352	13	339	1	1	116	0	1	0	0	22	0	7	0	0	1	0	0	3	23	0	15	16	0	1	1	1	0	88	0	30	1	4	0	7  
        àáå âåù	472	ABU GHOSH	2	670	329	7	322	1	1	119	0	1	0	0	32	0	3	0	0	0	0	0	2	26	0	4	12	0	0	0	0	0	110	0	8	2	0	1	0  
        àáå âåù	472	ABU GHOSH	3	704	345	20	325	2	1	111	0	1	0	0	6	2	2	0	0	0	0	1	1	22	0	29	11	0	0	0	2	0	124	1	5	0	1	0	3  
        àáå âåù	472	ABU GHOSH	4	667	342	19	323	0	1	131	0	0	0	1	6	0	12	0	0	1	0	2	1	20	0	13	6	0	2	0	1	1	94	0	26	0	0	1	4  
        àáå âåù	472	ABU GHOSH	5	588	237	11	226	0	1	75	0	0	0	0	4	0	2	0	0	0	0	0	0	13	0	12	14	0	0	1	0	0	73	0	26	0	1	1	3  
        àáå âåù	472	ABU GHOSH	6	535	239	9	230	0	2	92	0	1	0	0	29	0	5	0	0	0	0	0	2	14	0	8	4	0	0	0	0	0	58	0	11	1	1	0	2 
      2.Mapper Output: Ale Yarok 4  
        Am Shalem  1  
          ......  
        Yesh Atid 14  
      3.Reducer Output: 
        Moreshet Avot,Leader, Kalkala, Eretz Hadasha are the parties got lowest number of votes in ABU GHOSH settlement in 2013  
      4.Language: Python  
      5.Chart: Sorted Bar Chart  
  
  
  **4.For each settlement_name,what is the average number of bad votes in 2013 israeli election?**   
      1.Mapper Input:  
        àáå â'ååééòã (ùáè	967	ABU JUWEI'ID	1	690	118	8	110	0	0	3	0	0	0	0	0	0	1	0	0	0	0	0	1	0	0	5	0	0	0	0	0	0	94	1	3	0	0	0	2  
        àáå â'ååééòã (ùáè	967	ABU JUWEI'ID	2	753	99	3	96	0	0	10	0	0	0	0	0	0	0	0	0	0	0	0	0	2	0	0	0	0	0	0	0	0	83	0	1	0	0	0	0  
        àáå âåù	472	ABU GHOSH	1	725	352	13	339	1	1	116	0	1	0	0	22	0	7	0	0	1	0	0	3	23	0	15	16	0	1	1	1	0	88	0	30	1	4	0	7  
        àáå âåù	472	ABU GHOSH	2	670	329	7	322	1	1	119	0	1	0	0	32	0	3	0	0	0	0	0	2	26	0	4	12	0	0	0	0	0	110	0	8	2	0	1	0  
        ...............................  
        ...............................  
        úøàáéï à-öàðò(éùå	1346	TARABIN AS-SANI	1	154	54	1	53	0	0	4	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	3	1	0	0	0	0	0	9	0	32	0	0	2	1  
        úøåí	778	TARUM	1	401	306	2	304	1	4	0	0	0	3	1	0	0	5	0	0	3	3	17	101	14	0	88	1	0	0	0	6	0	0	0	45	0	5	1	6  
      2.Mapper Output: 
        bad_votes 40896  
      3.Reducer Output: 
        Average number of bad votes in israeli election 2013 per settlement is 4 votes  
      4.Language: Python  
      5.Chart: Pie chart  