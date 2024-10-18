import os
from pdf2docx import Converter  
import aspose.words as aw  

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
        document = aw.Document(docx_file)
        pdf_file = os.path.splitext(docx_file)[0] + '.pdf'
        document.save(pdf_file, aw.SaveFormat.PDF)  

def convert_docx_to_doc(docx_files):
    for docx_file in docx_files:
        document = aw.Document(docx_file)
        doc_file = os.path.splitext(docx_file)[0] + '.doc'
        document.save(doc_file, aw.SaveFormat.DOC)

def convert_doc_to_docx(doc_files):
    for doc_file in doc_files:
        document = aw.Document(doc_file)
        docx_file = os.path.splitext(doc_file)[0] + '.docx'
        document.save(docx_file, aw.SaveFormat.DOCX)

def convert_doc_to_pdf(doc_files):
    for doc_file in doc_files:
        document = aw.Document(doc_file)
        pdf_file = os.path.splitext(doc_file)[0] + '.pdf'
        document.save(pdf_file, aw.SaveFormat.PDF)
