import React, {useState} from 'react';
import './App.css';
import FilePicker from './components/FilePicker';
import FormatSelector from './components/FormatSelector';

function App() {
  const [selectedFiles, setSelectedFiles] = useState(null);
  const [fileTypeBefore, setfileTypeBefore] = useState('');
  const [fileTypeAfter, setfileTypeAfter] = useState('');

  const handleFilesChange = (files) => {
    setSelectedFiles(files);
  }

  const handleSelectFileTypeBefore = (fileType) => {
    setfileTypeBefore(fileType);
  }

  const handleSelectFileTypeAfter = (fileType) => {
    setfileTypeAfter(fileType);
  }

  return (
    <>
      <FilePicker onFilesChange={handleFilesChange} filetype={fileTypeBefore}/>
      <FormatSelector onSelectFileType={handleSelectFileTypeBefore}/>
      <FormatSelector onSelectFileType={handleSelectFileTypeAfter}/>
    </>
  );
}

export default App;
