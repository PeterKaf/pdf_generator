import streamlit as st
from PIL import Image

st.title("Invoice to PDF Converter")
message = """The Invoice to PDF Converter is a web application that allows you to convert XLSX invoice files 
into PDF format. With this app, you can easily upload your invoice files, convert them to PDF,
and download the generated PDF files."""

image = Image.open("Invoice_template.png")


st.write(message)
st.header("How to use the app")
st.write("1. Name invoice files so that invoice number is prefaced with '-' e.q: 'Invoice-<invoice number>.xlsx'.")
st.write("2. Prepare your invoice files in XLSX format, according to the template provided.")
st.image(image)
st.write("The first row of the XLSX file should contain the exact column titles."
         " date and customer name should be entered as shown in red. Total price needs to be calculated at the bottom.")
st.write("3. Upload your invoice files using the file uploader (click 'Browse files' or use drag and drop.)")
st.write("4. Click the 'Convert to PDF' button to start the conversion process.")
st.write("5. After the conversion process is complete, you can download the generated PDF files.")

