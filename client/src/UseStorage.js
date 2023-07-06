import {useState, useEffect} from 'react'


function UseStorage(file){
    const [progress, setProgress] = useState(0)
    const [url, setUrl] = useState(null);
    const [error, setError] = useState(null);

    useEffect(() => {
        const storageRef = projectStorage.ref(file.name);

        storageRef.put(file).on('state_changed', (snap) =>{
            let percentage = (snap.bytesTransferred/ snap.totalBytes) * 100;
            setProgress(percentage);
        }, (err) => {
            setError(error);
        }, async () => {
            const url = await storageRef.getDownloadUrl();
            setUrl(url);
        })
    }, [file]);
    return{progress, url, error}; //returning progress state to show the upload status in UI component

}

export default UseStorage