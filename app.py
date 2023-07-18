import streamlit as st
from pdf_generator import convert_to_pdf
import zipfile
import glob
from pathlib import Path

def main():
    st.title("Invoice to PDF Converter")

    # File uploader for xlsx files
    uploaded_files = st.file_uploader("Upload your xlsx invoice files", type=["xlsx"], accept_multiple_files=True)

    if uploaded_files:
        for uploaded_file in uploaded_files:
            file_contents = uploaded_file.read()

            # Save the uploaded file to the 'invoices' directory
            invoice_filepath = "invoices/" + uploaded_file.name
            with open(invoice_filepath, "wb") as f:
                f.write(file_contents)

        # Convert xlsx files to PDF
        convert_to_pdf("invoices/")

        # Create a zip file containing all the generated PDFs
        with zipfile.ZipFile("output.zip", "w") as zf:
            pdf_files = glob.glob("output/*.pdf")
            for pdf_file in pdf_files:
                zf.write(pdf_file, arcname=Path(pdf_file).name)

        # Display success message and download link
        st.success("PDF files successfully generated!")
        st.download_button(label="Download All PDFs", data=open("output.zip", "rb"), file_name="output.zip", mime="application/zip")

if __name__ == "__main__":
    main()
