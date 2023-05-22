import React from 'react';

const Footer = () => {
    const moment = require('moment');
    const currentDate = moment();


    return (
        <footer className="py-3 my-4">
            <ul className="nav justify-content-center border-bottom pb-3 mb-3">
                <li className="nav-item"><a href="/#" className="nav-link px-2 text-muted">Контакты</a></li>
                <li className="nav-item"><a href="/#" className="nav-link px-2 text-muted">Политика конфиденциальности</a></li>
            </ul>
            <p className="text-center text-muted">© 2020-{currentDate.format("YYYY")} MonkeyTeam</p>
        </footer>
    );
};

export default Footer; 