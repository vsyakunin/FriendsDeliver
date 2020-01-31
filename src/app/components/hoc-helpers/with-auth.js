import React, { useState } from 'react';
import ApiService from '../../services/api';
import { withRouter } from 'react-router-dom';

export const AuthContext = React.createContext({});

const Auth = withRouter(({ children, history }) => {
    const api = new ApiService();

    const [isAuthenticated, setIsAuthenticated] = useState(api.checkIsAuthenticated());
    // const [isLoading, setIsLoading] = useState(true);
    const [isRegistered, setIsRegistered] = useState(false);

    // авторизация
    const login = credentials => api.authLogin(credentials)
        .then(setIsAuthenticated(true))
        .then(setIsRegistered(false))
        .then((json) => {
            const { access_token = '' } = json;
            window.localStorage.setItem('accessToken', access_token);
            history.push('/user');
        })
        .catch(error => {
            alert(error);
            setIsAuthenticated(false)
        });

    // выход
    const logout = () => {
        api.authLogout();
        setIsAuthenticated(false)
    };

    // регистрация
    const signUp = credentials => api.authSignUp(credentials)
        .then(() => {
            setIsRegistered(true);
            history.push('/login');
        })
        .catch(error => {
            alert(error);
            setIsAuthenticated(false)
        });

    return (
        <AuthContext.Provider value={{ isAuthenticated, isRegistered, login, logout, signUp }}>
            {children}
        </AuthContext.Provider>
    )
});

export default Auth;