import os
from django.core.files.storage import default_storage
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .converter import *

@api_view(['POST'])
def load_files(request):
    if request.method == 'POST':
        files = request.FILES.getlist('files')
        file_type_before = request.POST.get('fileTypeBefore')
        file_type_after = request.POST.get('fileTypeAfter')

        if files:
            num_files = len(files)
            file_names = []
            folder_name = 'Files'  

            for file in files:
                file_path = os.path.join(folder_name, file.name)
                
                file_path_saved = default_storage.save(file_path, file)
                file_names.append(file_path_saved)

                if file_type_before == 'pdf':
                    if file_type_after == 'docx':
                        pass  
                    else:
                        pass  
                
                elif file_type_before == 'docx':
                    if file_type_after == 'pdf':
                        convert_docx_to_pdf([file_path_saved])
                    else:
                        pass  
                
                elif file_type_before == 'doc':
                    if file_type_after == 'docx':
                        pass  
                    else:
                        pass  
            
            file_names_str = ", ".join(file_names)
            message = f"{num_files} file(s) uploaded successfully. File type before: {file_type_before}, file type after: {file_type_after}. Files saved in '{folder_name}': {file_names_str}."
            return JsonResponse({
                'message': message,
                'num_files': num_files,
                'fileTypeBefore': file_type_before,
                'fileTypeAfter': file_type_after,
                'fileNames': file_names_str
            })
        else:
            return JsonResponse({'message': 'No files uploaded.'}, status=400)
    
    return JsonResponse({'error': 'Invalid request method. Only POST is allowed.'}, status=400)
