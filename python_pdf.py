import PyPDF2
from reportlab.pdfgen import canvas
from io import BytesIO

# Primeiro vamos criar um PDF com texto usando reportlab
def create_pdf_with_text(text):
    packet = BytesIO()
    c = canvas.Canvas(packet)
    c.drawString(100, 750, text)  # x=100, y=750 é a posição do texto na página
    c.save()
    packet.seek(0)
    return packet

# Lendo um PDF existente
with open('sample_pdf.pdf', 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    page = pdf_reader.pages[0].extract_text()
    print("Conteúdo do PDF existente:")
    print(page)

# Criando um novo PDF com texto
texto_novo = "Olá! Este é um novo PDF criado com Python!"
new_pdf_content = create_pdf_with_text(texto_novo)

# Criando um novo PDF
new_pdf = PyPDF2.PdfWriter()
new_page = PyPDF2.PdfReader(new_pdf_content).pages[0]
new_pdf.add_page(new_page)

# Salvando o novo PDF
with open('novo_pdf.pdf', 'wb') as output_file:
    new_pdf.write(output_file)

print("\nNovo PDF 'novo_pdf.pdf' foi criado com sucesso!")

