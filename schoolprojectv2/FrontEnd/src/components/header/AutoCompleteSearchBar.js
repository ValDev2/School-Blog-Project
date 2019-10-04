import React, { Component } from 'react';
import { connect } from 'react-redux';
import { getPosts } from '../../actions/posts.js';
import './css/AutoCompleteSearchBar.css';

class AutoCompleteSearchBar extends Component {
  constructor(props){
    super(props);
    this.state = {
      suggestions: {
        users: [],
        posts: []
      },
      value: ""
    }
    this.handleChange = this.handleChange.bind(this);
  }

  componentDidMount(){
    this.props.getPosts();
  }

  handleChange(e){
    const value = e.target.value;
    const regex = new RegExp(`${value}`, 'i');
    let postSuggestions = []
    //filtering posts and users
    console.log(this.props)
    if( value.length > 0 ){
      postSuggestions = this.props.posts.filter( item => regex.test(item.title) );
    }
    this.setState({
      suggestions: {...this.state.suggestions, posts: postSuggestions},
      value: value
    });
    console.log(this.state.suggestions);
  }

  render(){
    return(
      <div className="AutoCompleteSearchBar">
        <input type="text" onChange={this.handleChange}/>
        { this.state.suggestions.users.length > 0 || this.state.suggestions.posts.length > 0 &&
          <div className="AutocompleteResults">
            {this.state.suggestions.posts.length > 0 &&
              <ul className="PostResults">
                <span className="AutoComplete-categorie-name post-categorie">post</span>
                <hr />
                { this.state.suggestions.posts.map( item => (
                  <li className="single-post-result">
                    {item.title}
                  </li>
                ))}
              </ul>
            }
          </div>
        }
      </div>
    )
  }
}

const mapStateToProps = state => ({posts: state.posts})

export default connect(mapStateToProps, {getPosts})(AutoCompleteSearchBar);
