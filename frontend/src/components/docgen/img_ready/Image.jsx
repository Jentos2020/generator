import React, { useContext } from 'react';
import { DocContext } from '../../../context';


const Image = () => {
    const { imgUrl, docLoading } = useContext(DocContext);
    const moment = require('moment');

    
    const downloadHandle = () => {
        const currentDate = moment();
        const link = document.createElement("a");
        link.href = imgUrl;
        link.download = `IMG_${currentDate.format("YYYYMMDD_hhmmss")}`;
        link.click();
    }



    return (
        <div className="col-xl-7 col-lg-7 col-md-12 col-sm-12">
            <div className="shadow-lg p-2 mb-3 bg-body rounded">
                {docLoading
                    ? <div className="d-flex justify-content-center" style={{ marginTop: '100px', marginBottom: '100px' }}>
                        <div className="spinner-border me ms mt-auto" role="status"></div>
                    </div>
                    : <img src={imgUrl} className="rounded img-fluid" alt="zrd_razban_img" />
                }
                <div className="d-grid mt-3">
                    {docLoading
                        ? <button className="btn btn-primary disabled" type="button"><span className="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span></button>
                        : <button className="btn btn-primary" type="button" onClick={downloadHandle}> Скачать <i className="bi bi-cloud-download"></i></button>
                    }
                </div>
            </div>
            <p small="true" className="text-muted mb-3 ms-3 ms-3">*изображения не являются документами и не могут использоваться как настоящие.</p>
        </div>
    );
};

export default Image;