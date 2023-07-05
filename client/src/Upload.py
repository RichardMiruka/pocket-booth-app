import React, { useState } from "react";

function Upload(){
    const [fileInput, setFileInput] = useState(null);
    const [error, setError]= useState(null);

    const types = ['image/png', 'image/jpeg']

    function changeHandler(){
        let selected= e.target.files[0];
        
    }
    return (
        <form>
        <input type="file" onChange={changeHandler}>
        </form>
    )}
                                                         
}