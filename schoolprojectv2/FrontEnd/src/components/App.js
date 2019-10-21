import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import { Provider, connect } from 'react-redux';
import { store } from '../store.js';
import AppHeader from './header/AppHeader';
import HomePageStream from './HomePageStream/HomePageStream.js';
import HeaderCategories from './header/HeaderCategories.js';
import ArticleDetails from './ArticleDetails/ArticleDetails.js';
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
                   path="/:category"
                   render={routerProps => <HomePageStream {...routerProps}/>}
            />
            <Route exact
                   path="/article/:slug"
                   render={routerProps => <ArticleDetails {...routerProps}/>}
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
