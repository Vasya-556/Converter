import React from 'react'

function FilePicker({onFilesChange, filetype}) {
    const handleFilesChange = (event) => {
        onFilesChange(event.target.files);

        const files = event.target.files;
        const formData = new FormData();
        
        // Append all selected files to the FormData object
        for (let i = 0; i < files.length; i++) {
            formData.append('files', files[i]);
        }
        
    }
  return (
    <div>
        <label
        htmlFor='files'
        >Select files:</label>
        <input 
        type='file'
        id='files'
        onChange={handleFilesChange}
        multiple
        style={{display:"none"}}
        accept={filetype}
        />
    </div>
  )
}

export default FilePicker