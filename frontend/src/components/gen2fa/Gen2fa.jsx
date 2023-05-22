import React, { useState, useRef, useEffect } from 'react';
import axios from "axios";
import CopyToClipboard from 'react-copy-to-clipboard';

const Gen2fa = () => {
    const [codeValue, setCodeValue] = useState('');
    const [codeWait, setCodeWait] = useState(false);
    const [backCode, setBackCode] = useState('');
    const [prevCodeValue, setPrevCodeValue] = useState('');
    const [timeLeft, setTimeLeft] = useState(0);
    const [percent, setPercent] = useState(0);
    const [seconds, setSeconds] = useState(0);
    const codeField = useRef(null);
    const lifeTime = useRef(null);


    // затычка
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    function secondsUntilNextMinute() {
        const now = new Date();
        const seconds = now.getSeconds();
        if (seconds < 30) {
            return 30 - seconds;
        } else if (seconds < 60) {
            return 60 - seconds;
        } else {
            return 0;
        }
    }

    const sendCode = async e => {
        if ((codeValue.length > 15 && codeValue.length < 33) && (codeValue !== prevCodeValue || (codeValue === prevCodeValue && timeLeft === 0))) {
            codeField.current.classList.remove('is-invalid')
            setPrevCodeValue(codeValue);
            setCodeWait(true);
            await axios({
                method: 'post',
                url: '/doc/codegen/',
                data: { key: codeValue }
            }).then(async (response) => {
                setBackCode(response.data.code);
                setTimeLeft(secondsUntilNextMinute());
                setSeconds(secondsUntilNextMinute())
                setCodeWait(false);
            })
                .catch(error => {
                    console.log(error)
                    setCodeWait(false);
                    codeField.current.classList.add('is-invalid')
                });
        } else {
            codeField.current.classList.add('is-invalid')
        }
    };



    useEffect(() => {
        const intervalId = setInterval(() => {
            setTimeLeft(timeLeft - 1);
            setPercent((100 * (0 + timeLeft)) / seconds);
        }, 1000);

        if (timeLeft === 0) {
            setPercent(-1);
            clearInterval(intervalId)
        };
        if (timeLeft === -1) {
            clearInterval(intervalId);
            setPercent(-1);
        };

        return () => clearInterval(intervalId);
    }, [timeLeft]);



    return (
        <div className="container mb-5 mt-5 pt-5 pb-5">
            <div className="row">
                <div className="col-xl-5 col-lg-8 col-md-9 col-sm-12 mb-4 pt-3 pb-5 ps-5 pe-5 mx-auto shadow rounded-">
                    <p className="lead fs-2 mb-5">2FA генератор</p>
                    <input ref={codeField} className="form-control" type="text" onChange={e => setCodeValue(e.target.value)} placeholder="Secret Key" aria-label="default input example" />
                    <div className="invalid-feedback">
                        Введите корректный ключ
                    </div>
                    <div className="input-group mt-4">
                        <button type="button" className={`btn btn-primary ${codeWait ? "disabled" : ""}`} onClick={sendCode}>Генерировать</button>
                        <input className="form-control" type="text" defaultValue={backCode} placeholder="6-значный код" aria-label="readonly input example" readOnly />
                        <CopyToClipboard text={backCode}>
                            <button type="button" className="btn btn-secondary" ><i className="bi bi-front"></i></button>
                        </CopyToClipboard>
                    </div>
                    {percent > -1
                        ? <>
                            <div className="progress mt-2" role="progressbar" style={{ height: "20px" }}>
                                <div ref={lifeTime} className={`progress-bar progress-bar-striped ${percent > 40 ? "bg-success" : percent <= 40 && percent > 20 ? "bg-warning" : "bg-danger"} progress-bar-animated`} style={{ width: `${percent}%` }}></div>
                            </div>
                            <p className="fw-lighter">{timeLeft} сек.</p>
                        </>
                        : <p className="mt-5"></p>
                    }

                </div>
            </div>
        </div>
    );
};

export default Gen2fa;