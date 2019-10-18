import React, { Component } from 'react';
import { connect } from 'react-redux';
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
  }

  handleChange(e){
    const value = e.target.value;
    const regex = new RegExp(`${value}`, 'i');
    let postSuggestions = []
    //filtering posts and users
    if( value.length > 0 ){
      postSuggestions = this.props.posts.filter( item => regex.test(item.title) );
    }
    this.setState({
      suggestions: {...this.state.suggestions, posts: postSuggestions},
      value: value
    });
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


export default AutoCompleteSearchBar;
