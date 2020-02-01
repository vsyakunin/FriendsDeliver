import React, {useContext} from 'react';
import { NavLink, Link } from 'react-router-dom';
import {AuthContext} from './hoc-helpers/with-auth';

const AppHeader = () => {
    const { isAuthenticated, logout } = useContext(AuthContext);

    const Menu = () => {
        return (
            isAuthenticated ?
                <ul className={'nav justify-content-center'}>
                    <li className="nav-item">
                        <NavLink to="/search" className="nav-link" activeClassName={'active'}>Search</NavLink>
                    </li>
                    <li className="nav-item">
                        <NavLink to="/user" className="nav-link" activeClassName={'active'}>My page</NavLink>
                    </li>
                    <li className="nav-item">
                        <span className="nav-link" onClick={ logout }>Logout</span>
                    </li>
                </ul>
                : <ul className={'nav justify-content-center'}>
                    <li className="nav-item">
                        <NavLink to="/register" className="nav-link" activeClassName="active">Register</NavLink>
                    </li>
                    <li className="nav-item">
                        <NavLink to="/login" className="nav-link" activeClassName="active">Login</NavLink>
                    </li>
                </ul>
        )
    };

    return (
        <header className="masthead mb-auto">
            <div className="inner">
                <Link to="/"><h3 className="masthead-brand">FriendsDeliver</h3></Link>
                <nav className="nav nav-masthead">
                    <Menu/>
                </nav>
            </div>
        </header>
    )
};

export default AppHeader;