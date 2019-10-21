import debounce from "lodash.debounce";
import React, { Component } from 'react';
import StreamCardItem from '../cards/StreamCardItem';
import { connect } from 'react-redux';
import './css/PostList.css';

class PostList extends Component {
  render(){
    return(
      <div className="PostList">
        <div className="PostListContent">
          {this.props.posts.map( post => (
            <StreamCardItem post={post}/>
          ))}
        </div>
        <div className="PostListSideBar">
          <aside className="PostListSideBarAside">
            <div className="PostListSideBarTittle">
              <h2>Nos Top Utilisateurs </h2>
              <ul className="SideBarBestUser">
                <li></li>
              </ul>
            </div>
          </aside>
        </div>
      </div>
    )
  }
}

export default PostList;
