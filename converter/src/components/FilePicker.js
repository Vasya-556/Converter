import React from 'react'

function FilePicker({onFilesChange, filetype}) {
    const handleFilesChange = (event) => {
        onFilesChange(event.target.files);
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