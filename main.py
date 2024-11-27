import streamlit as st
from scraper import scrape_website, split_dom_content, clean_body_content, extract_body_content
from scraper import (
    scrape_website,
    split_dom_content,
    clean_body_content,
    extract_body_content,
)

st.title("Tradeone Data Gather")
url = st.text_input("Enter the url here: ")

if st.button("Scrape Site"):
    st.write("Im looking for your data")
    result = scrape_website(url)
    print(result)
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)

    st.session_state.dom_content = cleaned_content
    with st.expander("View Dom Content"):
        st.text_area("Dom content", cleaned_content, height=300)
