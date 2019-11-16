import React, {Component} from 'react';
import TextField from '@material-ui/core/TextField';
import { withStyles } from '@material-ui/core/styles';
import Button from '@material-ui/core/Button';
import './css/BasicArticleCreationForm.css';

const styles = {
  TextField: {
    width: "700px",
    padding: "5px",
    marginBottom: "20px"
  },
  Title: {
    padding: "5px",
    fontSize: "32px",
    fontWeight: "700",
    width: "700px",
  },
};

class BasicArticleCreationForm extends Component {

  constructor(props){
    super(props),
    this.state = {};
    this.continue = this.continue.bind(this);
  }

  continue(e){
    e.preventDefault();
    this.props.nextStep();
  }

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
                      className={classes.TextField}
                    />
                    <div className="nextStep">
                        <Button variant="outlined" className={classes.button} onClick={this.continue}>
                            Next
                        </Button>
                    </div>
                </div>
            </form>
        </div>
    )
  }
}

export default withStyles(styles)(BasicArticleCreationForm);
