import streamlit as st
import urllib
import base64
import os
from utils import semantic_search, summarize


def save_uploadedfile(uploadedFile):
    with open(os.path.join("data", uploadedFile.name), "wb") as f:
        f.write(uploadedFile.getbuffer())
    return st.success(f'Saved File:{uploadedFile.name} to directory')


@st.cache_data
def displayPDF(file):
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)


st.set_page_config(layout='wide')
st.title("Semantic Search Application")

uploaded_pdf = st.file_uploader("Upload your PDF", type=['pdf'])

if uploaded_pdf is not None:
    col1, col2, col3 = st.columns([3,1,1])
    with col1:
        input_file = save_uploadedfile(uploaded_pdf)
        pdf_file = "data/"+uploaded_pdf.name
        pdf_view = displayPDF(pdf_file)
    with col2:
        st.success("Search Area")
        query_search = st.text_area("Search your query")
        if st.checkbox("search"):
            st.info("Your query: "+query_search)
            result = semantic_search(query_search)
            st.write(result)
    with col3:
        st.success("Automated Summarization")
        summary_result = summarize(pdf_file)
        st.write(summary_result)            
    