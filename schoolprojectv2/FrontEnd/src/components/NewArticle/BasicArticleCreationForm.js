import React, {Component} from 'react';
import TextField from '@material-ui/core/TextField';
import { withStyles } from '@material-ui/core/styles';
import './css/BasicArticleCreationForm.css';


const styles = {
  TextField: {
    width: "700px",
    height: "500px",
    padding: "5px"
  },
  Title: {
    padding: "5px",
    fontSize: "32px",
    fontWeight: "700",
    width: "700px",
  },
};



class BasicArticleCreationForm extends Component {
  render(){

    const { classes } = this.props;

    return(
        <div className="BasicArticleCreationForm">
            <form noValidate autoComplete="off">
                <div>
                    <TextField
                      id="standard-basic"
                      label="Titre"
                      margin="normal"
                      className={classes.Title}
                      InputLabelProps={{style: {fontSize: 35}}}
                      inputProps={{style: {fontSize: 50}}}
                    />
                </div>
                <div>
                    <TextField
                      id="standard-basic"
                      label="Votre pensée ... "
                      margin="normal"
                      multiline
                      rows="8"
                      rowsMax="100"
                      className={classes.TextField}
                    />
                </div>
            </form>
        </div>
    )
  }
}

export default withStyles(styles)(BasicArticleCreationForm);
