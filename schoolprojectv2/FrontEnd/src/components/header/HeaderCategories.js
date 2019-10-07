import React, { Component } from 'react';
import { connect } from 'react-redux';
import { getCategories } from '../../actions/categories';
import './css/HeaderCategories.css';
import { Route, Switch, NavLink } from 'react-router-dom';
import AutoCompleteSearchBar from './AutoCompleteSearchBar';
var slugify = require('slugify')


class HeaderCategories extends Component {

  componentDidMount(){
    console.log("CALLING THE API !!!! ")
    this.props.getCategories();
  }

  render(){
    console.log("LES PROPS : ")
    console.log(this.props)
    return(
      <div className="HeaderCategories">
        <nav className="HeaderCategories-nav">
          <ul className="categories-list">
            { this.props.categories.map( categorie => (
              <NavLink exact
                       key={slugify(categorie.category).toLowerCase()}
                       className="nav_link"
                       activeClassName="active_link"
                       to={`/${slugify(categorie.category).toLowerCase()}`}>
                {categorie.category}
              </NavLink>
            ))}
          </ul>
        </nav>
      </div>
    )
  }
}

const mapStateToProps = state => {
  console.log("LES STATES ! ")
  console.log(state.categories)
  return {categories: state.categories.categories}
}


export default connect(mapStateToProps, {getCategories})(HeaderCategories);
