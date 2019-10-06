import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import './css/App.css';
import { Provider } from 'react-redux';
import { store } from '../store.js';
import AppHeader from './header/AppHeader';
import HeaderCategories from './header/HeaderCategories'
import PostListStream from './posts/PostListStream';
import { BrowserRouter } from "react-router-dom";
import { Route, Switch } from 'react-router-dom';

class App extends Component {
  render(){
    return(
      <Provider store={store}>
        <div className="App">
          <AppHeader />
          <HeaderCategories />
          <Switch>
            <Route exact
                   path="/sciences"
                   render={() => <PostListStream field="sciences" />}
            />
          </Switch>
        </div>
      </Provider>
    )
  }
}

ReactDOM.render(<BrowserRouter>
                  <App />
                </BrowserRouter>, document.getElementById('app'));
