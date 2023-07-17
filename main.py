import pandas as pd
import glob
#from fpdf import FPDF
#from pathlib import Path

invoice_filepaths = glob.glob("invoices/*xlsx")

for filepath in invoice_filepaths:
    df = pd.read_excel(filepath)
    print(df)