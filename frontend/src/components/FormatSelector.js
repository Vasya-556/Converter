import React from 'react'

function FormatSelector({onSelectFileType, defaultFileType}) {
    const handleSelectFileType = (event) => {
        onSelectFileType(event.target.value);
    }

  return (
    <div className='FormatSelector'>
        <select 
        name='fileTypes' 
        id='fileTypes'
        onChange={handleSelectFileType}
        defaultValue={defaultFileType}
        data-testid="fileTypes"
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