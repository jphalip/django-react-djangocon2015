'use strict';

import React from 'react'
import {ProgressBar, Grid} from 'react-bootstrap'
import Reflux from 'reflux'
import photoStore from './store'
import Album from './components/album'
import Actions from './actions'
import $ from 'jquery'


const MainController = React.createClass({
  mixins: [Reflux.connect(photoStore, 'myStore')],

  render() {
    if (! this.state.myStore.isHydrated) {
      // Store hasn't been hydrated yet so we display a progress bar
      return <Grid><ProgressBar active now={100} /></Grid>
    }
    else {
      // The store has data so we can display the album
      return (
        <Album
         photos={this.state.myStore.photos}
         favorites={this.state.myStore.favorites} />
      )
    }
  }

});


function initAjaxHydration(div) {
  /**
   * Hydrates the store with data fetched via Ajax.
   */
  React.render(<MainController />, div);
  setTimeout(() => {  // Simulate slow Internet connection to show the "Loading" state.
    photoStore.fetchData();
  }, 1000);
}


function initSerializedHydration(div) {
  /**
   * Hydrates the store with data accessed from a global variable that has been
   * serialized by the server.
   */
  photoStore.hydrate(
    window.initialData.photos,
    window.initialData.favorites
  );
  React.render(<MainController />, div);
}


function initPreRendered(div) {
  /**
   * Called when the component has already been rendered server-side.
   * Similar to initAjaxHydration() except we wait till the store is hydrated
   * before we render the React component again to avoid flickering — Otherwise
   * the component would be rendered without data, then rendered again with the
   * newly-fetched data, causing some flickering.
   */
  photoStore.fetchData().then(()=>{
    React.render(<MainController />, div);
  });
}


// Figure out which version of our demo to display
var div = document.getElementById('myapp');
switch(window.location.pathname) {
  case '/ajax/':
    initAjaxHydration(div);
    break;
  case '/serialized/':
    initSerializedHydration(div);
    break;
  case '/pre-rendered/':
    initPreRendered(div);
    break;
}