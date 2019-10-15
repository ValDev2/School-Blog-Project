import React, { Component } from 'react';
import { BrowserRouter } from "react-router-dom";
import { Route, Switch } from 'react-router-dom';
import HeaderCategories from './header/HeaderCategories'
import PostListStream from './posts/PostListStream';
import PostList from './posts/PostList';



class StreamPostSection extends Component {
  render(){
    return(
      <div className="StreamPostSection">
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
    )
  }
}
