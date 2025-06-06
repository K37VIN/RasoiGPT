from fpdf import FPDF
from io import BytesIO

def create_pdf(recipe):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt=recipe['title'], ln=True, align='C')

    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Ingredients", ln=True)
    pdf.set_font("Arial", '', 12)
    for line in recipe['ingredients'].split("\n"):
        pdf.multi_cell(0, 10, txt=line)

    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Steps", ln=True)
    pdf.set_font("Arial", '', 12)
    for line in recipe['steps'].split("\n"):
        pdf.multi_cell(0, 10, txt=line)

    buffer = BytesIO()
    pdf_output = pdf.output(dest='S').encode('latin1')  
    buffer.write(pdf_output)
    buffer.seek(0)
    return buffer
