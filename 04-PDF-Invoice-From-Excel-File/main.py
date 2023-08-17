import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob('invoices/*.xlsx')

for filepath in filepaths:
    # Creating the PDF
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()

    # Extracting the invoice number and date from the excel file name
    filename = Path(filepath).stem
    invoice_no, invoice_date = filename.split('-')

    # Invoice number as heading
    pdf.set_font(family='Times', size=16, style='B')
    pdf.cell(w=50, h=8, txt=f'Invoice No. {invoice_no}', ln=1)

    # Invoice date as sub-heading
    pdf.set_font(family='Times', size=12, style='B')
    pdf.cell(w=50, h=8, txt=f'Date. {invoice_date}', ln=1)

    # Empty lines
    pdf.cell(w=50, h=8, txt=' ', ln=1)

    # Reading the excel invoice using Pandas
    df = pd.read_excel(filepath, sheet_name='Sheet 1')

    # Header of the table
    invoice_columns = [item.replace('_', ' ').title() for item in df.columns]
    pdf.set_font(family='Times', size=10, style='B')
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=25, h=8, txt=invoice_columns[0], border=1)
    pdf.cell(w=70, h=8, txt=invoice_columns[1], border=1)
    pdf.cell(w=35, h=8, txt=invoice_columns[2], border=1)
    pdf.cell(w=30, h=8, txt=invoice_columns[3], border=1)
    pdf.cell(w=30, h=8, txt=invoice_columns[4], border=1, ln=1)

    # Rows of the table
    for index, row in df.iterrows():
        pdf.set_font(family='Times', size=10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=25, h=8, txt=str(row['product_id']), border=1)
        pdf.cell(w=70, h=8, txt=str(row['product_name']), border=1)
        pdf.cell(w=35, h=8, txt=str(row['amount_purchased']), border=1)
        pdf.cell(w=30, h=8, txt=str(row['price_per_unit']), border=1)
        pdf.cell(w=30, h=8, txt=str(row['total_price']), border=1, ln=1)

    # Final row with the total price
    total_price = df['total_price'].sum()
    pdf.set_font(family='Times', size=10, style='B')
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=25, h=8, txt='', border=1)
    pdf.cell(w=70, h=8, txt='', border=1)
    pdf.cell(w=35, h=8, txt='', border=1)
    pdf.cell(w=30, h=8, txt='', border=1)
    pdf.cell(w=30, h=8, txt=str(total_price), border=1, ln=1)

    # Empty lines
    pdf.cell(w=50, h=8, txt=' ', ln=1)

    # Total price message
    pdf.set_font(family='Times', size=14)
    pdf.cell(w=35, h=8, txt=f"The total price is ")
    pdf.set_font(family='Times', size=14, style='B')
    pdf.cell(w=30, h=8, txt=str(total_price), ln=1)

    # Empty lines
    pdf.cell(w=50, h=8, txt=' ', ln=1)

    # Company name and logo
    pdf.set_font(family='Times', size=14, style='B')
    pdf.cell(w=27, h=8, txt=f"PythonHow")
    pdf.image('pythonhow.png', w=10)

    # Final output of the PDF file
    pdf.output(f'pdfs/{filename}.pdf')
