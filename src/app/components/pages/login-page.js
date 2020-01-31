import React, {Component } from 'react';
import { AuthContext } from '../hoc-helpers/with-auth';
import { withRouter } from 'react-router-dom';

class LoginPage extends Component {
    static contextType = AuthContext;
    state = {
        email: "",
        password: "",
        remember: false,
    };

    handleLogin = (e) => {
        e.preventDefault();
        const { email, password, remember } = this.state;
        const data = {email: email, password: password, remember: remember};
        this.context.login(data)
    };

    handleChange = (e) => {
        this.setState({
            [e.target.name]: e.target.value
        })
    };

    render() {
        if(this.context.isAuthenticated) {
            this.props.history.push('/user')
        }
        return (
            <main role="main" className="inner cover">
                {
                    this.context.isRegistered ?
                        <div className={'alert alert-success text-center'}>
                             You success registered! Please, login :)
                        </div>
                        : null
                }
                <form className="form-signin" onSubmit={this.handleLogin}>
                    <h1 className="h3">Please sign in</h1>
                    <label htmlFor="inputEmail" className="sr-only">Email address</label>
                    <input type="email" id="inputEmail" name="email" className="form-control" placeholder="Email address"
                           value={this.state.email} onChange={this.handleChange}/>
                    <label htmlFor="inputPassword" className="sr-only">Password</label>
                    <input type="password" id="inputPassword" name="password" className="form-control" placeholder="Password"
                           value={this.state.password} onChange={this.handleChange}/>
                    <div className="checkbox mb-3">
                        <label>
                            <input type="checkbox" value={this.state.remember}
                                   onClick={ () => {this.setState({remember: !this.state.remember });}}/>
                            Remember me
                        </label>
                    </div>
                    <button className="btn btn-lg btn-light btn-block" type="submit" onClick={this.handleLogin}>Sign in</button>
                </form>
            </main>
        );
    }
}

export default withRouter(LoginPage)