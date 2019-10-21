import React, { Component } from 'react';
import { BrowserRouter } from 'react-router-dom';
import { Route, Switch } from 'react-router-dom';
import PostListStream from './PostListStream/PostListStream';
import PostList from './PostList/PostList';
import { connect } from 'react-redux';
import {getPostsByCategory} from '../../actions/posts';

class StreamPostSection extends Component {
  constructor(props){
    super(props);
    this.sortByHottest = this.sortByHottest.bind(this);
    this.handleDisplay = this.handleDisplay.bind(this);
  }

  //Getting Datas
  componentDidMount(){
    this.props.getPostsByCategory(this.props.match.params.category);
  }

  //Get posts depending on the url parameter
  componentDidUpdate(prevProps){
    if (prevProps.match.params.category !== this.props.match.params.category){
      this.props.getPostsByCategory(this.props.match.params.category);
    }
  }

  sortByHottest(){
    const posts = this.props.posts;
    //sorting posts by their like number value
    const compare = (a,b) => {
      if (b.like_number > a.like_number){
        return 1
      } else if (b.like_number < a.like_number){
        return -1
      }
      return 0;
    }
    return posts.sort(compare).slice(0,4);
    }


  handleDisplay(){
    const category = this.props.match.params.category;
    if(this.props.posts.length === 0){
      return <p></p>
    } else {
      return(
        <div className="StreamPostSection">
          <PostListStream category={category} posts={this.sortByHottest()} />
          <PostList category={category} posts={this.sortByHottest().slice(3)}/>
        </div>
      )
    }
  }

  render(){
    console.log(this.sortByHottest().slice(3));
    return(
      this.handleDisplay()
    )
  }
}



const mapStateToProps = state => {
  return {
    posts: state.homePage.postList.posts
  };
}

export default connect(mapStateToProps,{getPostsByCategory})(StreamPostSection);
