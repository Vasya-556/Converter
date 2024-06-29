import React, {useRef, useState} from 'react'
import '../App.css';

function FilePicker({onFilesChange, filetype}) {
  const filesRef = useRef(null);
  const [selectedFileNames, setSelectedFileNames] = useState([]);

  const handleFilesChange = (event) => {
        const files = filesRef.current.files;
        const formData = new FormData();

        setSelectedFileNames(Array.from(files).map(file => file.name));
        
        for (let i = 0; i < files.length; i++) {
            formData.append('files', files[i]);
        }        

        onFilesChange(formData);
    }
  return (
    <div className='FilePicker'>
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
        accept={`.${filetype}`}
        ref={filesRef}
        data-testid="fileTypes"
        />
        {selectedFileNames.length > 0 && (
                <div className='SelectedFilesList'>
                    {selectedFileNames.map((fileName, index) => (
                        <li key={index}>{fileName}</li>
                    ))}
                </div>
            )}
    </div>
  )
}

export default FilePicker