import React from 'react'

function FormatSelector({onSelectFileType}) {
    const handleSelectFileType = (event) => {
        onSelectFileType(event.target.value);
    }

  return (
    <div>
        <select 
        name='fileTypes' 
        id='fileTypes'
        onChange={handleSelectFileType}>
            <option value='.txt'>TXT</option>
            <option value='.pdf'>PDF</option>
            <option value='.ods'>ODS</option>
        </select>
    </div>
  )
}

export default FormatSelector