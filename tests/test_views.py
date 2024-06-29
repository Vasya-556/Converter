from backend.converter.api.views import *
from django.urls import reverse
from django.test import TestCase, Client
from django.core.files.uploadedfile import SimpleUploadedFile
import json
import os
from io import BytesIO
from zipfile import ZipFile
from django.core.files.uploadedfile import SimpleUploadedFile

class TestViews(TestCase):
    def test_load_files(self):
        client = Client()
        
        pdf_content = b'%PDF-1.4\n%mock content\n1 0 obj\n<<\n/Type /Catalog\n/Pages 2 0 R\n>>\nendobj\n2 0 obj\n<<\n/Type /Pages\n/Kids [3 0 R]\n/Count 1\n>>\nendobj\n3 0 obj\n<<\n/Type /Page\n/Parent 2 0 R\n/MediaBox [0 0 612 792]\n/Contents 4 0 R\n/Resources <<\n/Font <<\n/F1 5 0 R\n>>\n>>\n>>\nendobj\n4 0 obj\n<<\n/Length 55\n>>\nstream\nBT\n/F1 24 Tf\n100 100 Td\n(Mock PDF file content) Tj\nET\nendstream\nendobj\n5 0 obj\n<<\n/Type /Font\n/Subtype /Type1\n/BaseFont /Helvetica\n>>\nendobj\ntrailer\n<<\n/Root 1 0 R\n>>\n%%EOF'
        file1 = SimpleUploadedFile("file1.pdf", pdf_content, content_type="application/pdf")
        file2 = SimpleUploadedFile("file2.pdf", pdf_content, content_type="application/pdf")
        
        data = {
            'fileTypeBefore': 'pdf',
            'fileTypeAfter': 'docx',
            'files': [file1, file2],
        }
        response = client.post(reverse('load'), data, format='multipart')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/zip')

        with open('converted.zip', 'wb') as f:
            f.write(response.content)
        
        with ZipFile('converted.zip', 'r') as zipf:
            converted_files = zipf.namelist()
            self.assertIn('file1.docx', converted_files)
            self.assertIn('file2.docx', converted_files)

        os.remove('converted.zip')