import React, { Component } from 'react';
import { connect } from 'react-redux';
import { getCategories } from '../../actions/categories';
import './css/HeaderCategories.css';
import { NavLink, Link, Switch } from 'react-router-dom';
import AutoCompleteSearchBar from './AutoCompleteSearchBar';
var slugify = require('slugify')


class HeaderCategories extends Component {

  componentDidMount(){
    this.props.getCategories();
  }


  render(){
    return(
      <div className="HeaderCategories">
        <nav className="HeaderCategories-nav">
          <ul className="categories-list">
            { this.props.categories.map( category => (
              <NavLink exact
                       key={slugify(category.category).toLowerCase()}
                       activeClassName="active_link"
                       to={`/${slugify(category.category).toLowerCase()}`}>
                {category.category}
              </NavLink>
            ))}
          </ul>
        </nav>
      </div>
    )
  }
}

const mapStateToProps = state => {

  return {categories: state.categories.categories}
}


export default connect(mapStateToProps, {getCategories})(HeaderCategories);
