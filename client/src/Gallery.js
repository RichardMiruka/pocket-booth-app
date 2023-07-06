


function Gallery(){
    return (
        <div>
            <h1 className="mt-5 text-centre main heading">Pocket Booth App</h1>
            <div className="menu-tab container">
                <div className="menu-tab d-flex justify center-around">
                    <btn className="button">Homepage</btn>
                    <btn className="button">Favorite</btn>
                    <btn className="button">Private</btn>
                </div>
                <div>
                <input type="search"></input>
                <btn>search</btn>
                </div>
            </div>

        </div>
    )
}

export default Gallery;
