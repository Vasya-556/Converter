import FilePicker from '../components/FilePicker';
import { render, screen, fireEvent } from '@testing-library/react';
import React from 'react';

describe(FilePicker, () => { 
    it('check FilePicker prop', () => {
        const FileType = 'pdf'; 

        render(<FilePicker filetype={FileType}/>);

        const accepted_file_type = screen.getByTestId('fileTypes'); 

        expect(accepted_file_type).toHaveAttribute('accept', `.${FileType}`);
    });
    
      it('calls onFilesChange callback with FormData when files are selected', () => {
        const mockOnFilesChange = jest.fn();
        render(<FilePicker filetype="pdf" onFilesChange={mockOnFilesChange} />);
    
        const fileInput = screen.getByTestId('fileTypes');
        const file1 = new File(['file1 content'], 'file1.pdf', { type: 'application/pdf' });
        const file2 = new File(['file2 content'], 'file2.pdf', { type: 'application/pdf' });
    
        fireEvent.change(fileInput, { target: { files: [file1, file2] } });

        expect(mockOnFilesChange).toHaveBeenCalledTimes(1);
        expect(mockOnFilesChange.mock.calls[0][0]).toBeInstanceOf(FormData);
      });
})