import {useState, useEffect} from 'react';


// function UseServer(){
//     url = 'http://127.0.0.1:5000/images'
//     const [data, setData] = useState([]);
//     // async function fetchData() 
//     const response = fetch(url);

//     data = response.json();
//     console.log("Use Server",response)
// }
function UseServer() {
    const [image, setImage] = useState([]);
  
    useEffect(() => {
      fetch("/images")
        .then((res) => res.json())
        .then((result) => {
          setImage(result.image);
        });
    }, []);
  
    return (
      <div>
        {image.map((imag) => (
          <div key={imag.id}>
            <span>{imag.filename}</span>
            <span>{imag.id}</span>
          </div>
        ))}
      </div>
    );
  }


export default UseServer