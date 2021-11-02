# import required packages, libraries and files
import streamlit as st
import extractive_text_summarization_model as ext_model

# page config to change the page icon and the title of the page
st.set_page_config(page_title='Extractive Text Summarization', page_icon=':smiley:')

# UI starts from here
st.title('Extractive Text Summarization')
st.write('')
st.write('__*Text summarization*__ is a task that involves extracting the summary of the whole content while preserving the key information.')
st.write('Unlike __*Abstractive Summarization*__ that produces the whole new phrases which may not be present in the given content, __*Extractive Summarization*__ produces the summary by extracting the phrases from the given content. Extracted phrases are from the given content itself.')

st.write('')
query = st.text_area("Please enter your text content...", height=300)
submit_button = st.button("Submit")

if submit_button:
    use_model = ext_model.load_use_model()
    ext_model.call_all_func(query, use_model, top_n_percent=30)
