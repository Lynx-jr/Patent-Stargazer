import requests
import pandas as pd
from bs4 import BeautifulSoup
from time import sleep
from os import chdir
from glob import glob

'''
put assignee data into a csv file
'''
def assignee(file):
    f = open(file)
    data = json.load(f)
    assignee_data = list(data['assignees'][0].items())
    d = {}
    for i in assignee_data[0:5]:
        a = []
        a.append(i[1])
        d[i[0]] = a
    df = pd.DataFrame(data=d)
    df.to_csv('assignee.csv',index=False)

'''
put inventors data into a csv file
'''
def inventor(file):
    f = open(file)
    data = json.load(f)
    inventors_data = data['assignees'][0]['inventors']
    df = pd.DataFrame(data=inventors_data,index=None)
    df.to_csv('inventors.csv',index=False)

'''
put patent data into a csv file
'''
def patent(file):
    f = open(file)
    data = json.load(f)
    patents_data = data['assignees'][0]['patents']
    df = pd.DataFrame(data=patents_data,index=None)
    df.to_csv('patents.csv',index=False)

'''
merge to one cvs file
'''
# Produce a single CSV after combining all files
def produceOneCSV(list_of_files, file_out):
   # Consolidate all CSV files into one object
   result_obj = pd.concat([pd.read_csv(file) for file in list_of_files])
   # Convert the above object into a csv file and export
   result_obj.to_csv(file_out, index=False, encoding="utf-8")

# Move to the path that holds our CSV files
csv_file_path = '/Users/QianYi/Desktop/patents'
chdir(csv_file_path)

# List all CSV files in the working dir
file_pattern = ".csv"
list_of_files = [file for file in glob('*.{}'.format(file_pattern))]
print(list_of_files)

file_out = "ConsolidateOutput.csv"
produceOneCSV(['ALC.csv','Sonos.csv'], file_out)


