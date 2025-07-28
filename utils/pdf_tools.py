from fpdf import FPDF

def export_invoice_to_pdf(invoice, filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)
    pdf.cell(200, 10, txt=f"Invoice {invoice[0]}", ln=True)
    pdf.cell(200, 10, txt=f"Client: {invoice[1]}", ln=True)
    pdf.cell(200, 10, txt=f"Date: {invoice[2]}", ln=True)
    pdf.cell(200, 10, txt=f"Total: {invoice[3]}", ln=True)
    pdf.cell(200, 10, txt=f"Status: {invoice[4]}", ln=True)
    pdf.output(filename)
