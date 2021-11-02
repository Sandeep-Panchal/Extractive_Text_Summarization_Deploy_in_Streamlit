import numpy as np
import streamlit as st
import pandas as pd
# import nltk
# from nltk.tokenize import sent_tokenize
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx
import tensorflow_hub as hub
import tensorflow as tf

# load the universal sentence encoder model from tf hub
# we will keep the use model load in cache
@st.cache(suppress_st_warning=True)
def load_use_model():

    # loads the universal sentence encoder model
    use_model = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")
    # use_model = hub.load('https://tfhub.dev/google/universal-sentence-encoder-large/5')
    return use_model

# getting the embedding of the text (query from user)
def embed(text, mod):
    return np.array(mod(text))

## Data Preparation:
# Tokenize the entire document/documents by sentence.
# Flatten the tokenized sentences ie [['i am good'], ['i am going out']] becomes ['i amd good', 'i am going out']
# If necessary, do data cleaning such as removal of punctuations, change to lower case, remove numerics, stopwords, etc.
def data_preparation(query):
    
#     sent_tokens = nltk.sent_tokenize(query)
    sent_tokens = [i.strip() for i in query.split('.') if i.strip()!='']

    # create a dictionary with sentences as key and integers as values
    # this dictionary will be used in later section to get the top n sentences as per document order
    sent_as_key = dict(zip(sent_tokens, np.arange(1, len(sent_tokens)+1)))

    return sent_tokens, sent_as_key

## Vectorize the sentences using universal sentence encoder
# Vectorize each sentences and store in a list
def embed(sent_tokens, mod):

    # list to store all sentence vectors
    sent_vectors = []
    for s in sent_tokens:
        sent_vectors.append(mod([s]))

    return sent_vectors

## Get sentence similarity between sentences with cosine similarity
# Create a matrix of NxN where N is the number of sentences
# Get the cosine similarity between each sentences.
# Similarity between same sentence will be 0 only.
def cosine_similarity_matrix(sent_tokens, sent_vectors):

    cosine_matrix = np.zeros([len(sent_tokens), len(sent_tokens)])

    for i in range(len(sent_tokens)):
        for j in range(len(sent_tokens)):
            if i != j:
                cosine_matrix[i][j] = cosine_similarity(sent_vectors[i], sent_vectors[j])

    return cosine_matrix

## Applying page rank algorithm
# Page rank is generally used by google to rank web pages.
# This algorithm can even be extended for text rank
# That is giving ranks to each sentences and based on the rank, we can get the top N sentences that summarizes the document/documents.
def text_rank(cosine_matrix, sent_tokens, sent_as_key, top_n, top_n_percent):

    # get the similarity matrix graph
    nx_graph = nx.from_numpy_array(cosine_matrix)

    # gets the scores
    scores = nx.pagerank(nx_graph)

    # sort in descending order which has list of tuples [(score_1, sent_1), ...]
    sorted_score_sent = sorted((scores[i], sent) for i, sent in enumerate(sent_tokens))

    # sorted extracted top N sentences are random
    # we will again sort extracted top N sentences such that it follows the document sentence sequence
    sent_order_per_doc = {}
    for i in range(top_n):
        sent_order_per_doc[sent_as_key[sorted_score_sent[i][1]]] = sorted_score_sent[i][1]

    st.write('*'*25)
    st.write('Top {} ({}%) extracted sentences are:\n'.format(top_n, top_n_percent))
    st.write('*'*25)
    for i, k in enumerate(sorted(sent_order_per_doc.keys())):
        display_output = str(i+1)+') '+ str(sent_order_per_doc[k])
        st.write(display_output)

## Function to call all functions
def call_all_func(query, use_model, top_n_percent=30):

    # calling data_preparation
    sent_tokens, sent_as_key = data_preparation(query)

    # calling embed
    sent_vectors = embed(query, use_model)

    # calling cosine_similarity_matrix
    cosine_matrix = cosine_similarity_matrix(sent_tokens, sent_vectors)

    top_n = int(len(sent_tokens)*(top_n_percent/100))
    if top_n == 0:
        top_n = 1

    # calling text_rank
    text_rank(cosine_matrix, sent_tokens, sent_as_key, top_n, top_n_percent)
