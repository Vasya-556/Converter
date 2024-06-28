import React, {useState} from 'react';
import './App.css';
import FilePicker from './components/FilePicker';
import FormatSelector from './components/FormatSelector';
import Converter from './components/Converter';

function App() {
  const [selectedFiles, setSelectedFiles] = useState(null);
  const [fileTypeBefore, setfileTypeBefore] = useState('docx');
  const [fileTypeAfter, setfileTypeAfter] = useState('pdf');

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
      <div className="formatSelectorsContainer">
        <FormatSelector onSelectFileType={handleSelectFileTypeBefore} defaultFileType={fileTypeBefore} />
        <FormatSelector onSelectFileType={handleSelectFileTypeAfter} defaultFileType={fileTypeAfter} />
      </div>
      <Converter file={selectedFiles} fileTypeBefore={fileTypeBefore} fileTypeAfter={fileTypeAfter}/>
    </>
  );
}

export default App;
