import streamlit as st
import requests

st.title("🌾 SmartAgri Agentic AI")
st.subheader("Your AI-powered farming assistant")

crop = st.text_input("Enter Crop Name:", "Rice")
soil = st.text_input("Enter Soil Type:", "Loamy")

if st.button("Get Recommendation"):
    data = {"crop": crop, "soil": soil}
    response = requests.post("http://localhost:8000/analyze", json=data)
    if response.status_code == 200:
        st.success(response.json()["recommendation"])
    else:
        st.error("Error fetching recommendation!")
