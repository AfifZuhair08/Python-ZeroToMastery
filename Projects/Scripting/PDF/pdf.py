import PyPDF2

with open("files/twopage.pdf",'rb') as pdf_file:
    reader = PyPDF2.PdfReader(pdf_file)
    print(len(reader.pages))
    print(reader.pages[0])
    