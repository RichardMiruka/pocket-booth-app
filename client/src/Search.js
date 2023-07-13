import React, { useState, useRef } from 'react';
import './App.css';

function Search() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const searchInputRef = useRef(null);

  const handleSearch = async () => {
    try {
      const response = await fetch(`http://127.0.0.1:5000/users?query=${query}`);
      const data = await response.json();
      setResults(data);
    } catch (error) {
      console.error(error);
    }
  };

  const handleClick = () => {
    searchInputRef.current.focus();
  };

  return (
    <div className="search-container">
      <input type="text" ref={searchInputRef} value={query} onChange={(e) => setQuery(e.target.value)} />
      <button onClick={handleSearch}>Search</button>
      <div className="clickable-area" onClick={handleClick}></div>
      <ul>
        {results.map((result) => (
          <li key={result.id}>{result.name}</li>
        ))}
      </ul>
    </div>
  );
} 


export default Search;