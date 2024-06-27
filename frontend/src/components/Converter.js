import React, { useRef } from 'react';

function Converter({file2, fileTypeBefore, fileTypeAfter}) {
    const fileInputRef = useRef(null);

    const handleFileUpload = async (event) => {
        event.preventDefault();
        const formData = new FormData();

        const files = fileInputRef.current.files;
        if (files.length === 0) {
            console.error('No files selected');
            return;
        }

        for (let i = 0; i < files.length; i++) {
            formData.append('files', files[i]);
        }

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
        <form onSubmit={handleFileUpload}>
            <input type="file" ref={fileInputRef} name="files" multiple />
            <button type="submit">Upload and Convert</button>
        </form>
    )
}

export default Converter