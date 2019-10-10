import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import './css/App.css';
import { Provider } from 'react-redux';
import { store } from '../store.js';
import AppHeader from './header/AppHeader';
import HeaderCategories from './header/HeaderCategories'
import PostListStream from './posts/PostListStream';
import PostList from './posts/PostList';
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
                   key="sciences"
                   path="/sciences"
                   render={() => <PostListStream field="sciences" />}
            />
            <Route exact
                   key="littérature"
                   path="/littérature"
                   render={() => <PostListStream field="littérature" />}
            />
            <Route exact
                   key="sciences-sociales"
                   path="/sciences-sociales"
                   render={() => <PostListStream field="sciences-sociales" />}
            />
          </Switch>
          <PostList />
        </div>
      </Provider>
    )
  }
}

ReactDOM.render(<BrowserRouter>
                  <App />
                </BrowserRouter>, document.getElementById('app'));
