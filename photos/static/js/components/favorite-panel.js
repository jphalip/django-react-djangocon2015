import React from 'react'
import {
    Thumbnail, Badge, ButtonToolbar, Well, ListGroupItem, Grid, Col, Row
  } from 'react-bootstrap'
import Actions from '../actions'


const FavoritePanel = React.createClass({

  render() {

    if (! this.props.favorites.length) {
      // Don't display anything if there are no favorites
      return null;
    }

    // Create the thumbnails
    let thumbnails = this.props.favorites.map((favorite) => {
      let action = Actions.removeFromFavorites.bind(this, favorite);
      return (
        <Thumbnail
         src={favorite.photo.url} key={favorite.photo.id}
         onClick={action}
        />
      )
    });

    return (
      <div className="favorites">
        <h4>Favorites <Badge>{thumbnails.length}</Badge></h4>
        <Well>
          <Row>
            {thumbnails}
          </Row>
        </Well>
      </div>
    )
  }

});


export default FavoritePanel;