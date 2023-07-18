import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

# Path to the directories containing the Excel and PDF files
invoice_filepaths = "invoices/"
pdf_filepaths = "output/"


# Function definitions for generating PDF content
def get_col_titles(pdf, df):
    """
    Get the column titles from the dataframe and write them to the PDF
    :param pdf: FPDF object
    :param df: Pandas dataframe
    :return: None
    """
    columns = list(df.columns)
    pdf.set_font(family="Times", style="B", size=10)
    pdf.cell(w=50, h=8, txt=columns[0], border=1)
    pdf.cell(w=30, h=8, txt=columns[1], border=1)
    pdf.cell(w=40, h=8, txt=columns[2], border=1)
    pdf.cell(w=40, h=8, txt=columns[3], border=1, ln=1)


def get_table_contents(pdf, row):
    """
    Get the table contents from the dataframe and write them to the PDF
    :param pdf: FPDF object
    :param row: Dataframe row
    :return: None
    """
    pdf.set_font(family="Times", size=10)
    pdf.cell(w=50, h=8, txt=str(row['Product ID']), border=1)
    pdf.cell(w=30, h=8, txt=str(row['Quantity']), border=1)
    pdf.cell(w=40, h=8, txt=str(row['Unit Price']), border=1)
    pdf.cell(w=40, h=8, txt=str(row['Total Amount']), border=1, ln=1)


def get_total_price(pdf, df, index):
    """
    Get the total price from the dataframe and write it to the PDF
    :param pdf: FPDF object
    :param df: Pandas dataframe
    :param index: Index of the last row in the dataframe
    :return: None
    """
    pdf.set_font(family="Times", style="B", size=10)
    pdf.cell(w=50, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=40, h=8, txt="Total Price:", border=1)
    pdf.cell(w=40, h=8, txt=str(df.iloc[index, 5]), ln=1, border=1)


def xlsx_transform(filepath):
    """
    Transform the xlsx file to a PDF file
    :param filepath: path to the xlsx file
    :return: None
    """
    df = pd.read_excel(filepath)

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    filename = Path(filepath).stem
    invoice_nr = filename.split("-")[1]

    pdf.set_font(family="Times", style="B", size=16)
    pdf.cell(w=50, h=8, txt=f'Invoice nr: {invoice_nr}', ln=1)

    pdf.set_font(family="Times", style="B", size=16)
    pdf.cell(w=50, h=8, txt=f'Date: {df.iloc[0,0]}', ln=1)

    pdf.set_font(family="Times", style="B", size=16)
    pdf.cell(w=50, h=8, txt=f'Customer: {df.iloc[0,1]}', ln=1)
    pdf.cell(w=50, h=8, txt="", ln=1)

    get_col_titles(pdf, df)
    for index, row in df.iterrows():
        if index < len(df) - 1:
            get_table_contents(pdf, row)
        elif index == len(df) - 1:
            get_total_price(pdf, df, index)

    pdf.output(f'{pdf_filepaths}{filename}.pdf')


def convert_to_pdf(directory):
    """
    Convert all Excel files in the directory to PDF files via the xlsx_transform function
    :param directory: directory containing the Excel files
    :return: None
    """
    # Get all Excel files in the directory using glob
    excel_files = glob.glob(f"{directory}/*.xlsx")

    for file in excel_files:
        xlsx_transform(file)
