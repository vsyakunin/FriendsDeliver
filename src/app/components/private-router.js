import React, { useContext } from 'react';
import { Route, Redirect } from 'react-router-dom';
import { AuthContext } from './hoc-helpers/with-auth';

const PrivateRoute = ({ component: Component, ...otherProps }) => {
    const { isAuthenticated } = useContext(AuthContext)

    return (
        <Route
            {...otherProps}
            render={props => (
                (
                    isAuthenticated
                        ?
                        <Component {...props} />
                        :
                        <Redirect to={otherProps.redirectTo ? otherProps.redirectTo : '/login'} />
                )
            )}
        />
    )

};


export default PrivateRoute