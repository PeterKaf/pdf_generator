import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

invoice_filepaths = glob.glob("invoices/*xlsx")

for filepath in invoice_filepaths:
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

    for index, row in df.iterrows():
        if index < len(df) - 1:
            pdf.set_font(family="Times", size=10)
            pdf.cell(w=50, h=8, txt=str(row['Product ID']), border=1)
            pdf.cell(w=30, h=8, txt=str(row['Quantity']), border=1)
            pdf.cell(w=30, h=8, txt=str(row['Unit Price']), border=1)
            pdf.cell(w=30, h=8, txt=str(row['Total Amount']), border=1, ln=1)
        elif index == len(df) - 1:
            pdf.set_font(family="Times", style="B", size=16)
            pdf.cell(w=50, h=8, txt=f'Total Price: {df.iloc[index, 5]}', ln=1)


    pdf.output(f'output/{filename}.pdf')
