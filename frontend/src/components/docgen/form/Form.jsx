import React, { useState, useRef, useEffect, useContext } from 'react';
import axios from "axios";
import { DocContext } from '../../../context';

const Form = () => {
    const { imgUrl, setImgUrl, docLoading, setDocLoading } = useContext(DocContext);
    const [imgCount, setImgCount] = useState(null);

    const nameField = useRef(null);
    const surnameField = useRef(null);
    const sexField = useRef(null);
    const dateField = useRef(null);

    const [formData, setFormData] = useState({
        name: '',
        surname: '',
        patronymic: '',
        sex: 'female',
        birthday: '',
        inputState: 'UA',
        metadata: false,
    });

    useEffect(() => {
        sexField.current.setAttribute("checked", "");
        axios.get('/doc')
            .then(response => {
                setImgCount(response.data.imgCount);
            })
    }, []);


    const handleSubmit = async e => {
        e.preventDefault();
        if (document.getElementsByClassName('is-invalid').length > 0 || !formData.birthday.match(/\d{4}-[0-1][0-9]-[0-9]+/) || !formData.name || !formData.surname) {
            if (!formData.name) {
                nameField.current.classList.add('is-invalid')
            } else { nameField.current.classList.remove('is-invalid') }
            if (!formData.surname) {
                surnameField.current.classList.add('is-invalid')
            } else { surnameField.current.classList.remove('is-invalid') }
            if (!formData.birthday.match(/[0-9]+-[0-1][0-9]-\d{4}/)) {
                dateField.current.classList.add('is-invalid')
            } else { dateField.current.classList.remove('is-invalid') }
            if (document.getElementsByClassName('is-invalid').length > 0) {
                return;
            }
        }

        // Создаем док и конвертируем его в base64
        setDocLoading(true)
        await axios({
            method: 'post',
            url: '/doc/create/',
            data: formData
        }).then(async (response) => {
            console.log(response.data)
            setImgCount(imgCount + 1);
            setDocLoading(false);
            setImgUrl(`data:image/jpeg;base64,${response.data}`)
        })
    }

    return (
        <div className="col-xl-5 col-lg-5 col-md-12 col-sm-12">
            <form className="row g-3 me-2" onSubmit={handleSubmit}>
                <div className="col-md-6 col-sm-6">
                    <label htmlFor="name" className="form-label">Имя</label>
                    <input ref={nameField} type="text" className="form-control" id="name" name="name" onChange={e => setFormData({ ...formData, name: e.target.value })} />
                    <div className="invalid-feedback">
                        Заполните поле!
                    </div>
                </div>
                <div className="col-md-6 col-sm-6">
                    <label htmlFor="surname" className="form-label">Фамилия</label>
                    <input ref={surnameField} type="text" className="form-control" id="surname" name="surname" onChange={e => setFormData({ ...formData, surname: e.target.value })} />
                    <div className="invalid-feedback">
                        Заполните поле!
                    </div>
                </div>
                <div className="col-sm-6">
                    <label htmlFor="patronymic" className="form-label">Отчество</label>
                    <input type="text" className="form-control" id="patronymic" name="patronymic" onChange={e => setFormData({ ...formData, patronymic: e.target.value })} />
                </div>
                <div className="col-sm-6">
                    <label htmlFor="sex" className="form-label">Пол</label>
                    <div className="input-group mb-3" id="sex">
                        <div className="form-check form-check-inline">
                            <input className="form-check-input" value="male" type="radio" name="sex" onChange={e => setFormData({ ...formData, sex: e.target.value })} />
                            <label className="form-check-label" htmlFor="inlineRadio1">М</label>
                        </div>
                        <div className="form-check form-check-inline">
                            <input ref={sexField} className="form-check-input" value="female" type="radio" name="sex" onChange={e => setFormData({ ...formData, sex: e.target.value })} />
                            <label className="form-check-label" htmlFor="inlineRadio2">Ж</label>
                        </div>

                    </div>
                </div>
                <div className="col-6">
                    <label htmlFor="inputAddress" className="form-label">Дата рождения</label>
                    <input ref={dateField} type="text" className="form-control" id="birthday" name="birthday" placeholder="дд-мм-гггг" onChange={e => setFormData({ ...formData, birthday: e.target.value })} />
                    <div className="invalid-feedback">
                        Укажите корректную дату рождения.
                    </div>
                </div>
                <div className="col-6">
                    <label htmlFor="inputState" className="form-label">Страна</label>
                    <select id="inputState" name="inputState" className="form-select" defaultValue={'UA'} onChange={e => setFormData({ ...formData, inputState: e.target.value })}>
                        <option value="UA">Ukraine</option>
                        <option value="KZ">Kazakhstan</option>
                        <option value="USA">USA</option>
                    </select>
                </div>
                <div className="col-12">
                    <div className="form-check form-switch">
                        <input className="form-check-input" type="checkbox" id="metadata" name="metadata" onChange={e => setFormData({ ...formData, metadata: e.target.checked })} />
                        <label className="form-check-label" htmlFor="metadata">Добавлять метаданные</label>
                    </div>
                </div>
                <div className="col-12 mb-3">
                    {docLoading
                        ? <button type="button" className="btn btn-success disabled">
                            Сгенерировать
                            <span className="spinner-border spinner-border-sm ms-2" role="status" aria-hidden="true"></span>
                        </button>
                        : <button type="submit" className="btn btn-success">
                            Сгенерировать
                            <i className="bi bi-person-vcard ms-2"></i>
                        </button>
                    }
                    <p><small className="text-muted">Сгенерировано изображений: {imgCount}</small></p>
                </div>
            </form> 
        </div>
    );
};

export default Form;