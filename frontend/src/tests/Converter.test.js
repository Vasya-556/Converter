import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import Converter from '../components/Converter'; 

global.fetch = jest.fn(() =>
  Promise.resolve({
    ok: true,
    blob: () => Promise.resolve(new Blob(['dummy data'], { type: 'application/zip' })),
  })
);

describe('Converter', () => {
  test('calls the API and handles the response correctly', async () => {
    const file = new FormData();
    file.append('file', new Blob(['test content'], { type: 'text/plain' }));

    const fileTypeBefore = 'docx';
    const fileTypeAfter = 'pdf';

    render(<Converter file={file} fileTypeBefore={fileTypeBefore} fileTypeAfter={fileTypeAfter} />);

    const convertButton = screen.getByText('Convert');
    fireEvent.click(convertButton);

    expect(global.fetch).toHaveBeenCalledWith('http://127.0.0.1:8000/api/load/', {
      method: 'POST',
      body: file,
    });

    await screen.findByText('Convert');

    expect(file.get('fileTypeBefore')).toBe(fileTypeBefore);
    expect(file.get('fileTypeAfter')).toBe(fileTypeAfter);
  });
});