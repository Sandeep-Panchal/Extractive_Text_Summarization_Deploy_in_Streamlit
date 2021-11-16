## Extractive Text Summarization
 - In general, Text Summarization is a task of producing summary from the given text while preserving the key information.
 - Extractive Text Summarization is one of the Text Summarization methods that produces summary by extracting the important phrases or sentences. Extracted phrases or sentences are actually from the given content itself.
 - On the other hand, Abstractive Text Summarization, another method of Text Summarization, produces summary by creating entirely new phrases or sentences that may not be present in the given content.
 - Abstractive Text Summarization is more precise and powerful over Extractive Text Summarization.

### Objective:
 - Given the text content (group of phrases or sentences or paragraphs), top N sentences should return that actually describes the given text content.

### Approach:
 - __Data Preprocessing and Data Cleaning__: Using [NLTK](https://www.nltk.org/), preprocessed the data like getting the sentence tokenizer. For data cleaning, stopwords, punctuations, etc, can be removed if necessary. I have not done data cleaning.
 - __Text Embedding:__ With [Universal Sentence Encoder](https://www.tensorflow.org/hub/tutorials/semantic_similarity_with_tf_hub_universal_encoder), vectorized the text data of 512 dimension.
 - __Similarity Matrix__: [NLTK](https://www.nltk.org/) - Created similarity matrix of size AxA where A is the number of sentences. Then obtained [Cosine Similarity](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html) between sentences and stored in similarity matrix.
 - __Ranking Sentences__: [NLTK](https://www.nltk.org/) - Obtained ranks of sentences using Page Rank algorithm.
 - __Frontend UI and Deployment Framework__: [Streamlit](https://streamlit.io/)

### Web App Link:
 - https://share.streamlit.io/sandeep-panchal/extractive_text_summarization_deploy_in_streamlit/main/extractive_text_summarization_ui.py

### References:
 - https://www.analyticsvidhya.com/blog/2018/11/introduction-text-summarization-textrank-python/
 
### Streamlit App Link:
 - https://share.streamlit.io/sandeep-panchal/extractive_text_summarization_deploy_in_streamlit/main/extractive_text_summarization_ui.py
