import os
from docx2pdf import convert
from spire.doc import Document, FileFormat, ToPdfParameterList
from pdf2docx import Converter

def convert_pdf_to_docx(pdf_files):
    for pdf_file in pdf_files:
        docx_file = os.path.splitext(pdf_file)[0] + '.docx'
        cv = Converter(pdf_file)
        cv.convert(docx_file)        
        cv.close()

def convert_pdf_to_doc(pdf_files):
    for pdf_file in pdf_files:
        doc_file = os.path.splitext(pdf_file)[0] + '.doc'
        cv = Converter(pdf_file)
        cv.convert(doc_file)
        cv.close()

def convert_docx_to_pdf(docx_files):
    for docx_file in docx_files:
        convert(docx_file)

def convert_docx_to_doc(docx_files):
    for docx_file in docx_files:
        document = Document()
        document.LoadFromFile(docx_file)
        doc_file = os.path.splitext(docx_file)[0] + '.doc'
        document.SaveToFile(doc_file, FileFormat.Doc)

def convert_doc_to_docx(doc_files):
    for doc_file in doc_files:
        document = Document()
        document.LoadFromFile(doc_file)
        docx_file = doc_file.replace('.doc', '.docx')
        document.SaveToFile(docx_file, FileFormat.Docx)

def convert_doc_to_pdf(doc_files):
    for doc_file in doc_files:
        document = Document()
        document.LoadFromFile(doc_file)
        parameters = ToPdfParameterList()
        parameters.IsEmbeddedAllFonts = True
        pdf_file = doc_file.replace('.doc', '.pdf')
        document.SaveToFile(pdf_file, parameters)
        document.Close()