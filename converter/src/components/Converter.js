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

        // Append files to FormData
        for (let i = 0; i < files.length; i++) {
            formData.append('files', files[i]);
        }

        // Append additional data to FormData
        formData.append('fileTypeBefore', fileTypeBefore);
        formData.append('fileTypeAfter', fileTypeAfter);

        try {
            const response = await fetch('http://127.0.0.1:8000/api/upload/', {
                method: 'POST',
                body: formData,
            });

            const result = await response.json();
            console.log(result.message);
        } catch (error) {
            console.error('Error:', error);
        }
    };

    return (
        <div>
        <form onSubmit={handleFileUpload}>
            <input type="file" ref={fileInputRef} name="myfile" multiple />
            <button type="submit">Upload</button>
        </form>
        </div>
    )
}

export default Converter