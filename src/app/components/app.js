import React, { Component } from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom';

import AppHeader from './app-header';
import RegisterPage from './pages/register-page';
import LoginPage from './pages/login-page';
import AppFooter from './app-footer';

import '../styles/app.css';
import PrivateRoute from './private-router';
import UserPage from './pages/user-page';
import Auth from './hoc-helpers/with-auth';
import SearchPage from "./pages/search-page";

export default class App extends Component {
  render() {

      return (
          <BrowserRouter>
              <Auth>
                <AppHeader/>
                  <Switch>
                      <PrivateRoute path={"/user"} component={UserPage}/>
                      <PrivateRoute path={"/search"} component={SearchPage}/>
                      <Route path="/"
                         render={() => <h2>Welcome to FriendsDeliver</h2>}
                         exact />
                      <Route path="/register" component={RegisterPage}/>
                      <Route path="/login" render={() => (
                          <LoginPage/>)}/>
                      <Route render={() => <h2>Page not found</h2>} />
                  </Switch>
                <AppFooter/>
              </Auth>
          </BrowserRouter>
      );
  }
}
