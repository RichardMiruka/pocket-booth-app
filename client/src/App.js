import './App.css';
import UploadForm from './Upload';
import Gallery from './Gallery';
import Search from './Search';
import UseServer from './UseServer';

function App() {
  return (
    <div>
      <Gallery />
      <Search />
      <UploadForm />
      <UseServer />
    </div>
  );
}

export default App;
