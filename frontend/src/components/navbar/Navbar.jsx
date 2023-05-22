import React from 'react';
import { Link, NavLink } from 'react-router-dom'
import Logo from './img/monk.svg';

const Navbar = () => {
    return (
        <nav className="navbar navbar-expand-sm navbar-dark bg-primary">
            <div className="container-fluid">
                <Link to="/" className="navbar-brand">
                    <img src={Logo} alt="" width="30" height="24" className="d-inline-block align-text-top" />
                    Monkeys
                </Link>
                <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"></span>
                </button>
                <div className="collapse navbar-collapse" id="navbarNav">
                    <ul className="navbar-nav">
                        <li className="nav-item">
                            <button className="btn btn-outline-light" type="submit">Магазин</button>
                        </li>
                        <li className="nav-item">
                            <NavLink to="/" className={({ isActive }) => { return isActive ? "nav-link active" : "nav-link"; }}>
                                PhotoGen
                            </NavLink>
                        </li>
                        <li className="nav-item">
                            <NavLink to="/2fa" className={({ isActive }) => { return isActive ? "nav-link active" : "nav-link"; }}>
                                2FA генератор
                            </NavLink>
                        </li>
                        <li className="nav-item">
                            <NavLink to="/dashboard" className={({ isActive }) => { return isActive ? "nav-link active" : "nav-link"; }}>
                                Тренды
                            </NavLink>
                        </li>
                        <li className="nav-item">
                            <a className="nav-link" href="/#" tabIndex="-1" aria-disabled="true">Чекер AI</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    );
};

export default Navbar;