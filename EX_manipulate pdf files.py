# Program to manipulate pdf files using pyPDF2 module. Merge multiple pdfs into a single pdf. It can add custom data, viewwing options and passwords to the pdf. pypdf can retrieve metadata text and from pdfs as well.


from PyPDF2 import PdfWriter
import os

merger = PdfWriter()
files = [file for file in os.listdir() 
if file.endswith(".pdf")]

for pdf in files:
    merger.append(pdf)
merger.write("merged-pdf.pdf")
merger.close()

print(dir(files))