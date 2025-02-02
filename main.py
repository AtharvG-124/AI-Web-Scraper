import streamlit as st
from scrape import scrape_website, split_dom_content, clean_body_content, extract_body_content
from parse import parse_with_ollama


st.title("Web Scraper AI")

url = st.text_input("Enter the URL of the website you want to scrape:")

if st.button("Scrape"):
    st.write("Scraping...")
    result = scrape_website(url)
    body_content = extract_body_content(result)
    cleaned_body_content = clean_body_content(body_content)
    st.session_state.dom_content = cleaned_body_content

    with st.expander("View DOM Content"):
        st.text_area("DOM Content", cleaned_body_content, height=300)


if "dom_content" in st.session_state:
    parse_desc = st.text_area("Describe what you want to parse:")
    if st.button("Parse Content"):
        if parse_desc:
            st.write("Parsing...")
            dom_content = split_dom_content(st.session_state.dom_content)
            result = parse_with_ollama(dom_content, parse_desc)
            st.write(result)
        else:
            st.write("Please provide a description to parse.")
