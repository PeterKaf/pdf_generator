import streamlit as st
from PIL import Image

st.title("Invoice to PDF Converter")
message = """The Invoice to PDF Converter is a web application that allows you to convert XLSX invoice files 
into PDF format. With this app, you can easily upload your invoice files, convert them to PDF,
and download the generated PDF files."""

st.write(message)
st.header("How to use the app")
st.write("1. Prepare your invoice files in XLSX format, according to the template provided.")
st.write("2. Upload your invoice files using the file uploader.")
st.write("3. Click the 'Convert to PDF' button to start the conversion process.")
st.write("4. After the conversion process is complete, you can download the generated PDF files.")

