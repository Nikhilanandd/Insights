import streamlit as st
import requests
import os
from PIL import Image

st.set_page_config(page_title="Data Insights Generator", layout="wide")

st.title("📊 Welcome to Data Insights Generator")

st.sidebar.header("🔍 About")
st.sidebar.markdown("""
This app lets you:
- Upload your datasets 📄
- Get auto-generated insights 📈
- Visualize the data instantly 🖼️
""")

st.sidebar.header("🕒 Previous Uploads")
uploads = os.listdir("uploads")
if uploads:
    for file in uploads:
        st.sidebar.write(f"• {file}")
else:
    st.sidebar.write("No uploads yet.")

st.write("## Upload Your Dataset")

uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=['csv', 'xlsx'])

if uploaded_file is not None:
    with open(os.path.join("uploads", uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"✅ File {uploaded_file.name} uploaded successfully!")

    if st.button("Generate Insights"):
        with st.spinner('⏳ Generating insights...'):
            files = {'file': open(os.path.join("uploads", uploaded_file.name), 'rb')}
            response = requests.post("http://127.0.0.1:5000/upload", files=files)

            if response.status_code == 200:
                data = response.json()
                st.subheader("📜 Insights Summary")
                st.json(data['insights'])

                st.subheader("🖼️ Visualization")
                if os.path.exists(data['chart_path']):
                    image = Image.open(data['chart_path'])
                    st.image(image, caption="Generated Chart", use_column_width=True)
                else:
                    st.error("Visualization image not found.")
            else:
                st.error("Something went wrong. Please try again.")
