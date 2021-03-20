import requests
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np  
import matplotlib.mlab as mlab  
import matplotlib.pyplot as plt  
import seaborn as sns
import math
from pandas import DataFrame

#Section 1: Scrape 1st round with patents api
urlg = 'https://api.patentsview.org/patents/query?q={"_and":[{"assignee_organization":"Google Inc."},{"_text_any":{"patent_abstract":"cloud"}}]}&f=["inventor_city","patent_processing_time", "cpc_group_id", "cpc_group_title"]&o={"matched_subentities_only": "true", "per_page": 1000, "include_subentity_total_counts": "false"}'
google_cloud = requests.get(urlg).json()
urlm = 'https://api.patentsview.org/patents/query?q={"_and":[{"assignee_organization":"Microsoft Technology Licensing, Llc"},{"_text_any":{"patent_abstract":"cloud"}}]}&f=["inventor_city","patent_processing_time", "cpc_group_id", "cpc_group_title"]&o={"matched_subentities_only": "true", "per_page": 1000, "include_subentity_total_counts": "false"}'
microsoft_cloud = requests.get(urlm).json()
urla = 'https://api.patentsview.org/patents/query?q={"_and":[{"assignee_organization":"Amazon Technologies, Inc."},{"_text_any":{"patent_abstract":"cloud"}}]}&f=["inventor_city","patent_processing_time", "cpc_group_id", "cpc_group_title"]&o={"matched_subentities_only": "true", "per_page": 1000, "include_subentity_total_counts": "false"}'
amazon_cloud = requests.get(urla).json()

#Section 2: Visualize Inventor's city
def inventor_city_stats(cloud_dict):
    '''
    This function generates a dataframe object that match cities to occurences.
    
    Input:
    cloud_dict: the patents dictionary, contains the inventor city we are interested in
    Output:
    inventor_city_df: dataframe object, keys of cities, values of inventor city counts     
    '''
    patents = cloud_dict['patents']
    inventor_city_list = []
    inventor_city_dict = {}
    for i in patents:
        single_p_inventors_list = i['inventors']
        for j in single_p_inventors_list:
            inventor_city_list.append(j['inventor_city'])
    
    for i in inventor_city_list:
        if i not in inventor_city_dict:
            inventor_city_dict[i] = 1
        else:
            inventor_city_dict[i] += 1
    inventor_city_df = pd.DataFrame(pd.Series(inventor_city_dict), columns = ['inventor_city_count'])
    inventor_city_df = inventor_city_df.reset_index().rename(columns = {'index': 'city'})   
    inventor_city_df['city'] = inventor_city_df['city'].astype('str') 
    
    return inventor_city_df

def inventor_city_viz(c, company_name):
    '''
    This function serves to visualize the inventor's cities, in particular their relative numbers \
    to observe which city has the most inventors.
    Input:
    c: (dataframe) dataframe from the last step
    company_name: (str) '' Note that the quotation marks must be included
    Output:   
    Picture file: (png) Cities with the most Inventors
    '''
    f, ax=plt.subplots(figsize=(8,4))
    d = sns.barplot(c.city, c.inventor_city_count, palette="BuPu_r", \
                    order=c.sort_values('inventor_city_count', ascending = False).iloc[:15].city)
    plt.title('Cities with the most Inventors', fontsize = 10)
    plt.xlabel('City', fontsize = 8)
    plt.ylabel('Inventors', fontsize = 8)
    d.set_xticklabels(ax.get_xticklabels(), rotation = 30, fontsize = 8)
    plt.xticks()
    plt.yticks(fontsize=15)
    sns.despine()
    plt.show();
    fig = d.get_figure()
    fig.savefig('{}_inventor_city_pic.png'.format(company_name), dpi = 400)

g = inventor_city_stats(google_cloud)
a = inventor_city_stats(amazon_cloud)
m = inventor_city_stats(microsoft_cloud)

inventor_city_viz(g, 'Google')
inventor_city_viz(a, 'Amazon')
inventor_city_viz(m, 'Microsoft')

#Section 3: Visualize the processing time of a single patent
def processing_time_vis(cloud_data):
    '''
    Calculate and visualize the time from filing application date to grant date for the patent.
    
    Input:
    cloud_data: (dict) The patent dictionary
    Output:
    Picture
    '''
    time_lst = []
    index = []
    time_c_lst = []
    for i in cloud_data["patents"]:
        a = int(i["patent_processing_time"])
        time_lst.append(a/365)
        time_c_lst.append(math.floor(a/365))
    
    time_df = DataFrame({'processing_time' : time_lst, 'time_c' : time_c_lst})
    time_df.processing_time.plot.hist(grid=False,rwidth=0.9,color='#607c8e')
    plt.title('Number of Patents')
    plt.ylabel('Patent Counts')
    plt.xlabel('Processing time in years')

processing_time_vis(google_cloud)
processing_time_vis(amazon_cloud)
processing_time_vis(microsoft_cloud)

#Section 4: Visualize the CPC category for each company

def get_cpc_id(info,n):
    '''
    This function aims to count the cpc categories for each company
    Input:
        info: dict,scraping output as json object
        n: int,the number to select the most top n cpc category
    output:
        return a sorted dictionary of cpc category 
        '''
    total_id_dict = {}
    total_id_list = []
    top_dict = {}
    for i in range(len(info)):
        sub_info = info[i]['cpcs']
        for j in range(len(sub_info)):
            group_id = sub_info[j]['cpc_group_id']
            total_id_list.append(group_id)
            
    for i in total_id_list:
        if i != None:
            total_id_dict[i] = total_id_dict.get(i,0)+1
    
    sort_total = {key:val for key,val in sorted(total_id_dict.items(),key=lambda item:item[1],reverse = True)}
    
    new_total = {}
    num = 0
    for key,values in sort_total.items():
        num += 1
        if num < n:
            new_total[key] = values
    
    return new_total

def viz_class(viz_dict,company):
    '''
    This function is to visualize the company cpc category into a barplot
    Input:
        viz_dict: the sorted dictionary containing cpc categories
        company: a string of company's name
    '''
    x = [key for key,values in viz_dict.items()]
    y = [values for key,values in viz_dict.items()]
    plt.subplots(figsize = (5,4,5))
    sns.barplot(x, y,palette = "BuPu_r")
    title_viz = "{} Cloud Patents Classification".format(company)
    plt.title(title_viz,fontdict= { 'fontweight':'bold'})
    plt.xticks(rotation=90)

#extract patents data from scraping json file
#obtain sorted list of patent number

google_info = google_cloud['patents']
viz_dict_g = get_cpc_id(google_info,11)

micro_info = google_cloud['patents']
viz_dict_m = get_cpc_id(micro_info,11)

amazon_info = amazon_cloud['patents']
viz_dict_a = get_cpc_id(amazon_info,11)

# viz three barplot according to the cpc category data
viz_class(viz_dict_g,"Google")
viz_class(viz_dict_m,"Microsoft")
viz_class(viz_dict_a,"Amazon")

