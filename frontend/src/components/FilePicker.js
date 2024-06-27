import React, {useRef} from 'react'

function FilePicker({onFilesChange, filetype}) {
  const filesRef = useRef(null);

  const handleFilesChange = (event) => {
        const files = filesRef.current.files;
        const formData = new FormData();
        
        for (let i = 0; i < files.length; i++) {
            formData.append('files', files[i]);
        }        

        onFilesChange(formData);
    }
  return (
    <div>
        <label
        htmlFor='files'>
          Select files:
        </label>
        
        <input 
        type='file'
        name='files'
        id='files'
        onChange={handleFilesChange}
        multiple
        style={{display:"none"}}
        accept={`.${filetype}`}
        ref={filesRef}
        />
    </div>
  )
}

export default FilePicker