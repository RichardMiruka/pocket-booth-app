import React, { useEffect, useState } from "react"
import './App.css';
import UploadForm from './Upload';
import Gallery from './Gallery';
import Search from './Search';
import UseServer from './UseServer';
import CommentMessage from './NewPhotos';

function App() {

  const [messages, setMessages] = useState([]);
  const [photos, setPhotos] = useState([]);
  const [search, setSearch] = useState("");

  useEffect(() => {
    fetch("http://127.0.0.1:5000/users")
      .then((r) => r.json())
      .then((messages) => setMessages(messages));
  }, []);

  function handleAddMessage(newMessage) {
    setMessages([...messages, newMessage]);
  }

  // function handleDeleteMessage(id) {
  //   const updatedMessages = messages.filter((message) => message.id !== id);
  //   setMessages(updatedMessages);
  // }

  // function handleUpdateMessage(updatedMessageObj) {
  //   const updatedMessages = messages.map((message) => {
  //     if (message.id === updatedMessageObj.id) {
  //       return updatedMessageObj;
  //     } else {
  //       return message;
  //     }
  //   });
  //   setMessages(updatedMessages);
  // }

  const displayedPhotos = photos.filter((photo) =>
    photo.body.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div>
      <Gallery photos= {displayedPhotos}/>
      <Search search={search} onSearchChange={setSearch}/>
      <UploadForm />
      <UseServer />
      <CommentMessage onAddMessage={handleAddMessage} />
    </div>
  );
}

export default App;
