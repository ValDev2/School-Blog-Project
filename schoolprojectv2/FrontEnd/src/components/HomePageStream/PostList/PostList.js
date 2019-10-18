import debounce from "lodash.debounce";
import React, { Component } from 'react';
import StreamCardItem from '../cards/StreamCardItem';
import { connect } from 'react-redux';
import './css/PostList.css';

class PostList extends Component {
  constructor(props){
    super(props);
    this.state = {
      posts: []
    }
  }
  componentDidMount(){
  }

  render(){
    return(
      <div className="PostList">
        <div className="PostListContent">
          <StreamCardItem />
          <StreamCardItem />
          <StreamCardItem />

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
