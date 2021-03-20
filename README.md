# final-project-boom-shaka-laka
## Patent Stargazer
final-project-boom-shaka-laka created by GitHub Classroom

Project “Patent Stargazer”

-- Developers' Foreword --\
We really hope you could be able to run and play with the app. If you cannot run the app after the instruction below, please do reach out to us to assist you in successfully running the app. We could be contacted at:

#########################################\
ZHAO Chuqing: cqzhao@uchicago.edu\
QIAN Yi: yiq@uchicago.edu\
LIU Yingxuan: yingxuan@uchicago.edu\
#########################################

-- Context --\
I. How to run our app and play with it\
II. Introduction to our code\
  A. an overview of our code structure\
  B. Brief introduction to each section\
  C. People in charge of each section\
III. Detailed information and analysis about the project\

## I. How to run our app and play with it (IMPORTANT)

### A.	Python packages required to run the app (please use Python3)
i) jupyter notebook\
ii) tkinter\
iii) PIL\
(You will not need internet connection since we have pre-assembled everything within the tkinter.)

### B.	If you want to change another company for visualization for your own use:
i) For scraping: requests, bs4, pandas, time\
ii) For legal status: pyecharts\
iii) For processing time, inventor city, and CPC: numpy, matplotlib, math, seaborn, pandas\
iv) For network analysis: \
v) For word cloud: \
vi) For interface: tkinter, PIL

### C. How to run the app and what are its features
i) Download our folder "Patent_stargazer" into your local directory\
ii) Open the jupyter notebook file under the directory path\
iii) Simply run the whole notebook.\
iv) You can see buttons with “Microsoft”, “Google”, “Amazon”, and if you click on any of them, their corresponding visualizations appears.\
v) (Optional) You may copy part of our code into your own Python editor and conduct analysis based on your interest

## II. An introduction to our code 

### A.	An overview of our code structure
Our project folder is divided into 6 relevant files:
1. Web Scraping (approx. 255 lines)
2. time_city_cpc (approx. 173 lines)
3. Legal Status Viz (approx. 50 lines)
4. Network data.ipynb (approx. 190 lines)
5. NLP.ipynb (approx. 210 lines)
6. Patent Stargazer App.ipynb (approx. 176 lines)

### B.	Brief introduction to each section
1. Web Scraping: this file aims to obtain relational data from USPTO PatentsView database, including company's cloud computing-related patents, patent date, patent citation information, CPC, patent processing time, legal status, city and inventor's information.
2. time_city_cpc: this file is to analyze the average processing time for patent in each targeted company, inventors location distribution and patent's classification. 
3. Legal Status Viz: this file is to analyze and visualize the legal status of total patents in each targeted company.
4. Network data: this file is to build, analyze and visualize network of companies. It includes cleaning patents' data into nodes and edges, analyze the statistical properties and draw subgraphs for targeted companies.
5. NLP: this file is to conduct text analysis on company's patent abstract. Text cleaning and word clouds visualization are included.
6. Patent Stargazer: this file is to build the interface of three companies. It includes the functions of interface visualization and organizes data visualization.

### C.	People in charge of each section
Chuqing Zhao:
1) Web scraping for patent data, citation data, CPC classification data and patents’ abstract data into json file
2) Clean, organize cloud computing related patents from original json files to csv
3) Responsible for CPC classification analysis and data visualization
4) Network analysis, including creating network, statistical properties, robustness check and visualization
5) NLP: cleaning text data and making word cloud for each targeted company
6) Part of README report (network analysis and NLP part), code and data merge

Yi Qian:
1) Scrape patent data for network analysis 
2) Clean, organize data, and save results to csv files
3) Conduct patent processing time analysis and visualization
4) Responsible for part of README report
5) Merge csv data and data cleaning code 
6) Make slides related to processing time, city and cpc analysis 

Yingxuan Liu:
1) Responsible for the idea, part of the project planning, and relevant quality control
2) Download and scraped for patent data, citation data, CPC classification data and patents’ abstract data into json file from incoPat and the APIs
3) Clean, organize cloud computing related patents from original json files to csv
4) Responsible for legal status analysis, inventor city analysis and correlated visualization
5) Patent Stargazer App: Designed the GUI interface
6) Responsible for building the slides and README report structure, conduct code and data merge, and final editing

## III. Detailed information and analysis about the project 

### A.	Background:

Patents have several advantages as a “technology indicator.” In addition to being public information, patents provide a wealth of detailed information, comprehensive coverage of technologies and countries, a relatively standardized level of invention, and long time-series of data. Until recently, however, significant questions hindered more extensive use of patent data by corporate technology managers. The chief question concerned the validity of patent data as a measure of technology. Another frequently expressed concern was that patents vary widely in their importance, which is not reflected in simple patent counts. Analysts have also been concerned about patent data's timeliness and the utility of existing patent technology classifications.

Our project aims to answer a series of questions regarding the characteristics of patents from particular companies. We are interested in using patent data for technical analysis and planning and will explore in our project "Patent Stargazer“ with a focus on cloud computation patents. The output of this project, a miniature tool, helps us to visualize our findings. This tool and relevant code offer patent enthusiasts a way to have similar or custom-made visualizations comparing to EXTREMELY COSTLY databases such as Derwent and incoPat (From Yingxuan’s own working experience). Our tool and codes have a significant advantage comparing with such database accounts, which often cost thousands of dollars per year, and most of its services are not used in the daily analysis.

### B.	Data:

The raw data is from four sources: 
We scraped data from the official website of United States Patent and Trademark office’s (USPTO) PatentsView application programming interface (API), by which we obtained detailed and organized information about patents. This API provides web developers and researchers programmatic access to longitudinal data and metadata on patents, inventors, companies, and geographic locations. We chose the cloud technology field to conduct the study. Having a background such that Amazon Web Services, Miscrosoft Azure, and Google Cloud Platform are leading cloud providers, and for the ease of analysis, we started from scraping the patent data of Amazon Technologies Inc., Microsoft Technology Licensing, Llc., and Google Inc.. The two APIs we have used are as follow:

1) PatentsView Patent API
2) PatentsView Assignee API

Please refer to section C – Glossary, to check the key terms scraped for further analysis in our study.

3) incoPat Global Patent Database – This part of data is used for legal status, the USPTO API does not offer current legal status and if a patent is invalid or undetermined, it usually appears as a Null inside the patents dictionary. This data is manually sorted out into a dictionary form since there wasn’t too much data but is still crucial for the analysis.

### C.	Glossary

**Table 1. Terms about an assignee—the owner of the patent**

|	  | Terms	| Description |
|---|-------|-------------|
|1	|assignee organization|	the name of the entity that owns the patent|
|2	|assignee id| the unique id of the entity|
|3	|assignee last known city| Inventor's city as of their most recent patent grant date|
|4	|assignee total number inventor| Total number of inventors in assignee|
|5	|assignee total number patents|	Total number of patents in assignee|

**Table 2. Terms about a patent**
|	  | Terms	| Description |
|---|-------|-------------|
|1	|patent number| US Patent number, as assigned by USPTO|
|2	|patent date|	Date patent was granted|
|3	|patent kind|	World Intellectual Property Organization (WIPO) Standard ST.16 Patent Code|
|4	|patent title| Title of the patent|
|5	|patent abstract| Abstract of the patent|
|6	|patent number combined citations| Number of patents and applications cited by the selected patent. This is the sum of citations of US patents, foreign patents, and US applications|
|7	|patent processing time| Time from filing application date to grant date for the patent|

**Table 3. Terms about an inventor—the individual who conceived the invention**
|	  | Terms	| Description |
|---|-------|-------------|
|1	|inventor first name|	Inventor first name|
|2	|inventor location id|	Inventor spatial location information|

**Table 4. Terms about the citation situation of the patent**
|	  | Terms	| Description |
|---|-------|-------------|
|1	|cited by patent title|	Title of citing patent|
|2	|cited by patent number|	Patent number of citing patent|
|3	|cited by patent category|	Category of citing patent|
|4	|cited patent title|	Title of cited patent|
|5	|cited patent number| Patent number of citing patent|

**Table 5. Terms about Cooperative Patent Classification (CPC)**
|	  | Terms	| Description |
|---|-------|-------------|
|1	|cpc group id|	CPC group ID|
|2	|cpc group title|	Description of CPC group|


*Note: A hierarchical patent classification scheme developed through a joint partnership between the USPTO and the European Patent Office (EPO) to harmonize and replace each office’s individual classification system, the US Patent Classification (USPC) and the European Classification (ECLA). The USPTO formally launched the CPC system in January 2013.

### D．Project Structure:

Our project is constituted by three parts: first of all, we conducted statistical analysis about the patent processing time, legal status of patent, patent geological distribution as well as patent classification. Second, we used network analysis to examine the market structure through various network metrics and visualization.Third,  we analyzed the patents' abstracts by NLP techniques.

**Patent Processing Time**

The processing time calculates the duration from the application date to the approval date. The distribution of patent processing time is roughly similar to Amazon, Microsoft, and Google. They all have right-tailed distribution. Though several pieces of patents take a long processing time, such as eight years or even longer, most patents take less than five years to be approved. The average processing time is approximately between 2 to 3 years. The processing time of most patents applied by these three companies also belongs to this interval. The average patent processing time in the United States is 25 months. We can see that the cloud technology patent application processing is relatively stable, not too slow or too fast. Such a pattern allows cloud technologies and services to develop at a stable speed as well.

**The Legal Status**

The legal status contains at least four categories under different taxonomies. Here we used incoPat’s categorization, dividing the patents’ legal status into Valid, Unconfirmed, Invalid, Lapse after granting. Although the total number of available patents varies, we can still observe patterns within each company’s legal status. Google has the highest portion of valid patents, and Microsoft has the least portion. There is still room for improvement for both companies. Part of the reason that Microsoft has the least portion was that it has the highest patent amount, and Google has the lowest number of cloud computation patents. Combining with the patent processing time, we can observe that Google has a taller pillar comparing with the other two during 1-2 yrs. This evidence showed that the lack of patents had forced Google to take a relatively radical stance for applications, either by litigation or acquiring other companies’ patents.

**Inventor’s City Location**

From the inventor’s geological distribution statistics, we can see that most inventors come from tech-heavy cities in coastal areas. We expect such a pattern is typical in the technology field. If an individual is interested in becoming an inventor for any of those companies, our list would be a good reference. This distribution also contributes to how automation risk varies within different regions, cities, and states. The cities with the most inventors may have the most technology-related labor force and tech-encouraging policies. Those cities also adapt best to technological transitions. On the contrary, Heartland states and cities may be the most vulnerable to such risk.

**Patent Classification**

The distribution of patent classification is also similar among these three leading companies. From the bar chart, we can see that most patents belong to the G06F or H04L category. The former is the electric digital data processing, and the latter is the transmission of digital information. Amazon and Google should take measures from research and development strategy, patent mining strategy, patent application strategy, and many other aspects to enhance the quality control and internal audit of patent application technical scheme to improve the authorization amount of its patent application. Moreover, Amazon’s statistics may also show that its patent layout strategy has a certain focus in terms of specific categories (H04L). Before further analysis about patent abstract to explore detailed content of these patents, we assume that these leading companies have been developing cloud technologies in a similar direction.

**Network Analysis**

To understand the cloud computing market structure, we collect the citation information from the UPSTO API. The data collection procedure follows a snowball sampling method. We first collected the two dimensions of citation information from API: first is the company’s names of cited patents, and second is the company’s names of patents that have been cited by target companies. After collecting the first round of directed citation data, we used the same method to collect the citation information from the first-round scraping companies. In our dataset, we have gathered around 8,000 pairs of citation pairs, covering almost 200 cloud computing companies. 

Then, we clean the data by using pandas dataframe and build a directed citation network by NetworkX and Gephi. We browse the overview of networks and look at the network property. First, we use the modularity algorithm to cluster the nodes into five communities in different colors. Then, we find that the degree distribution follows a power-law distribution, meaning there are few companies have higher citation rate than average companies. In the graph, we can see the nodes with higher degrees are Symantec, Adobe, Lockheed Martin Corporation, and QUANTA Computer. Next, we use different centrality measures, including betweenness centrality, eigenvector centrality, degree centrality, and pagerank score. Results show that Microsoft, Cisco, and Symantec are the top three companies in the central position of the graph. 

Next, the results show that the citation network follows a “small world effect”. In the citation graph, the average length path is around 1, meaning that a certain company could reach another only by one node length. To check the robustness of smallworldness, we compared the network with an equivalent random network with the same number of nodes. It implies the network has certain hubs that connect most companies with high degrees and are more able to generate innovation than average companies.

Next, we examine the subgraph and plot the directed network of the top three companies with the highest degrees. Microsoft, Symantec, and Lockheed. Compared subgraph 1 and subgraph 2, we find Microsoft and Symantec are very closed to each other. Interestingly, we find the companies with the highest market shares are not companies that have more citations and more innovation of cloud computing techniques. It implies that middle and small size companies like Symantec are more expertized in cloud computing, but its business is not competitive as the big-name companies like Amazon and Google.

**Natural Language Processing**

We further provide a fine-grained analysis of patent abstracts by using natural language processing techniques. To clean text, we first do tokenization and remove all punctuation and stop words by SpaCy packages. We do lemmatization to convert each word into base form and part-of-speech tagging, keeping noun (NN) and verb (VB) in base form. To visualize the word frequency, we make word clouds for each of the three targeted companies. From the results, we notice that although all three companies focus on cloud computing services, the products are quite different. 

## E. Conclusion

Indeed, since not all inventions are patented, the method cannot be used to compile a comprehensive inventory of all firms active in a particular technology or all developments in a field. Our data collection is flawed in some sense because we did not combine the patents in the same family as well as considering sub-companies of those conglomerates. However, the patent analysis can still provide strong hints about firms’ research and development on technologies. The statistical analysis of patent records is a valid approach to assessing the development of technologies. The method is particularly useful in sketching the “big picture” of activity in a technology—including past trends and the life cycle stage. The network analysis provides an overview of the market structure consisting of small-size innovative companies and big-name companies with top market shares. Findings show that innovation can not be equal to high market shares. Because in the graph we find some small-sized companies have more leading technology with relatively high citation rates than big companies. Although those small-size companies take a small proportion of total market shares, they enjoy high innovation levels with cutting-edge techniques. For those big companies, their cloud computing services are mature and diverse, even though they do not have leading reach and development. From the word clouds, we can see the slight difference in each big company. However, Microsoft, an outlier with high innovation and a large part of market shares, is often at the central position in the market network.


