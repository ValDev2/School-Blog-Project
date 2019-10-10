import debounce from "lodash.debounce";
import React, { Component } from 'react';
import SmallCard from './cards/SmallCard';
import { connect } from 'react-redux';
import { getPostByCategoryType } from '../../actions/posts';
import './css/PostList.css';

class PostList extends Component {
  constructor(props){
    super(props);
    this.state = {
      erre: false,
      hasMore: true,
      isLoading: false,
      posts: []
    }
    window.onscroll = debounce(() => {
      const {
        loadUsers,
        state: {
          error,
          isLoading,
          hasMore,
        },
      } = this;

      if ( error || isLoading || hasMore ) return;
      if (window.innerHeight + document.documentElement.scrollTop === document.documentElement.offsetHeight) {
        //implement Load Posts !
      }
      }, 100);
    }


  componentDidMount(){
    console.log("MOUNTING !!");
    this.props.getPostByCategoryType(this.props.categoryType);
    console.log(this.props)
  }

  render(){
    console.log("MES PROPS !")
    console.log(this.props);
    return(
      <div className="PostList">
        <div className="PostListContent">
        {this.props.posts.map( post => (
          <SmallCard />
        ))}
        </div>
        <div className="PostListSideBar">
          <aside className="PostListSideBar">
            <div className="PostListSideBarTittle">
              <h2>Best Users</h2>
              <ul className="SideBarBestUser">
                <li>Jean</li>
              </ul>
            </div>
          </aside>
        </div>
      </div>
    )
  }
}

const mapStateToProps = state => {
  console.log("STATES !!!");
  console.log(state);
  return {
    categoryType: state.categoryFields.category_type,
    posts: state.posts
  }
}


export default connect(mapStateToProps, { getPostByCategoryType })(PostList);
