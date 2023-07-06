import './App.css';
import UseServer from './UseServer';


function Gallery() {
    const items = []; // Assuming you have an array of items

    return (
        <div>
            <h1 className="nav-bar">Pocket Booth App</h1>
            <div className="menu-tab container">
                <div className="menu-tab d-flex justify-content-around">
                    <button className="button">Homepage</button>
                    <button className="button">Favorite</button>
                    <button className="button">Private</button>
                </div>
            </div>
            <div className="menu-items container-fluid mt-5">
                <div className="row">
                    <div className="col-11 mx-auto">
                        <UseServer/>
                        {items.map((element) => {
                            const { id, user, image, title } = element;
                            return (
                                <div key={id}>
                                    <a href={`/item/${id}`}>{title}</a><br />
                                    <div className="col-12 col-md-12 col-lg-4 img-div">
                                        <img src={image} alt="photo of us" className="img-fluid" />
                                    </div>
                                    <p>{user}</p>
                                </div>
                            );
                        })}
                    </div>
                </div>
            </div>
        </div>
    );
}

export default Gallery;
