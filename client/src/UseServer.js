import React, { useState, useEffect } from 'react';

function UseServer() {
  const [data, setData] = useState([]);
  // console.log(data)
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function fetchData() {
      try {
        const response = await fetch('http://127.0.0.1:5000/images');
        const jsonData = await response.json();
        setData(jsonData);
        setLoading(false);
      } catch (error) {
        setError(error);
        setLoading(false);
      }
    }

    fetchData();
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error.message}</div>;
  }

  return (
    <div>
      {/* Display the fetched data */}
      {data && (
        
        <ul>
          {data.map((item) => (
            // <li key={item.id}>{item.name}</li>
            <img src={item.filename} alt="image"/>
          ))}
        </ul>
      )}
    </div>
  );
}

export default UseServer;
