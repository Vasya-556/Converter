from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework.response import Response
from rest_framework import status
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from pdf2docx import Converter
from django.http import JsonResponse

@api_view(['POST'])
def upload_files(request):
    if request.method == 'POST':
        files = request.FILES.getlist('files')
        file_type_before = request.POST.get('fileTypeBefore')
        file_type_after = request.POST.get('fileTypeAfter')

        if files:
            num_files = len(files)
            file_names = ", ".join([file.name for file in files])
            message = f"{num_files} file(s) uploaded successfully. File type before: {file_type_before}, file type after: {file_type_after}. Files: {file_names}."
            return JsonResponse({
                'message': message,
                'num_files': num_files,
                'fileTypeBefore': file_type_before,
                'fileTypeAfter': file_type_after
            })
        
        if file_type_before == 'pdf':
            if file_type_after == 'docx':
                ...
            else:
                ...        
        
        if file_type_before == 'docx':
            if file_type_after == 'pdf':
                ...
            else:
                ...
        
        if file_type_before == 'doc':
            if file_type_after == 'docx':
                ...
            else:
                ...

        else:
            return JsonResponse({'message': 'No files uploaded.'}, status=400)
    
    return JsonResponse({'error': 'Invalid request method. Only POST is allowed.'}, status=400)
