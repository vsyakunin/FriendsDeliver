export default class ApiService {
    _apiHost = 'http://127.0.0.1:5000';
    _apiBase = this._apiHost + '/v1';
    _apiLogin = this._apiHost + '/login';
    _apiRegister = this._apiHost + '/registration';

    fetch(url, method = 'GET', params) {
        params = {
            ...params,
            method: method,
            headers: {
                'Content-Type': 'Application/json',
                'Authorization': 'Bearer ' + window.localStorage.getItem('accessToken')
            }
        };
        return fetch(url, params);
    }

    async getResource(url) {
        const res = await fetch(
            `${this._apiBase}${url}`,
            {
                headers: {
                    Authorization: "Bearer " + window.localStorage.getItem('accessToken')
                }
            }
        );
        return await res.json();
    }

    getAllStation() {
        return this.getResource('/stations/');
    }
    getUsers(from, to) {
        return this.getResource('/stations/users/');
    }

    checkIsAuthenticated() {
        return window.localStorage.getItem('accessToken') !== null &&
            window.localStorage.getItem('accessToken') !== "";
    }

    authLogin(credentials) {
        return this.fetch(this._apiLogin, 'POST',
            {
                body: JSON.stringify(credentials)
            }).then(res => {
            if(res.status !== 200) {
                throw new Error("");
            }
            return res.json()
        })
    }

    authLogout() {
        window.localStorage.removeItem('accessToken');
    }

    authSignUp(credentials) {
        return this.fetch(this._apiRegister, 'POST',
            {
                body: JSON.stringify(credentials)
            })
    }

    searchUsers(from_station, to_station) {
        return this.fetch(`${this._apiBase}/stations/users/?from=${from_station}&to=${to_station}`)
    }


    setFavouritesStations(station_id, old_station_id) {
        return this.fetch(`${this._apiBase}/user/stations/`, 'POST',
            {
                body: JSON.stringify({
                    station_id,
                    old_station_id,
                    weekday: 0
                })
            })
    }

    auth() {

    }
}