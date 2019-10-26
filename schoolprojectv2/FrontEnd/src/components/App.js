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
import { transitions, positions, Provider as AlertProvider } from 'react-alert'
import AlertTemplate from 'react-alert-template-basic'
import Alerts from './Alerts/Alerts.js';


const options = {
  timeout: 2000,
  position: "top center"
}


class App extends Component {
  render(){
    return(
      <Provider store={store}>
        <AlertProvider template={AlertTemplate}
                       {...options}
        >
          <div className="App">
            <AppHeader />
            <Alerts />
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
        </AlertProvider>
      </Provider>
    )
  }
}

ReactDOM.render(<BrowserRouter>
                  <App />
                </BrowserRouter>, document.getElementById('app'));
