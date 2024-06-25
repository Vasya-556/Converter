import os
import zipfile
from pdf2docx import Converter
from docx import Document
from win32com.client import Dispatch
from docx2pdf import convert
from spire.doc import *
from spire.doc.common import *
from win32com.client import Dispatch

# Conversion functions
def convert_pdf_to_docx(pdf_files):
    output_files = []
    for pdf_file in pdf_files:
        docx_file = os.path.splitext(pdf_file)[0] + '.docx'
        cv = Converter(pdf_file)
        cv.convert(docx_file)
        cv.close()
        output_files.append(docx_file)
    return output_files

def convert_pdf_to_doc(pdf_files):
    output_files = []
    for pdf_file in pdf_files:
        doc_file = os.path.splitext(pdf_file)[0] + '.doc'
        cv = Converter(pdf_file)
        cv.convert(doc_file)
        cv.close()
        output_files.append(doc_file)
    return output_files

def convert_docx_to_pdf(docx_files):
    output_files = []
    for docx_file in docx_files:
        pdf_file = os.path.splitext(docx_file)[0] + '.pdf'
        convert(docx_file)
        output_files.append(pdf_file)
    return output_files

def convert_docx_to_doc(docx_files):
    output_files = []
    for docx_file in docx_files:
        document = Document()
        document.LoadFromFile(docx_file)
        doc_file = os.path.splitext(docx_file)[0] + '.doc'
        document.SaveToFile(doc_file, FileFormat.Doc)
        output_files.append(doc_file)
    return output_files

def convert_doc_to_docx(doc_files):
    output_files = []
    for doc_file in doc_files:
        document = Document()
        document.LoadFromFile(doc_file)
        docx_file = doc_file.replace('.doc', '.docx')
        document.SaveToFile(docx_file, FileFormat.Docx)
        output_files.append(docx_file)
    return output_files

def convert_doc_to_pdf(doc_files):
    output_files = []
    word = Dispatch('Word.Application')
    for doc_file in doc_files:
        pdf_file = os.path.splitext(doc_file)[0] + '.pdf'
        doc_path = os.path.abspath(doc_file)
        doc = word.Documents.Open(doc_path)
        pdf_path = os.path.abspath(pdf_file)
        doc.SaveAs(pdf_path, FileFormat=17)
        doc.Close()
        output_files.append(pdf_file)
    word.Quit()
    return output_files

# Zip creation function
def create_zip(output_files, zip_filename):
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for file in output_files:
            zipf.write(file, os.path.basename(file))

# Example usage
pdf_files = ['sample1.pdf', 'sample2.pdf']
docx_files = ['sample1.docx', 'sample2.docx']
doc_files = ['sample1.doc', 'sample2.doc']

output_files = []
# output_files.extend(convert_pdf_to_docx(pdf_files))
# output_files.extend(convert_pdf_to_doc(pdf_files))
# output_files.extend(convert_docx_to_pdf(docx_files))
# output_files.extend(convert_docx_to_doc(docx_files))
output_files.extend(convert_doc_to_docx(doc_files))
output_files.extend(convert_doc_to_pdf(doc_files))

create_zip(output_files, 'converted_files.zip')
