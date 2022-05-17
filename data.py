# import csv

# def CSVReader(rows) :
# 	with open("C:\\Users\\Khadija\\Downloads\\data(2).csv",encoding='utf-8') as file:
# 	    csvreader = csv.reader(file)
# 	    header = next(csvreader)
# 	    for row in csvreader:
# 	        rows.append(row)
# 	return header

import pandas as pd
import numpy as np
import re
import shlex
import string
import gensim
import random
import nltk
nltk.download('stopwords')
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from gensim.models import Word2Vec
from gensim.models.phrases import Phrases, Phraser
from gensim.models import KeyedVectors
from PIL import Image
from pandas import read_csv
#*******************************************************************************
   #data definition
data = pd.read_csv(r'C:\Users\Khadija\Downloads\data(2).csv',na_values = "Missing", index_col=None)
df_survey_row = pd.read_excel("C:\\Users\\Khadija\\Documents\\Projet DS\\Data.xlsx", header=6, sheet_name="Raw Data" , index_col=None, usecols="B:T")
#data_survey = pd.read_csv(r'C:\Users\Khadija\Downloads\HUU_Tunisia_Alumni_Survey_Analysis__ESPRIT_2020_v1.csv',sep=';',encoding='latin',sheet_name="Raw Data")
df=pd.DataFrame(data)

df_survey = pd.read_excel("C:\\Users\\Khadija\\Downloads\\data_survey.xlsx", sheet_name="Tunisia_ESPRIT")
#*********************************************************************************
df_survey.drop(1,axis = 'rows', inplace =True)
selected_words=['Career advisement','Online job portal','Psychometric testing',"Mentorship","Virtual internships",'Interview preparation'
               ,'Career conferences and events','Job listings, placements and referrals','Networking events','CV and cover letter writing'
               ,'Decision-making support','Incubator integrated into the campus','Start-up workshops','Speaker series','Training around behavioral skills "Soft Skills"','Others, please specify']

Career_Advisement = df_survey.loc[df_survey['Q71_1'].isin(selected_words),'Q71_1'].value_counts(dropna=True)
Online_Job = df_survey.loc[df_survey['Q71_13'].isin(selected_words),'Q71_13'].value_counts(dropna=True)
Psychometric_testing = df_survey.loc[df_survey['Q71_11'].isin(selected_words),'Q71_11'].value_counts(dropna=True)
Mentorship = df_survey.loc[df_survey['Q71_4'].isin(selected_words),'Q71_4'].value_counts(dropna=True)
Virtual_internship = df_survey.loc[df_survey['Q71_14'].isin(selected_words),'Q71_14'].value_counts(dropna=True)
Interview_preparation = df_survey.loc[df_survey['Q71_5'].isin(selected_words),'Q71_5'].value_counts(dropna=True)
Career_conf_events =  df_survey.loc[df_survey['Q71_6'].isin(selected_words),'Q71_6'].value_counts(dropna=True)
job_listing = df_survey.loc[df_survey['Q71_7'].isin(selected_words),'Q71_7'].value_counts(dropna=True)
networking_events = df_survey.loc[df_survey['Q71_8'].isin(selected_words),'Q71_8'].value_counts(dropna=True)
Cv_conver_letter_writing = df_survey.loc[df_survey['Q71_9'].isin(selected_words),'Q71_9'].value_counts(dropna=True) 
Decision_making_support = df_survey.loc[df_survey['Q71_12'].isin(selected_words),'Q71_12'].value_counts(dropna=True) 
Incubator_integrated = df_survey.loc[df_survey['Q71_15'].isin(selected_words),'Q71_15'].value_counts(dropna=True)
startup_workshops = df_survey.loc[df_survey['Q71_16'].isin(selected_words),'Q71_16'].value_counts(dropna=True)
speaker_serie = df_survey.loc[df_survey['Q71_17'].isin(selected_words),'Q71_17'].value_counts(dropna=True)
Soft_skills = df_survey.loc[df_survey['Q71_18'].isin(selected_words),'Q71_18'].value_counts(dropna=True) 
Others = df_survey.loc[df_survey['Q71_10'].isin(selected_words),'Q71_10'].value_counts(dropna=True)
Needs = {"Career Advisement":Career_Advisement[0], 
       "Online job":Online_Job[0],
       "Psychometric testing":Psychometric_testing[0],
       "Mentorship": Mentorship[0],
       "Virtual internship": Virtual_internship[0],
       "interview preparation": Interview_preparation[0],
        "career conf": Career_conf_events[0], 
        "Job listing": job_listing[0], 
        "networking events": networking_events[0],
        "CV": Cv_conver_letter_writing[0],
        "Decision making": Decision_making_support[0],
        "Incubator":  Incubator_integrated[0],
        "startup workshop":startup_workshops[0],
       "speaker serie": speaker_serie[0], 
       "soft skill": Soft_skills[0],
       "others": Others[0]}

Current_Student_Status=df_survey['Q15'].value_counts().to_dict()
Current_Student_Status.pop('Which\nof the following best describes your employment status as of the day you\nare taking this survey? - Selected Choice')





#################################################################################################################################


#Recommandation 


#######################################################################################################################

df['Skills'] = df[df.columns[10:15]].apply(
    lambda x: ','.join(x.dropna().astype(str)),
    axis=1
)
#Utitlity functions for removing ASCII characters, converting lower case, removing stop words, html and punctuation from description

def _removeNonAscii(s):
    return "".join(i for i in s if  ord(i)<128)

def make_lower_case(text):
    return text.lower()

def remove_stop_words(text):
    text = text.split()
    stops = set(stopwords.words("english"))
    text = [w for w in text if not w in stops]
    text = " ".join(text)
    return text

def remove_html(text):
    html_pattern = re.compile('<.*?>')
    return html_pattern.sub(r'', text)

def remove_punctuation(text):
    tokenizer = RegexpTokenizer(r'\w+')
    text = tokenizer.tokenize(text)
    text = " ".join(text)
    return text

df['cleaned'] = df['Skills'].apply(_removeNonAscii)
df['cleaned'] = df.cleaned.apply(func = make_lower_case)
df['cleaned'] = df.cleaned.apply(func = remove_stop_words)
df['cleaned'] = df.cleaned.apply(func=remove_punctuation)
df['cleaned'] = df.cleaned.apply(func=remove_html)

corpus = []
for words in df['cleaned']:
    corpus.append(words.split())
 