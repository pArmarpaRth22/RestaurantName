import streamlit as st
from langchainHelper import generate_content

# Title
st.title("Restaurant Name and Menu Generator")

# Input for API Key in the sidebar
api_key = st.sidebar.text_input("Enter your API Key", type="password")

# Cuisine selection
cuisine = st.sidebar.selectbox("Pick a Cuisine", ("", "Indian", "Italian", "Arabic", "Mexican", "American", "Japanese", "Russian"))

# Proceed if API key and cuisine are provided
if api_key and cuisine:
    res = generate_content(cuisine, api_key)  # Pass API key to the generate_content function
    st.subheader(res)
