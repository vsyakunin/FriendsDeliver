import React, { Component } from "react";
import ApiService from '../../services/api';
import StationSelector from '../station-select';

export default class UserPage extends Component {
    state = {
        stations: [],
        fromStation: 0,
        toStation: 0
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
        const { [name]: old_id = 0 } = this.state;
        this.setState({[name]: id}, () => {
            this.api.setFavouritesStations(id, old_id)
                .then((res) => res.json())
                .then(() => {
                    alert('Your station save')
                })
        })
    }

    render() {

        return (
            <main role="main" className={'inner cover'}>
                <div className={'userpage'}>
                    <h3>Please select your stations:</h3>
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
                </div>
            </main>
        );
    }
}