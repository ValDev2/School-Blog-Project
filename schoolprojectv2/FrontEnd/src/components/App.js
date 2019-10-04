import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import './css/App.css';
import { Provider } from 'react-redux';
import { store } from '../store.js';
import AppHeader from './header/AppHeader.js';

class App extends Component {
  render(){
    return(
      <Provider store={store}>
        <div className="App">
          <AppHeader />
        </div>
      </Provider>
    )
  }
}

ReactDOM.render(<App />, document.getElementById('app'));
