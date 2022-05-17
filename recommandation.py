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
from tqdm import tqdm
from PIL import Image
from data import *
from pandas import read_csv




df['location']= df['location'].astype(str)
companies = df["company"].unique().tolist()
# shuffle customer ID's
random.shuffle(companies)

# extract 90% of customer ID's
companies_train = [companies[i] for i in range(round(0.9*len(companies)))]

# split data into train and validation set
train_df = df[df['company'].isin(companies_train)]
validation_df = df[~df['company'].isin(companies_train)]

# list to capture purchase history of the customers
locations_train = []

# populate the list with the product codes
for i in tqdm(companies_train):
    temp = train_df[train_df["company"] == i]["location"].tolist()
    locations_train.append(temp)


# list to capture purchase history of the customers
location_val = []

# populate the list with the product codes
for i in tqdm(validation_df['company'].unique()):
    temp = validation_df[validation_df["company"] == i]["location"].tolist()
    location_val.append(temp)

# train word2vec model
model = Word2Vec(window = 10, sg = 1, hs = 0,
                 negative = 10, # for negative sampling
                 alpha=0.03, min_alpha=0.0007,
                 seed = 14)

model.build_vocab(locations_train, progress_per=200)

model.train(locations_train, total_examples = model.corpus_count, 
            epochs=10, report_delay=1)

model.save("word2vec_2.model")
model.init_sims(replace=True)
# extract all vectors
X = model.wv.index_to_key

jobs = train_df[["location", "jobTitle"]]

# remove duplicates
jobs.drop_duplicates(inplace=True, subset='location', keep="last")

# create product-ID and product-description dictionary
jobs_dict = jobs.groupby('location')['jobTitle'].apply(list).to_dict()
def similar_jobs(v, n = 6):
    
    # extract most similar products for the input vector
    ms = model.wv.similar_by_vector(v, topn= n+1)[1:]
    
    # extract name and similarity score of the similar products
    new_ms = []
    for j in ms:
        pair = (jobs_dict[j[0]][0], j[1])
        new_ms.append(pair)
        
    return new_ms 


google_word2vec = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin',binary=True)
google_model = Word2Vec(vector_size=300, window=5, min_count = 2, workers = -1)
google_model.build_vocab(corpus)
google_model.train(corpus, total_examples=google_model.corpus_count, epochs = 5)

def vectors(x):
    
    # Creating a list for storing the vectors (description into vectors)
    global word_embeddings
    word_embeddings = []

    # Reading the each book description 
    for line in df['cleaned']:
        avgword2vec = None
        count = 0
        for word in line.split():
            if word in google_model.wv.vocab:
                count += 1
                if avgword2vec is None:
                    avgword2vec = google_model[word]
                else:
                    avgword2vec = avgword2vec + google_model[word]
                
        if avgword2vec is not None:
            avgword2vec = avgword2vec / count
        
            word_embeddings.append(avgword2vec)

#Building TFIDF model and calculate TFIDF score

tfidf = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df = 5, stop_words='english')
tfidf.fit(df['cleaned'])

# Getting the words from the TF-IDF model

tfidf_list = dict(zip(tfidf.get_feature_names(), list(tfidf.idf_)))
tfidf_feature = tfidf.get_feature_names() # tfidf words/col-names

# Building TF-IDF Word2Vec 

# Storing the TFIDF Word2Vec embeddings
tfidf_vectors = []; 
line = 0;
# for each book description
for desc in corpus: 
  # Word vectors are of zero length (Used 300 dimensions)
    sent_vec = np.zeros(300) 
    # num of words with a valid vector in the book description
    weight_sum =0; 
    # for each word in the book description
    for word in desc: 
        if word in google_model.wv.key_to_index and word in tfidf_feature:
            vec = google_model.wv[word]
            tf_idf = tfidf_list[word] * (desc.count(word) / len(desc))
            sent_vec += (vec * tf_idf)
            weight_sum += tf_idf
    if weight_sum != 0:
        sent_vec /= weight_sum
    tfidf_vectors.append(sent_vec)
    line += 1

def recommendations(title):
    # finding cosine similarity for the vectors

    cosine_similarities = cosine_similarity(tfidf_vectors,  tfidf_vectors)
    
    # taking the title and book image link and store in new data frame called books
    jobs = df[['jobTitle','jobLocation']]
    #Reverse mapping of the index
    indices = pd.Series(df.index, index = df['cleaned']).drop_duplicates()
    idx = indices[title]
    sim_scores = list(enumerate(cosine_similarities[idx]))
    sim_scores = sim_scores[1:6]
    #sim_scores = sorted(sim_scores, key = lambda x: x[1], reverse = True)
    skill_indices = [i[0] for i in sim_scores]
    recommend = jobs.iloc[skill_indices]
    return  recommend

