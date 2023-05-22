import React, { useState } from 'react';
import { DocContext } from '../../context';
import Form from './form/Form';
import Header from './header/Header';
import Image from './img_ready/Image';

const Monkeygen = () => {
    // это для запуска через докер(?)
    // const [imgUrl, setImgUrl] = useState('preview_img.jpg');
    const [imgUrl, setImgUrl] = useState('http://localhost:8000/media/preview_img.jpg');
    const [docLoading, setDocLoading] = useState(false); 
    
    return (
        <div className="container mt-3">
            <div className="row">
                <DocContext.Provider value={{imgUrl, setImgUrl, docLoading, setDocLoading}}>
                    <Header />
                    <Form />
                    <Image />
                </DocContext.Provider>
            </div>
        </div>
    );
};

export default Monkeygen; 