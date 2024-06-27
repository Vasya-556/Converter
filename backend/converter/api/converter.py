from docx2pdf import convert

def convert_docx_to_pdf(docx_files):
    for docx_file in docx_files:
        convert(docx_file)