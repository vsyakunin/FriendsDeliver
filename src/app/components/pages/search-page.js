import React, { Component } from "react";
import ApiService from '../../services/api';
import StationSelector from '../station-select';

export default class SearchPage extends Component {
    state = {
        stations: [],
        fromStation: 0,
        toStation: 0,
        users: []
    };

    componentDidMount() {
        this.api = new ApiService();
        this.getStations();
    }

    getStations() {
        this.api.getAllStation()
            .then(stations => this.setState({ stations }));
    }

    saveStation(id, name) {
        this.setState({ [name]: id }, () => {
            const { fromStation, toStation } = this.state;
            if(fromStation && toStation) {
                this.api.searchUsers(fromStation, toStation)
                    .then((res) => res.json())
                    .then((users) => {
                        this.setState({ users })
                    })
            }
        })
    }

    render() {

        return (
            <main role="main" className={'inner cover'}>
                <div className={'searchpage'}>
                    <h3>Please select "from" and "to" stations for delivery:</h3>
                    <form>
                        <div className={'row'}>
                            <div className={'col'}>
                                <StationSelector
                                    onSelectStation={(id) => this.saveStation(id, 'fromStation')}
                                    placeholder={'From'} stations={this.state.stations}/>
                            </div>

                            <div className={'col'}>
                                <StationSelector
                                    onSelectStation={(id) => this.saveStation(id, 'toStation')}
                                    placeholder={'To'} stations={this.state.stations}/>
                            </div>
                        </div>
                    </form>
                    {
                        this.state.toStation && this.state.fromStation ?
                            this.state.users.length > 0 ?
                                this.state.users.map(({ id, name }) => {
                                    return (
                                        <p key={id}>{name}</p>
                                    )
                                })
                            : <p>Users not found, please try later!</p>
                        : null
                    }
                </div>
            </main>
        );
    }
}