import React, {Component} from 'react';
import TextField from '@material-ui/core/TextField';
import { withStyles } from '@material-ui/core/styles';
import Button from '@material-ui/core/Button';
import OutlinedInput from '@material-ui/core/OutlinedInput';
import InputLabel from '@material-ui/core/InputLabel';
import FormControl from '@material-ui/core/FormControl';
import { InputAdornment } from '@material-ui/core';
import './css/ExtraInfosArticleCreationForm.css';



const styles = {
  TextField: {
    width: "700px",
    marginBottom: "20px"
  },
  previewTitle: {
    fontSize: "26px",
    fontWeight: "700",
    width: "700px",
  },
  tagInput: {
    fontSize: "18px",
    marginBottom: "15px"
  },
  publishBtn: {
    backgroundColor: "#00aeab",
    color: "#fff",
    border: "none",
    "&:hover": {
        backgroundColor: "#00aeab"
    }
  },
  BackBtn: {

  }
};



class ExtraInfosArticleCreationForm extends Component {
  constructor(props){
    super(props),
    this.state = {};
    this.continue = this.continue.bind(this);
    this.back = this.back.bind(this);
  }

  continue(e){
    e.preventDefault();
    this.props.nextStep();
  }

  back(e){
    e.preventDefault();
    this.props.previousStep();
  }

  render(){
    const { classes } = this.props;
    return(
        <div className="ExtraInfosArticleCreationForm">
            <div class="ExtraInfosForm">
                <div class="NewarticlePreview">
                    <h2>Story Preview</h2>
                    <div class="NewArticleImage"></div>
                    <div class="NewArticlePreviewText">
                        <TextField
                          id="standard-basic"
                          label=""
                          margin="normal"
                          className={classes.previewTitle}
                          InputLabelProps={{style: {fontSize: 25}}}
                          inputProps={{style: {fontSize: 50}}}
                        />
                        <TextField
                          id="standard-basic"
                          label=""
                          margin="normal"
                          InputLabelProps={{style: {fontSize: 18}}}
                          inputProps={{style: {fontSize: 25, color: "#8f8f8f", marginTop: 10, marginBottom: 10 }}}
                        />
                        <p class="NewArticlePreviewNote">
                            <strong>Important</strong> : Cette preview vous permet de visualiser votre Article sur le site. C'est comme cela qu'il apparaitra au près de la communauté !
                        </p>
                    </div>
                </div>
            </div>
            <div class="NewArticleTags">
                <p><strong>Tags : </strong>Ajoutez jusqu'à 5 tags pour renseigner la communauté du contenu de votre site</p>
                <FormControl fullWidth className={classes.margin} variant="outlined">
                    <TextField
                      id="outlined-full-width"
                      label="Tags"
                      style={{ margin: 8 }}
                      fullWidth
                      margin="normal"
                      InputLabelProps={{
                        shrink: true,
                        color: "red"
                      }}
                      inputProps={{className: classes.tagInput}}
                      variant="outlined"
                    />
                </FormControl>
            </div>
            <div class="NewArticleReadyToPublish">
                <p><strong>Prêt à Publier votre Article à la communauté ?</strong></p>
                <ul>
                    <div class="NewArticlePublishBtn">
                        <Button color="primary" className={classes.publishBtn} onClick={this.continue}>
                            Publier
                        </Button>
                    </div>
                    <div class="NewArticlePublishBtn">
                        <Button variant="outlined" className={classes.button} onClick={this.back}>
                            Next
                        </Button>
                    </div>
                </ul>
            </div>
        </div>
    )
  }
}

export default withStyles(styles)(ExtraInfosArticleCreationForm);
