import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import {connect } from 'react-redux';
import AppHeader from './header/AppHeader';
import HomePageStream from './HomePageStream/HomePageStream.js';
import HeaderCategories from './header/HeaderCategories.js';
import ArticleDetails from './ArticleDetails/ArticleDetails.js';
import { Route, Switch, Redirect } from 'react-router-dom';
import {authStateCheck} from '../actions/authentication.js';
import { Provider } from 'react-redux'
import { store } from '../store.js';
import { BrowserRouter } from "react-router-dom";
import Login from './Authentication/Login.js';
import Alert from './Alert/Alert.js';

class Container extends Component {

  componentDidMount(){
    this.props.authStateCheck();
  }

  render(){
    const { classes } = this.props;
    return(
      <div className="Container">
        <Provider store={store}>
            <AppHeader {...this.props}/>
            <Alert />
            <HeaderCategories {...this.props}/>
            <Switch>
                <Route exact
                       path="/:category"
                       render={routerProps => <HomePageStream {...routerProps} {...this.props}/>}
                />
                <Route exact
                       path="/article/:slug"
                       render={routerProps => <ArticleDetails {...routerProps} {...this.props}/>}
                />
                <Route exact
                       path="/authentication/login"
                       render={ routerProps => (this.props.isAuthenticated) ? <Redirect to='/'/> : (<Login {...routerProps}{...this.props} />)}
                />
            </Switch>
        </Provider >
      </div>
    )
  }
}


const mapStateToProps = state => {
  return {
    isAuthenticated: state.authentication.token !== null,
    loading: state.authentication.loading,
  }
}

export default connect(mapStateToProps, {authStateCheck})(Container);
