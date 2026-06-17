import streamlit as st
import requests

st.title("Movie Review Sentiment Analysis")

review = st.text_area("Type your Review Here!")

if st.button("Analyze"):
    if review.strip()=="":
        st.warning("Enter your review first!")
    else:
        response = requests.post(
            "http://127.0.0.1:8000/analysis",
            json = {"review":review}
        )
        result = response.json()

        st.subheader("Results: ")
        label = result["analysis"]
        if label == "Negative":
            st.error("Negative!")
        else:
            st.success("Positive")
        
        st.caption(f'Input: {result["review"]}')