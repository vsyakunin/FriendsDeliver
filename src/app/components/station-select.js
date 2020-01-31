import React, { Component } from 'react';

export default class StationSelector extends Component {
    state = {
        selectedStation: 0,
        filteredStations: [],
        userInput: ''
    };

    filteredStations = (e) => {
        const userInput = e.currentTarget.value;

        const filteredStations = this.props.stations.filter(({ name }) =>
            name.toLowerCase().indexOf(userInput.toLowerCase()) > -1
        );
        this.setState({
            filteredStations,
            userInput
        });
    };

    onSelectStation = (id, name) => {
        this.setState({
            selectedStation: id,
            filteredStations: [],
            userInput: name
        }, () => {
            if(typeof this.props.onSelectStation !== 'undefined') {
                this.props.onSelectStation(id);
            }
        });
    };

    render() {

        return (
            <div>
                <input className={'form-control'} placeholder={this.props.placeholder}
                       value={this.state.userInput}
                       onChange={this.filteredStations} />
                {this.state.userInput.length > 0 ?
                    <ul className={'suggestions'}>
                        {
                            this.state.filteredStations.map(({name, id, line: { color }}) =>{
                                return (
                                    <li key={id} onClick={() => this.onSelectStation(id, name)}>
                                        <div style={{background: '#'+color}}/>
                                        <div>{name}</div>
                                    </li>
                                )
                            })
                        }
                    </ul>
                : null}
            </div>
        )
    }
}