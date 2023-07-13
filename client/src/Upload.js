import React, { useState } from 'react';
import './App.css';  
import axios from 'axios';


function UploadForm() {
  const [file, setFile] = useState(null);
  const [error, setError] = useState(null);

  const types = ['image/png', 'image/jpeg'];

  function changeHandler(e, files) {
    let selected = e.target.files[0];
    if (selected && types.includes(selected.type)) {
      setFile(selected);
      setError('');
    } else {
      setFile(null);
      setError('Please choose an image file (png or jpeg)');
    } 
    
    const formData = new FormData();
    formData.append("myImage", files);

    try {
      const response = fetch('http://127.0.0.1:5000/images', {
        method: 'POST',
        body: formData,
      });

      if (response.ok) {
        const data = response.json();
        setFile(data.imageUrl); // Set the uploaded image URL in state
      } else {
        setError('Error uploading image');
      }
    } catch (error) {
      setError('Error uploading image');
    }
    // axios.post('http://127.0.0.1:5000/images', formData)
    // .then((response) => console.log(response));

  }

  // function uploadHandler(e) {
  //   const file = e.target.files[0];
  //   file.isUploading = true;
  //   setFile([...files, file])

  //  
  // }

  return (
    <form className='uploadoutput'>
      <input type="file" onChange={changeHandler} />
      <div className="output">
        {error && <div className="error">{error}</div>}
        {file && <div>{file.name}</div>}
      </div>
      <button>Upload</button> 
    </form>
  );
}

export default UploadForm;
