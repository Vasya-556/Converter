import React from 'react';
import { render, screen } from '@testing-library/react';
import FormatSelector from '../components/FormatSelector';

describe(FormatSelector, () => {
    it('check default file type prop', () => {
        const defaultFileType = 'pdf'; 

        render(<FormatSelector defaultFileType={defaultFileType} />);

        const selectElement = screen.getByTestId('fileTypes'); 

        expect(selectElement).toHaveValue(defaultFileType);
        expect(screen.getByText('PDF')).toBeInTheDocument(); 
    });
})