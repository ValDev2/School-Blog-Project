import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { store } from '../store.js';
import { BrowserRouter } from "react-router-dom";
import Container from './Container.js';



class App extends Component {
  render(){
    return(
      <Provider store={store}>
          <Container />
      </Provider>
    )
  }
}

ReactDOM.render(<BrowserRouter>
                  <App />
                </BrowserRouter>, document.getElementById('app'));

export default App;
