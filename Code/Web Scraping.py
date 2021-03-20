import requests
import pandas as pd
from bs4 import BeautifulSoup
from time import sleep

##Section 1:scrape three companies data
#for specific explanation of each query key, please refer to the glossary in README
url_google = 'https://api.patentsview.org/patents/query?q={"_and":[{"assignee_organization":"Google Inc."},' \
       '{"_text_any":{"patent_abstract":"cloud"}}]}&f=["patent_number", "assignee_organization","inventor_city", ' \
       '"patent_processing_time", "cpc_group_id", "cpc_group_title", "citedby_patent_number", "cited_patent_number"]' \
       '&o={"matched_subentities_only": "true", "per_page": 1000, "include_subentity_total_counts": "false"}'
google_cloud = requests.get(url_google).json()

url_micro = 'https://api.patentsview.org/patents/query?q={"_and":[{"assignee_organization":"Microsoft Technology Licensing, LLC"},' \
       '{"_text_any":{"patent_abstract":"cloud"}}]}&f=["patent_number", "assignee_organization","inventor_city", ' \
       '"patent_processing_time", "cpc_group_id", "cpc_group_title", "citedby_patent_number", "cited_patent_number"]' \
       '&o={"matched_subentities_only": "true", "per_page": 1000, "include_subentity_total_counts": "false"}'
micro_cloud = requests.get(url_micro).json()

url_amazon = 'https://api.patentsview.org/patents/query?q={"_and":[{"assignee_organization":"Amazon Technologies, Inc."},' \
       '{"_text_any":{"patent_abstract":"cloud"}}]}&f=["patent_number", "assignee_organization","inventor_city", ' \
       '"patent_processing_time", "cpc_group_id", "cpc_group_title", "citedby_patent_number", "cited_patent_number"]' \
       '&o={"matched_subentities_only": "true", "per_page": 1000, "include_subentity_total_counts": "false"}'
amazon_cloud = requests.get(url_amazon).json()

#using assignee API: patent data, inventor data and assignee innovation information
url2_micro = 'https://api.patentsview.org/assignees/query?q={"_begins":{"assignee_organization":"Microsoft Technology Licensing, LLC"}}' \
           '&f=["patent_number","patent_date","assignee_organization","assignee_id",' \
           '"inventor_first_name","patent_num_combined_citations","assignee_lastknown_city",' \
           '"patent_date","assignee_total_num_inventors","assignee_total_num_patents",' \
           '"inventor_location_id","patent_kind","patent_abstract"]'
t = requests.get(url2_micro).json()

#save the data into json
json_file = "C:/Users/Louisa Zhao/Desktop/CS project/Microsoft.json"
with open(json_file,"w") as f:
    json.dump(t.json(),f)

url2_google = 'https://api.patentsview.org/assignees/query?q={"_begins":{"assignee_organization":"Google Inc."}}' \
           '&f=["patent_number","patent_date","assignee_organization","assignee_id",' \
           '"inventor_first_name","patent_num_combined_citations","assignee_lastknown_city",' \
           '"patent_date","assignee_total_num_inventors","assignee_total_num_patents",' \
           '"inventor_location_id","patent_kind","patent_abstract"]'
t = requests.get(url2_goolge).json()

#save Google data into json
json_file = "C:/Users/Louisa Zhao/Desktop/CS project/Google.json"
with open(json_file,"w") as f:
    json.dump(t.json(),f)

#save Microsoft data into json
url2_micro = 'https://api.patentsview.org/assignees/query?q={"_begins":{"assignee_organization":"Microsoft Technology Licensing, LLC"}}' \
           '&f=["patent_number","patent_date","assignee_organization","assignee_id",' \
           '"inventor_first_name","patent_num_combined_citations","assignee_lastknown_city",' \
           '"patent_date","assignee_total_num_inventors","assignee_total_num_patents",' \
           '"inventor_location_id","patent_kind","patent_abstract"]'
t = requests.get(url2_micro).json()

#save  Microsoft data into json
json_file = "C:/Users/Louisa Zhao/Desktop/CS project/Google.json"
with open(json_file,"w") as f:
    json.dump(t.json(),f)

#save Microsoft data into json
url2_amazon = 'https://api.patentsview.org/assignees/query?q={"_begins":{"assignee_organization":"Amazon Technologies, Inc."}}' \
           '&f=["patent_number","patent_date","assignee_organization","assignee_id",' \
           '"inventor_first_name","patent_num_combined_citations","assignee_lastknown_city",' \
           '"patent_date","assignee_total_num_inventors","assignee_total_num_patents",' \
           '"inventor_location_id","patent_kind","patent_abstract"]'
t = requests.get(url2_amazon).json()

#save  Microsoft data into json
json_file = "C:/Users/Louisa Zhao/Desktop/CS project/Amazon.json"
with open(json_file,"w") as f:
    json.dump(t.json(),f)


##Section 2:scrape three companies' citation data
#scrape cited and citation data
#get cited_patent_num
def get_patent_num(patent_dict):
    '''
    This function is to extract the citedby patents' number
    from original patents dictionaries
    '''
    num_list = []
    for i in range(len(patent_dict['patents'])):
        if 'cited_patents' in patent_dict['patents'][i]:
            cite_list = patent_dict['patents'][i]['cited_patents']
            for j in range(len(cite_list)):
                c = patent_dict['patents'][i]['cited_patents'][j]['cited_patent_number']
                if c != None:
                    num_list.append(c)
    return num_list

def get_cited_company(num_list,total_list):
    '''
    This function is to extract cited company
    Inputs:
        num_list: list of company
        total_list:list save all data
    return a list of cited company
    '''
    url_1 = 'https://api.patentsview.org/patents/query?q={"_and":[{"patent_number":'
    url_2 = '}]}&f=["assignee_organization"]'
    url = ''
    cited_company_list = []
    for num in num_list:
        url = url_1+num+url_2
        a = requests.get(url).json()
        if 'status' in a:
            continue
        if a['patents'] == None:
            continue
        else:
            company = a['patents'][0]['assignees'][0]['assignee_organization']
            cited_company_list.append(company)
            total_list.append(company)

    return cited_company_list


#Section 3: get citedby data
#cited by
def get_cite_num(patent_dict):
    '''
    This function is to extract the citedby patents' number
    from original patents dictionaries
    '''
    num_list = []
    for i in range(len(patent_dict['patents'])):
        cite_list = patent_dict['patents'][i]['citedby_patents']
        for j in range(len(cite_list)):
            c = patent_dict['patents'][i]['citedby_patents'][j]['citedby_patent_number']
            if c != None:
                num_list.append(c)
    return num_list

#output the cited data into txt
micro_cite_num_list = get_patent_num(micro_cloud)
company_micro = get_cited_company(micro_cite_num_list)
#output the citedby data into txt
micro_num_list = get_cite_num(micro_cloud)
micro_cited_company = get_cited_company(micro_num_list)

#save citation data into txt
with open('Microsoft cited patent.txt','w',encoding='utf-8') as output:
    for c in company_micro:
        output.write(str(c)+'\n')

google_cite_num_list = get_patent_num(google_cloud)
company_google = get_cited_company(google_cite_num_list)
#output the citedby data into txt
google_num_list = get_cite_num(google_cloud)
google_cited_company = get_cited_company(google_num_list)

#save citation data into txt
with open('Google cited patent.txt','w',encoding='utf-8') as output:
    for c in company_micro:
        output.write(str(c)+'\n')

amazon_cite_num_list = get_patent_num(amazon_cloud)
company_google = get_cited_company(amazon_cite_num_list)
#output the citedby data into txt
amazon_num_list = get_cite_num(amazon_cloud)
amazon_cited_company = get_cited_company(google_num_list)

#save citation data into txt
with open('Amazon cited patent.txt','w',encoding='utf-8') as output:
    for c in company_micro:
        output.write(str(c)+'\n')


##Section 4: second round citation scraping
file = "Cited patent.txt" #open first round citation file
data = pd.read_csv(file,sep = "\n",header = None, names = ['target']) #import data into pandas
data_lst = data.values.tolist() #clean data in the DataFrame into list

company = ['Microsoft Technology Licensing, LLC', 'Google Inc.', 'Amazon Technologies, Inc.', 'None']
scrape_lst = []
for i in data_lst:
    for j in i:
        if j not in scrape_lst and j not in company: #exclude the target companies data
            scrape_lst.append(j)

#Scrape company's data
total_list=[] #save total citation company's data as a list of tuple
#organized it into function
def organization_patent(scrape_lst,total_list):
    '''
    This function is used to scrape the company's data
    Input:
        scrape_lst: a list of string
        total_list: the total list containing the company and cited company
    '''
    for i in scrape_lst:
        company_total_list = []
        url1 = 'https://api.patentsview.org/patents/query?q={"_and":[{"assignee_organization":"'
        company = i
        url2 = '"},{"_text_any":{"patent_abstract":"cloud"}}]}&f=["patent_number", "patent_title","assignee_organization","citedby_patent_title","citedby_patent_number","cited_patent_number","citedby_patent_category"]&o={"matched_subentities_only": "true", "per_page": 10000, "include_subentity_total_counts": "false"}'
        url = url1+company+url2
        micro_cloud = requests.get(url).json()
        #print(micro_cloud)
        if micro_cloud['patents'] != None:
            num_list = get_patent_num(micro_cloud)
            get_cited_company(company,num_list,company_total_list)
            total_list.append(company_total_list)
            df = pd.DataFrame(data = company_total_list)
            df.to_csv("C:/Users/Louisa Zhao/Desktop/CS project/second round citation.csv",mode = 'a',encoding = 'utf-8')
    return total_list

return_list = organization_patent(scrape_lst,total_list)

##Section 5: Scraping cloud business related assignee data into json file
url1 = 'https://api.patentsview.org/assignees/query?q={"_begins":{"assignee_organization":"ALCLEAR, LLC"}}&f=["patent_number","patent_date","assignee_organization","assignee_id","inventor_first_name","patent_num_combined_citations","assignee_lastknown_city","patent_date","assignee_total_num_inventors","assignee_total_num_patents","inventor_location_id","patent_kind","patent_title","patent_abstract"]'
output1 = requests.get(url1).json()
ALC.json = "/Users/QianYi/Desktop/ALC.json"
with open(ALC.json, "w") as f:
    json.dump(output1, f)

url2 = 'https://api.patentsview.org/assignees/query?q={"_begins":{"assignee_organization":"Oracle International Corporation"}}&f=["patent_number","patent_date","assignee_organization","assignee_id","inventor_first_name","patent_num_combined_citations","assignee_lastknown_city","patent_date","assignee_total_num_inventors","assignee_total_num_patents","inventor_location_id","patent_kind","patent_title","patent_abstract"]'
output2 = requests.get(url2).json()
Oracle.json = "/Users/QianYi/Desktop/Oracle.json"
with open(Oracle.json, "w") as f:
    json.dump(output2, f)

url3 = 'https://api.patentsview.org/assignees/query?q={"_begins":{"assignee_organization":"Sonos, Inc."}}&f=["patent_number","patent_date","assignee_organization","assignee_id","inventor_first_name","patent_num_combined_citations","assignee_lastknown_city","patent_date","assignee_total_num_inventors","assignee_total_num_patents","inventor_location_id","patent_kind","patent_title","patent_abstract"]'
output3 = requests.get(url3).json()
Sonos.json = "/Users/QianYi/Desktop/Sonos.json"
with open(Sonos.json, "w") as f:
    json.dump(output3, f)

url4 = 'https://api.patentsview.org/assignees/query?q={"_begins":{"assignee_organization":"Intuit Inc."}}&f=["patent_number","patent_date","assignee_organization","assignee_id","inventor_first_name","patent_num_combined_citations","assignee_lastknown_city","patent_date","assignee_total_num_inventors","assignee_total_num_patents","inventor_location_id","patent_kind","patent_title","patent_abstract"]'
output4 = requests.get(url4).json()
Intuit.json = "/Users/QianYi/Desktop/Intuit.json"
with open(json_file, "w") as f:
    json.dump(output4, f)

url5 = 'https://api.patentsview.org/assignees/query?q={"_begins":{"assignee_organization":"Akamai Technologies, Inc."}}&f=["patent_number","patent_date","assignee_organization","assignee_id","inventor_first_name","patent_num_combined_citations","assignee_lastknown_city","patent_date","assignee_total_num_inventors","assignee_total_num_patents","inventor_location_id","patent_kind","patent_title","patent_abstract"]'
output5 = requests.get(url5).json()
Akamai.json = "/Users/QianYi/Desktop/Akamai.json"
with open(Akamai.json, "w") as f:
    json.dump(output5, f)

url6 = 'https://api.patentsview.org/assignees/query?q={"_begins":{"assignee_organization":"Cisco Technology, Inc."}}&f=["patent_number","patent_date","assignee_organization","assignee_id","inventor_first_name","patent_num_combined_citations","assignee_lastknown_city","patent_date","assignee_total_num_inventors","assignee_total_num_patents","inventor_location_id","patent_kind","patent_title","patent_abstract"]'
output = requests.get(url7).json()
Cisco.json = "/Users/QianYi/Desktop/Cisco.json"
with open(Cisco.json, "w") as f:
    json.dump(output6, f)

url7 = 'https://api.patentsview.org/assignees/query?q={"_begins":{"assignee_organization":"Intel Corporation"}}&f=["patent_number","patent_date","assignee_organization","assignee_id","inventor_first_name","patent_num_combined_citations","assignee_lastknown_city","patent_date","assignee_total_num_inventors","assignee_total_num_patents","inventor_location_id","patent_kind","patent_title","patent_abstract"]'
output7 = requests.get(url7).json()
Intel.json = "/Users/QianYi/Desktop/Intel.json"
with open(Intel.json, "w") as f:
    json.dump(output7, f)
