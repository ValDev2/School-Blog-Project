import React, {Component} from 'react';
import { connect } from 'react-redux';
import {authLogin} from '../../actions/authentication.js';
import CircularProgress from '@material-ui/core/CircularProgress';
import Input from '@material-ui/core/Input';
import InputLabel from '@material-ui/core/InputLabel';
import InputAdornment from '@material-ui/core/InputAdornment';
import FormControl from '@material-ui/core/FormControl';
import TextField from '@material-ui/core/TextField';
import Grid from '@material-ui/core/Grid';
import AccountCircle from '@material-ui/icons/AccountCircle';
import Button from '@material-ui/core/Button';
import './css/Login.css';



class Login extends Component {

  constructor(props){
    super(props);
    this.state = {
      email: "",
      password: ""
    }
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(e){
    this.setState({[e.target.name]: e.target.value});
    console.log(this.state)
  }

  handleSubmit(e){
    e.preventDefault();
    this.props.authLogin(this.state.email, this.state.password);
  }

  render(){
    return(
      <section className="Login">
          <div className="Login-content">
              <div className="Login-text">
                  <h1 className="Login-introduction">
                    Se connecter
                  </h1>
                  <h2 className="Login-subtitle">
                    Entrez vos identifiants
                  </h2>
              </div>
              <div className="Login-form-content">
                  <div style={{fontSize: "20px"}} className="login-form">
                      <Grid container spacing={1} alignItems="flex-end" className="form-input" style={{fontSize: "20px"}}>
                          <Grid item>
                            <TextField id="input-with-icon-grid" label="Email" onChange={this.handleChange} name="email"/>
                          </Grid>
                      </Grid>
                      <Grid container spacing={1} alignItems="flex-end" className="form-input">
                          <Grid item>
                            <TextField id="input-with-icon-grid" label="Password" onChange={this.handleChange} type="password" name="password" className="form-label"/>
                          </Grid>
                      </Grid>
                      <div className="submit-button">
                          { this.props.loading === true ? (
                              <CircularProgress disableShrink />
                          ) : (
                              <Button variant="outlined" size="large" color="primary" onClick={this.handleSubmit} className="submit-button">
                                submit
                              </Button>
                          )}

                      </div>
                  </div>
              </div>
          </div>
      </section>
    )
  }
}

const mapStateToProps = state => {
  console.log(state);
  return {
    token: state.authentication.token,
    loading: state.authentication.loading
  }
}

export default connect(mapStateToProps, {authLogin})(Login);
