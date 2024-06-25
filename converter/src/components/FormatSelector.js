import React from 'react'

function FormatSelector({onSelectFileType, defaultFileType}) {
    const handleSelectFileType = (event) => {
        onSelectFileType(event.target.value);
    }

  return (
    <div>
        <select 
        name='fileTypes' 
        id='fileTypes'
        onChange={handleSelectFileType}
        defaultValue={defaultFileType}
        >
            <option value='docx'>DOCX</option>
            <option value='doc'>DOC</option>
            <option value='pdf'>PDF</option>
            {/* <option value='.odt'>ODT</option> */}
        </select>
    </div>
  )
}

export default FormatSelector