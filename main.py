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
    pdf.cell(w=50, h=8, txt=f'Date: {df.iloc[0,0]}')

    pdf.output(f'output/{filename}.pdf')
