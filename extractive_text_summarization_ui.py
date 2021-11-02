import streamlit as st
import numpy as np
import tensorflow_hub as hub
import tensorflow as tf

# load the universal sentence encoder model from tf hub
def load_use_model():

    # loads the universal sentence encoder model
    use_model = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")
    # use_model = hub.load('https://tfhub.dev/google/universal-sentence-encoder-large/5')
    return use_model

# getting the embedding of the text (query from user)
def embed(text, mod):
    return np.array(mod(text))

@st.cache(suppress_st_warning=True)
def load_all_fun():

    # call load_use_model to load the universal sentence encoder model from tf hub
    use_model = load_use_model()

    return use_model

query = 'aws, s3bucket, ec2'
def vectorize(query):

    query_vect = embed([query], use_model)

    st.write(query_vect)

if __name__ == '__main__':

    use_model = load_all_fun()
    vectorize(query)

