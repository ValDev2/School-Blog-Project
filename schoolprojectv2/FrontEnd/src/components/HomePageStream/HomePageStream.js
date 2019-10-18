import React, { Component } from 'react';
import { BrowserRouter } from 'react-router-dom';
import { Route, Switch } from 'react-router-dom';
import PostListStream from './PostListStream/PostListStream';
import PostList from './PostList/PostList';
import { connect } from 'react-redux';
import {getPostsByCategory} from '../../actions/posts';

class StreamPostSection extends Component {

  componentDidMount(){
    this.props.getPostsByCategory(this.state.category)
  }

  constructor(props){
    super(props);
    this.state = {
      category: this.props.match.params.category
    }
  }
  render(){
    return(
      <div className="StreamPostSection">
        <PostListStream category={this.state.category}/>
        <PostList/>
      </div>
    )
  }
}

const mapStateToProps = state => {
  return {
    posts: state
  }
}

export default connect(mapStateToProps,{getPostsByCategory})(StreamPostSection);
