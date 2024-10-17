import os
import zipfile
import shutil
from django.core.files.storage import default_storage
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from .converter import *

def clear_directory(directory):
    if os.path.exists(directory):
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f'Failed to delete {file_path}. Reason: {e}')

@api_view(['POST'])
def load_files(request):
    if request.method == 'POST':
        files = request.FILES.getlist('files')
        file_type_before = request.POST.get('fileTypeBefore')
        file_type_after = request.POST.get('fileTypeAfter')

        clear_directory('Files')

        if files:
            file_names = []
            converted_files = []
            folder_name = 'Files'  
            converted_folder_name = 'Converted'  

            if not os.path.exists(converted_folder_name):
                os.makedirs(converted_folder_name)

            for file in files:
                file_path = os.path.join(folder_name, file.name)
                
                file_path_saved = default_storage.save(file_path, file)
                file_names.append(file_path_saved)

                if file_type_before == 'pdf':
                    if file_type_after == 'docx':
                        convert_pdf_to_docx([file_path_saved])
                        converted_file_path = file_path_saved.replace('.pdf', '.docx')
                        converted_files.append(converted_file_path)
                    elif file_type_after == 'doc':
                        convert_pdf_to_doc([file_path_saved])
                        converted_file_path = file_path_saved.replace('.pdf', '.doc')
                        converted_files.append(converted_file_path)

                elif file_type_before == 'docx':
                    if file_type_after == 'pdf':
                        convert_docx_to_pdf([file_path_saved])
                        converted_file_path = file_path_saved.replace('.docx', '.pdf')
                        converted_files.append(converted_file_path)
                    elif file_type_after == 'doc':
                        convert_docx_to_doc([file_path_saved])
                        converted_file_path = file_path_saved.replace('.docx', '.doc')
                        converted_files.append(converted_file_path)

                elif file_type_before == 'doc':
                    if file_type_after == 'docx':
                        convert_doc_to_docx([file_path_saved])
                        converted_file_path = file_path_saved.replace('.doc', '.doc')
                        converted_files.append(converted_file_path)
                    elif file_type_after == 'pdf':
                        convert_doc_to_pdf([file_path_saved])
                        converted_file_path = file_path_saved.replace('.doc', '.pdf')
                        converted_files.append(converted_file_path)



            zip_file_path = os.path.join(converted_folder_name, 'converted.zip')
            with zipfile.ZipFile(zip_file_path, 'w') as zipf:
                for file in converted_files:
                    zipf.write(file, os.path.basename(file))

            with open(zip_file_path, 'rb') as file:
                response = HttpResponse(file, content_type='application/zip')
                response['Content-Disposition'] = f'attachment; filename="{os.path.basename(zip_file_path)}"'
            return response

        else:
            return JsonResponse({'message': 'No files uploaded.'}, status=400)
    
    return JsonResponse({'error': 'Invalid request method. Only POST is allowed.'}, status=400)



def hello_world(request):
    return HttpResponse('<h1>Hello World</h1>')