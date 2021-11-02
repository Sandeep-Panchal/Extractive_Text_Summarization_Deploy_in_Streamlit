# import required packages, libraries and files
import streamlit as st
import extractive_text_summarization_model as ext_model

# page config to change the page icon and the title of the page
st.set_page_config(page_title='Extractive Text Summarization', page_icon=':smiley:')

# UI starts from here
st.title('Extractive Text Summarization')
st.write('')

query = st.text_area("Please enter your text content...", height=300)
submit_button = st.button("Submit")

if submit_button:
    use_model, stop_words = ext_model.load_func_cache()
    ext_model.call_all_func(query, use_model, top_n_percent=30)