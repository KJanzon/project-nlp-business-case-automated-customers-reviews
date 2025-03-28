
import streamlit as st
import os

# Set up
st.set_page_config(page_title="Amazon Product Reviews", layout="centered")
st.title("🛍️ Amazon Product Review Summaries")
st.markdown("Explore our consumer-style summaries of top Amazon products based on real user reviews.")

# Dropdown to select category
categories = {
    "Tablet": "tablet.md",
    "Smart Speaker": "smart_speaker.md",
    "E-reader": "e_reader.md"
}

category = st.selectbox("Select a Product Category", list(categories.keys()))

# Load and display the markdown file
file_path = os.path.join("product_articles", categories[category])

with open(file_path, "r", encoding="utf-8") as f:
    st.markdown(f.read(), unsafe_allow_html=True)
