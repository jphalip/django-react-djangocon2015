import React from 'react'
import {
  Thumbnail, ButtonGroup, Button, ButtonToolbar, ListGroupItem, Col, Row
} from 'react-bootstrap'
import {
  LAYOUT_THUMBNAILS, LAYOUT_LIST, TYPE_ALL, TYPE_COLOR, TYPE_BW, ControlBar
} from './control-bar'
import {isFavorite} from '../utils'
import Actions from '../actions'


const PhotoPanel = React.createClass({

  getInitialState() {
    return {
      layout: LAYOUT_THUMBNAILS,
      photoType: TYPE_ALL
    };
  },


  /**
   * Returns the filtered list of photos that have the given photoType
   * (Color or Black & White).
   */
  filterPhotos(photos, photoType) {
    return photos.filter((photo) => {
      switch (photoType) {
        case TYPE_COLOR:
          // Only return color photos
          return photo.is_color;
        case TYPE_BW:
          // Only return B&W photos
          return !photo.is_color;
        default:
          // Return all photos
          return true;
      }
    });
  },


  /*****************************************************************
   *
   * EVENT HANDLERS
   *
   *****************************************************************/

  onPhotoTypeChange(photoType) {
    this.setState({photoType: photoType});
  },

  onLayoutChange(layout) {
    this.setState({layout: layout});
  },


  /*****************************************************************
   *
   * RENDERING
   *
   *****************************************************************/

  /**
   * Main render function.
   */
  render() {
    let filteredPhotos = this.filterPhotos(
      this.props.photos, this.state.photoType
    );

    return (
      <div className="album">
        <ControlBar
         layout={this.state.layout}
         photoType={this.state.photoType}
         onPhotoTypeChange={this.onPhotoTypeChange}
         onLayoutChange={this.onLayoutChange}
        />
        <Row>
          {this.renderPhotos(filteredPhotos)}
        </Row>
      </div>
    )
  },

  /**
   * Renders the given photos.
   */
  renderPhotos(photos) {
    return photos.map((photo) => {
      // Compute the photo's attributes
      let photoIsFavorite = isFavorite(this.props.favorites, photo.id);
      let style = photoIsFavorite ? {backgroundColor: '#F65374'} : {};
      let action = Actions.toggleFavorite.bind(this, photo);

      // Render the photo as thumbnail or list item based on the
      // selected layout option
      switch (this.state.layout) {
        case LAYOUT_THUMBNAILS:
          return this.renderPhotoAsThumbnail(photo, style, action);
          break;
        case LAYOUT_LIST:
          return this.renderPhotoAsListItem(photo, style, action);
          break;
      }
    });
  },

  /**
   * Renders a single photo as a thumbnail.
   */
  renderPhotoAsThumbnail(photo, style, action) {
    return (
      <Col md={4} sm={4} key={photo.id}>
        <Thumbnail src={photo.url} onClick={action} style={style} />
      </Col>
    )
  },

  /**
   * Renders a single photo as a list item.
   */
  renderPhotoAsListItem(photo, style, action) {
    return (
      <ListGroupItem key={photo.id} onClick={action} style={style}>
        <img src={photo.url} width={60}/>
      </ListGroupItem>
    )
  }

});


export default PhotoPanel;