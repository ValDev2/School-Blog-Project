import React, {Component} from 'react';



class BasicArticleCreationForm extends Component {

  render(){
    return(
        <div className="BasicArticleCreationForm">
            <form className={classes.root} noValidate>
                  <CssTextField className={classes.margin} id="custom-css-standard-input" label="Custom CSS" />
                  <CssTextField
                    className={classes.margin}
                    label="Custom CSS"
                    variant="outlined"
                    id="custom-css-outlined-input"
                  />
                  <ThemeProvider theme={theme}>
                    <TextField
                      className={classes.margin}
                      label="ThemeProvider"
                      id="mui-theme-provider-standard-input"
                    />
                    <TextField
                      className={classes.margin}
                      label="ThemeProvider"
                      variant="outlined"
                      id="mui-theme-provider-outlined-input"
                    />
                  </ThemeProvider>
            </form>
        </div>
    )
  }
}
