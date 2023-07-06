import React from 'react';

function Gallery() {
  return (
    <div>
      <h1 className="mt-5 text-center main heading">Pocket Booth App</h1>
      <div className="menu-tab container">
        <div className="menu-tab d-flex justify-center-around">
          <button className="button">Homepage</button>
          <button className="button">Favorite</button>
          <button className="button">Private</button>
        </div>
      </div>
    </div>
  );
}

export default Gallery;
