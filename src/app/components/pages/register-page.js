import React, { Component } from 'react';
import { AuthContext } from '../hoc-helpers/with-auth';

export default class RegisterPage extends Component {
    static contextType = AuthContext;
    state = {
        name: "",
        email: "",
        password: "",
        password_confirm: "",
        delivers: false,
    };

    handleSubmit = (e) => {
        e.preventDefault();

        const { name, email, password, password_confirm, delivers } = this.state;
        const data = {name: name, email: email, password: password,
            password_confirm: password_confirm, delivers: delivers};

        this.context.signUp(data);

    };

    handleChange = (e) => {
        this.setState({
            [e.target.name]: e.target.value
        })
    };

    render() {
        return (
            <main role="main" className="inner cover">

                {
                    this.state.password !== this.state.password_confirm ?
                        <div className={'alert alert-danger text-center'}>
                            You passwords do not match!
                        </div>
                        : null
                }


                <form className="form-register" onSubmit={this.handleSubmit}>
                    <h1 className="h3">Register</h1>
                    <label htmlFor="inputName" className="sr-only">Name</label>
                    <input type="text" id="inputName" name="name" className="form-control" placeholder="Name"
                           value={this.state.name} onChange={this.handleChange} required/>
                    <label htmlFor="inputEmail" className="sr-only">Email address</label>
                    <input type="email" id="inputEmail" name="email" className="form-control" placeholder="Email address"
                           value={this.state.email} onChange={this.handleChange} required/>
                    <label htmlFor="inputPassword" className="sr-only">Password</label>
                    <input type="password" id="inputPassword" name="password" className="form-control" placeholder="Password"
                           value={this.state.password} onChange={this.handleChange} required/>
                    <label htmlFor="inputRetryPassword" className="sr-only"> Retry password</label>
                    <input type="password" id="inputRetryPassword"  name="password_confirm" className="form-control" placeholder="Retry password"
                           value={this.state.password_confirm} onChange={this.handleChange} required/>
                    <div className="checkbox mb-3">
                        <label>
                            <input type="checkbox" name="delivers" value={this.state.delivers}
                                   onClick={ () => {this.setState({delivers: !this.state.delivers });}}/>
                            I agree to deliver packages
                        </label>
                    </div>
                    <button className="btn btn-lg btn-light btn-block" type="submit">Register</button>
                </form>
            </main>
        );
    }
}
