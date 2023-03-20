import fitz
from PyPDF2 import PdfReader

pdffile = "images\Social Science.pdf"
file = open(pdffile, "rb")
pdfReader = PdfReader(file)
totalPages = len(pdfReader.pages)
print(totalPages)
doc = fitz.open(pdffile)
for i in range(totalPages):
    page = doc.load_page(i)  # number of page
    pix = page.get_pixmap()
    output = f"images/{i}.png"
    pix.save(output)
doc.close()
