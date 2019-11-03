import React, { Component } from 'react';
import { connect } from 'react-redux'
import './css/AppHeader.css';
import { makeStyles } from '@material-ui/core/styles';
import { withStyles } from '@material-ui/styles';
import Button from '@material-ui/core/Button';
import AutoCompleteSearchBar from './AutoCompleteSearchBar.js';
import { Link } from 'react-router-dom';


//Material Ui Styling
const styles = {
  button: {
    lineHeight: 0,
    padding: "10px",
    marginLeft: 0,
    fontSize: "10px",
    borderColor: "#00AEAB",
    color: "#00AEAB",
    fontWeight: "500"
  }
}

class AppHeader extends Component {
  constructor(props){
    super(props);
    this.state = {
      isLogin: false,
      isOpen: false,
      searchingValue: "",
      notifsNumber: 0,
    }
    this.toogleIsOpen = this.toogleIsOpen.bind(this);
  }

  toogleIsOpen(){
    this.setState( st => ({
      isOpen: !st.isOpen
    }))
  }

  render(){
    const { classes } = this.props;
    return(
      <div className="AppHeader">
        <nav className="UpperNavBar">
          <div className="logo">
            <Link to="/" className="AppHeader-logowordmark">Garry's</Link>
          </div>
          <div className="Appheader-metabar">
            <ul className="Appheader-metabar-buttons">
              <li className="metabar-button" id="metabar-search-icon">
              { this.state.isOpen === true ? (
                <div className="searching-content">
                <i className="fas fa-search" onClick={this.toogleIsOpen}></i>
                <AutoCompleteSearchBar />
                </div>
              ) : (
                <i className="fas fa-search" onClick={this.toogleIsOpen}></i>
              )}
              </li>
              { this.state.isLogin ? (
                <div>
                  <li className="metabar-button" id="metabar-notification-icon">
                    <i className="far fa-bell"></i>
                  </li>
                  <li className="metabar-button user-profile-icon" id="metabar-profile-icon">
                    <div className="profile-rounded-icon"></div>
                  </li>
                </div>
              ) : (
                <Link to="/authentication/login">
                  <li className="metabar-button user-profile-icon" id="sign-in">
                    <Button variant="outlined" color="primary" className={classes.button}>
                      Sign In
                    </Button>
                  </li>
                </Link>
              )
              }
            </ul>
          </div>
        </nav>
      </div>
    )
  }
}


export default withStyles(styles)(AppHeader);
