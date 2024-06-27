import React from 'react';

function Converter({file, fileTypeBefore, fileTypeAfter}) {
    const handleButtonClick = async (event) => {
        if (!file) {
            console.error('No files selected');
            return;
        }

        const formData = file;
        formData.append('fileTypeBefore', fileTypeBefore);
        formData.append('fileTypeAfter', fileTypeAfter);

        try {
            const response = await fetch('http://127.0.0.1:8000/api/load/', {
                method: 'POST',
                body: formData,
            });

            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const blob = await response.blob();
            const url = window.URL.createObjectURL(blob);

            const a = document.createElement('a');
            a.href = url;
            a.download = 'converted.zip';  
            document.body.appendChild(a);
            a.click();
            a.remove();

        } catch (error) {
            console.error('Error:', error);
        }
    };

    return (
        <div>
            <button
            onClick={handleButtonClick}>
            Convert
            </button>
        </div>
    )
}

export default Converter